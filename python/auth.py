import os.path
import webbrowser
from pickle import UnpicklingError

import sgtk
from dropbox import DropboxOAuth2FlowNoRedirect


class AuthenticationHandling:
    def __init__(self, fw):
        self._fw = fw
        self._auth = None
        self._token = None

    def authenticate(self):
        """Retrieve App key and secret and attempt to fetch Token"""
        # First, try to get the stored token, hopefully it is not expired, so that we can use it:
        restored_token = self.get_stored_session_token()
        if restored_token:
            return restored_token
        else:
            return self.get_new_token()

    def get_new_token(self):
        result, _ = self._fw.engine.execute_in_main_thread(self.show_ack_form)
        if result:
            # User accepted, and has probably already seen the URL to get Authorisation code
            # It is now time to show the UI to allow him to enter it.
            self._fw.engine.execute_in_main_thread(self.show_enter_auth_code_form)
            if self._token is not None:
                return self._token
            raise ValueError('Token cannot be None')

    def _setup_ack_dlg(self, widget):
        widget.ack_accepted.connect(self._on_ack_confirmed)

    def _setup_token_dlg(self, widget):
        widget.auth_code_entered.connect(self._on_auth_code_entered)

    def show_ack_form(self):

        try:
            from .widgets.acknowledge_token_widget import AcknowledgeFormWidget
            return self._fw.engine.show_modal("Dropbox Acknowledge",
                                              self._fw,
                                              AcknowledgeFormWidget,
                                              setup_proc=self._setup_ack_dlg)
        except Exception as e:
            # TODO: log errors, custom handling etc. for now just pass
            self._fw.logger.debug(e)

    def show_enter_auth_code_form(self):
        try:
            from .widgets.auth_code_token import AuthCodeFormWidget
            result, _ = self._fw.engine.show_modal("Enter Authorization Code",
                                                   self._fw,
                                                   AuthCodeFormWidget,
                                                   setup_proc=self._setup_token_dlg,
                                                   )
        except Exception as e:
            # TODO: log errors, custom handling etc. for now just pass
            self._fw.logger.debug(e)

    def _on_ack_confirmed(self, widget):
        # User confirmed that some actions would be required of him,
        # Now, prepare the Authentication URL and open it for the user
        key = self._fw.get_setting("app_key")
        self._auth = DropboxOAuth2FlowNoRedirect(key, use_pkce=True, token_access_type='offline')
        authorize_url = self._auth.start()
        webbrowser.open(authorize_url)

    def _on_auth_code_entered(self, widget):
        auth_code = widget.auth_code()
        try:
            oauth_result = self._auth.finish(auth_code)
        except Exception as e:
            print('Error: %s' % (e,))
            raise
        self._token = oauth_result.refresh_token
        self.store_session_token()

    def _compute_token_path(self):
        filename = sgtk.util.filesystem.create_valid_filename("token.pk")
        token_cache_dir = self._fw.site_cache_location
        sgtk.util.filesystem.ensure_folder_exists(token_cache_dir)
        token_path = os.path.join(token_cache_dir, filename)
        return token_path

    def store_session_token(self):
        if self._token is not None:
            token_path = self._compute_token_path()
            with open(token_path, "wb") as f:
                sgtk.util.pickle.dump(self._token, f)

    def get_stored_session_token(self):
        token_path = self._compute_token_path()
        if os.path.isfile(token_path) and os.path.exists(token_path):
            with open(token_path, "rb") as f:
                try:
                    return sgtk.util.pickle.load(f)
                except UnpicklingError as e:
                    self._fw.logger.warning(e)
        return None

    def clear_cache(self):
        token_path = self._compute_token_path()
        sgtk.util.filesystem.safe_delete_file(token_path)


def login():
    fw = sgtk.platform.current_bundle()
    return AuthenticationHandling(fw).authenticate()


def clear_cache():
    fw = sgtk.platform.current_bundle()
    AuthenticationHandling(fw).clear_cache()
