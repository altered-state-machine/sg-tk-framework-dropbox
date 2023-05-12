import sgtk


class GetDropboxProjectNamespace(sgtk.Hook):

    def execute(self, dbx_team_api, **kwargs):
        """
        Return the Dropbox user profile associated with the specified shotgun user email

        This method is using email address to find correct user in the team

        :param sg_user:  Dictionary
                         The shotgun user entity fields

        :returns:        String
                         The Perforce username for the specified Shotgun user
        """
        # If user set's non-standard directory in Dropbox, it must be configured in
        # Framework's settings, alternatively, we refer to the value of `Tank Name`
        # stored in Shotgrid
        sg_project_name = kwargs.get("app_home")
        if not sg_project_name:
            # Accessing protected member to get project name instead of contacting
            # Shotgrid's database.
            sg_project_name = self.sgtk.pipeline_configuration._project_name
        for namespace in dbx_team_api.team_namespaces_list().namespaces:
            if namespace.name == sg_project_name:
                return namespace
