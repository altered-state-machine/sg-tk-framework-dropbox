import sgtk


class GetDropboxUserProfile(sgtk.Hook):

    def execute(self, dbx_team_api, sg_user, **kwargs):
        """
        Return the Dropbox user profile associated with the specified shotgun user email

        This method is using email address to find correct user in the team

        :param sg_user:  Dictionary
                         The shotgun user entity fields

        :returns:        String
                         The Perforce username for the specified Shotgun user
        """

        for member in dbx_team_api.team_members_list().members:
            profile = member.profile
            if profile.email == sg_user['email']:
                return profile
