import threading

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

import sgtk

# global connection rlock to ensure that attempting to connect to Dropbox happens exclusively this can happen
# if the framework needs to connect from multiple threads, and they enter the correct password for the first thread.
_g_connection_lock = threading.RLock()


class ConnectionHandler:
    def __init__(self, fw):
        """
        Construction
        """
        self._fw = fw
        self._team_api = None

    @property
    def connection(self):
        """
        Returns the Dropbox object for this connection.
        """
        return self._team_api

    def authenticate(self):
        """Retrieve App key and secret and attempt to fetch Token"""
        key = self._fw.get_setting("app_key")
        secret = self._fw.get_setting("app_secret")
        token = self._fw.get_setting("app_token")
        if token:
            # Looks like TOKEN was supplied from framework config,
            # Let's immediately use that to authenticate
            return token

        # Alternatively, we should request user to open web browser and
        # navigate to a page to allow the APP to access their shared folders.
        auth_flow = DropboxOAuth2FlowNoRedirect(key, secret)

        # TODO: Make QWidget UI which will allow for auth token collection from the user.

    def connect_to_dropbox(self):
        if hasattr(self, "_team_api") and hasattr(self, "_user_api"):
            if self._team_api is not None and self._user_api is not None:
                return self._team_api, self._user_api
        # Access token can expire,
        # TODO: Add logic that will check expiry and refresh token when needed.
        # Currently, just get new token by hand
        access_token = self.authenticate()

        team_api = dropbox.DropboxTeam(oauth2_access_token=access_token)

        sg_user = sgtk.util.get_current_user(self._fw.sgtk)
        dbx_profile = self._fw.execute_hook("hook_get_dropbox_user_profile", dbx_team_api=team_api, sg_user=sg_user)
        user_api = team_api.as_user(dbx_profile.team_member_id)

        self._team_api = team_api
        self._user_api = user_api

        return self._team_api, self._user_api

    def connect(self):
        global _g_connection_lock
        _g_connection_lock.acquire()
        try:
            self.connect_to_dropbox()
            try:
                self._fw.log_metric("Connected")
            except:
                # ignore all errors. ex: using a core that doesn't support metrics
                pass

            return self._team_api, self._user_api
        except Exception as e:
            self._fw.logger.debug(e)
            raise
        finally:
            _g_connection_lock.release()


def connect():
    fw = sgtk.platform.current_bundle()
    return ConnectionHandler(fw).connect()
