from user.user import User


class Authentication:
    def __init__(self):
        pass

    @staticmethod
    def authenticate_user(email, password):
        user_list = User.get_list()
        for user in user_list:
            if user.get('email') == email and user.get('password') == password:
                return True
        return False

    def get_user_signin_info(self):
        print("---------- Realizando Autenticação ----------")
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")

        if self.is_empty_signin_data(email, password):
            print(f'\n---------------- Não podem conter campos em branco ----------------\n')
            return None

        return email, password

    def is_empty_signin_data(self, email: str, password: str) -> bool:
        return email.strip() == "" or password.strip() == ""
