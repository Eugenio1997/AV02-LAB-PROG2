from user.user import User


class Authentication:
    @staticmethod
    def authenticate_user(email, password):
        users = User.get_list()
        for user in users:
            if user['email'] == email and user['password'] == password:
                return True

        return False

    @staticmethod
    def get_user_signin_info():
        print("---------- Realizando Autenticação ----------")
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")

        is_valid: bool = Authentication.validate_user_signin_info(email, password)

        if is_valid:
            return email, password

    @staticmethod
    def validate_user_signin_info(email: str, password: str) -> bool:

        if Authentication.is_empty_signin_data(email, password):
            print(f'\n---------------- Não podem conter campos em branco ----------------\n')
            Authentication.get_user_signin_info()
        else:
            return True  # A entrada não está em branco



    @staticmethod
    def is_empty_signin_data(email: str, password: str) -> bool:
        return (email.strip() == "" or
                password.strip() == "")