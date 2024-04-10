

class User:
    users = []  # Lista para armazenar os usuários

    def __init__(self, name, phone_number, email, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    @staticmethod
    def get_user_signup_info():
        # Solicita os dados de cadastro ao usuário
        print("---------- Realizando Cadastro ----------")
        name: str = input("Digite seu nome: ")
        phone_number: str = input("Digite seu número de telefone: ")
        email: str = input("Digite seu email: ")
        password: str = input("Digite sua senha: ")

        is_valid: bool = User.validate_user_signup_info(name, phone_number, email, password)

        if is_valid:
            return name, phone_number, email, password
        else:
            return None

    @staticmethod
    def validate_user_signup_info(name: str, phone_number: str, email: str, password: str) -> bool:

        if User.is_empty(name, phone_number, email, password):
            print(f'\nNão podem conter campos em branco')
            User.get_user_signup_info()
        else:
            return True  # A entrada não está em branco

    @staticmethod
    def save(name, phone_number, email, password) -> None:
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

    @staticmethod
    def is_empty(name: str, phone_number: str, email: str, password: str) -> bool:
        return (name.strip() == "" or
                phone_number.strip() == "" or
                email.strip() == "" or
                password.strip() == "")
