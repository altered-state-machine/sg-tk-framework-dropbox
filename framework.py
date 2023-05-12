# Copyright (c) 2020 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
A framework that handles uploading and downloading of files from a Dropbox storage provider.
"""
import os
import sys

import sgtk


class DropboxStorageFramework(sgtk.platform.Framework):
    def init_framework(self):
        """
        Construction
        """
        self.log_debug("%s: Initializing..." % self)

        # initialize dropbox sdk:
        self.__init_dropbox_sdk()

        self.connection = self.import_module("connection")
        self.auth = self.import_module("auth")

    def upload_publish(self, published_file):
        """
        Uploads a PublishedFile's path to the remote storage.
        :param published_file: dict
        :return: str path to uploaded file
        """
        paths = self.upload_publishes([published_file])[0]
        return paths[0] if len(paths) else None

    def upload_publishes(self, published_files):
        """
        Uploads a list of PublishedFile's paths to the remote storage.
        :param published_files: list of dicts
        :return: list of strings to the uploaded files
        """

        team_api, user_api = self.connection.connect()

        uploaded_files = []
        try:
            for published_file in published_files:
                self.engine.show_busy(
                    "Uploading", "Sending to remote: %s ..." % published_file["code"]
                )
                self.logger.debug("Executing upload hook for %s" % published_file)
                uploaded_files.append(
                    self.execute_hook_method(
                        "hook_provider",
                        "upload",
                        published_file=published_file,
                        dbx=user_api,
                        namespace=self.get_dropbox_project_namespace(team_api)
                    )
                )
        finally:
            self.engine.clear_busy()
        return uploaded_files

    def download_publish(self, published_file):
        """
        Downloads a list of PublishedFiles from the remote storage to the local storage.
        :param published_file: dict
        :return: str path to the downloaded file.
        """
        paths = self.download_publishes([published_file])
        return paths[0] if len(paths) else None

    def download_publishes(self, published_files):
        """
        Downloads a list of PublishedFiles from the remote storage to the local storage.
        :param published_files: list of dicts
        :return: list of strings of paths to the downloaded files.
        """
        downloaded_files = []
        try:
            for published_file in published_files:
                self.engine.show_busy(
                    "Download",
                    "Retrieving from remote: %s ..." % published_file["code"],
                )
                self.logger.debug("Executing download hook for %s" % published_file)
                downloaded_files.append(
                    self.execute_hook_method(
                        "hook_provider",
                        "download",
                        published_file=published_file,

                    )
                )
        finally:
            self.engine.clear_busy()
        return downloaded_files

    def get_dropbox_user(self, dbx_team_api, sg_user):
        """
        Return the Dropbox user associated with the specified Shotgun user
        """
        dropbox_user = self.execute_hook("hook_get_dropbox_user_profile", sg_user=sg_user)
        return dropbox_user

    def get_dropbox_project_namespace(self, dbx_team_api):
        project_namespace = self.execute_hook("hook_get_dropbox_project_namespace",
                                              dbx_team_api=dbx_team_api,
                                              )
        return project_namespace

    # private methods
    def __init_dropbox_sdk(self):
        """
        Make sure that dropbox sdk is available and if it's not then add it to the path if
        we have a version we can use.
        """
        # before-app-launch hook currently handles this step.
        sdk_path = os.path.join(self.disk_location, "resources")
        if sdk_path not in sys.path:
            sys.path.append(sdk_path)
        try:
            from dropbox import Dropbox
        except Exception as e:
            self.log_error(e)
            self.log_error("Failed to load dropbox sdk!")
        else:
            # Dropbox sdk already available!
            self.log_debug("Dropbox sdk successfully loaded!")
            return
