import sgtk
from sgtk.platform.qt import QtCore, QtGui
from dropbox import DropboxOAuth2FlowNoRedirect


class AuthenticationHandling:
    def __init__(self, fw):
        self._fw = fw

    def authenticate(self):
        """Retrieve App key and secret and attempt to fetch Token"""
        key = self._fw.get_setting("app_key")
        # token = self._fw.get_setting("app_token")
        # if token:
        #     # Looks like TOKEN was supplied from framework config,
        #     # Let's immediately use that to authenticate
        #     # Most likley this is for development use, since Tokens expire
        #     # it is not logical to put it in your App
        #     return token

        # Alternatively, we should request user to open web browser and
        # navigate to a page to allow the APP to access their shared folders.
        auth_flow = DropboxOAuth2FlowNoRedirect(key, use_pkce=True, token_access_type='offline')
        authorize_url = auth_flow.start()

        self._fw.engine.execute_in_main_thread(self.show_ack_form, authorize_url)

        # TODO: Make QWidget UI which will allow for auth token collection from the user.

    def _setup_ack_dlg(self, widget):
        """
        Connects dialog events to the AuthenticationHandling.
        """
        widget.show_ack_clicked.connect(self._on_ack_confirmed)

    def show_ack_form(self, authorize_url):

        try:
            from .widgets.acknowledge_token_widget import AcknowledgeFormWidget
            import webbrowser
            result, _ = self._fw.engine.show_modal("Dropbox Acknowledge",
                                                   self._fw,
                                                   AcknowledgeFormWidget,
                                                   setup_proc=self._setup_ack_dlg)
            if result == QtGui.QDialog.Accepted:
                # all good show the Web page with details
                webbrowser.open(authorize_url)
        except Exception:
            pass

    def _on_ack_confirmed(self):
        pass

    def store_session_token(self, token):
        pass

    def get_stored_session_token(self):
        pass


def login():
    fw = sgtk.platform.current_bundle()
    return AuthenticationHandling(fw).authenticate()
