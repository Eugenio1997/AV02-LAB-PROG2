class User:
    users = []  # Lista para armazenar os usuários

    def __init__(self, name, phone_number, email, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    @staticmethod
    def get_signup_data():
        # Solicita os dados de cadastro ao usuário
        print("---------- Realizando Cadastro ----------")
        name = input("Digite seu nome: ")
        phone_number = input("Digite seu número de telefone: ")
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")

        return name, phone_number, email, password

    @staticmethod
    def save(name, phone_number, email, password):
        user = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "password": password
        }
        User.users.append(user)
        print("--------------- Cadastro realizado com sucesso. ---------------\n")

    @staticmethod
    def get_list():
        return User.users
