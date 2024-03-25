from user.user import User


class Authentication:
    @staticmethod
    def authenticate_user(email, password):
        users = User.get_list()  # Chamada correta para método estático
        for user in users:
            if user['email'] == email and user['password'] == password:
                return True

        return False

    @staticmethod
    def get_data():
        print("---------- Realizando Autenticação ----------")
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")

        return email, password