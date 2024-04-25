from user.user_controller import UserController


class AuthenticateUserValidations:

    def __init__(self):
        self.user_manager = UserController()

    def validate_user_existence(self, email: str):

        user_list = self.user_manager.get_user_list()

        for user in user_list:
            if user.get('email') == email:
                return True
        return False

