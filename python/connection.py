import threading

import dropbox
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
        self._retry = 2

    def connect_to_dropbox(self, token):
        if hasattr(self, "_team_api") and hasattr(self, "_user_api"):
            if self._team_api is not None and self._user_api is not None:
                return self._team_api, self._user_api
        # Access token can expire,
        # TODO: Add logic that will check expiry and refresh token when needed.
        # Currently, just get new token by hand
        key = self._fw.get_setting("app_key")
        team_api = dropbox.DropboxTeam(oauth2_refresh_token=token, app_key=key)

        sg_user = sgtk.util.get_current_user(self._fw.sgtk)
        dbx_profile = self._fw.execute_hook("hook_get_dropbox_user_profile", dbx_team_api=team_api, sg_user=sg_user)
        user_api = team_api.as_user(dbx_profile.team_member_id)

        self._team_api = team_api
        self._user_api = user_api

        return self._team_api, self._user_api

    def connect(self, token):
        global _g_connection_lock
        while self._retry >= 0:
            _g_connection_lock.acquire()
            try:
                self.connect_to_dropbox(token)
            except dropbox.exceptions.AuthError as e:
                self._fw.logger.debug(e)
                self._retry -= 1
                token = get_new_token()
                self.connect_to_dropbox(token)
            except Exception as e:
                self._fw.logger.debug(e)
                raise
            finally:
                _g_connection_lock.release()
                break
        else:
            self._fw.logger.error("Cannot connect to cloud storage")
        return self._team_api, self._user_api


def get_token():
    from . import auth
    token = auth.login()
    return token


def get_new_token():
    from . import auth
    auth.clear_cache()
    token = auth.login()
    return token


def connect():
    fw = sgtk.platform.current_bundle()
    token = get_token()
    return ConnectionHandler(fw).connect(token)
