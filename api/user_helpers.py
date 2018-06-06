class UserHelpers:
    @staticmethod
    def get_user_role(user):
        """
        Get user's role (ADM - Admin, CON - Consumer).
        :param user: user instance.
        :return: user's role.
        """
        if user.is_staff:
            return 'ADM'
        else:
            return 'CON'
