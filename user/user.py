class User:
    __user_list = []  # Lista para armazenar os usuários

    def __init__(self):
        pass

    def get_user_signup_info(self):
        # Solicita os dados de cadastro ao usuário
        print("---------- Realizando Cadastro ----------")
        name: str = input("Digite seu nome: ")
        phone_number: str = input("Digite seu número de telefone: ")
        email: str = input("Digite seu email: ")
        password: str = input("Digite sua senha: ")

        is_valid: bool = self.validate_user_signup_info(name, phone_number, email, password)

        if is_valid:
            return name, phone_number, email, password
        else:
            return None

    def validate_user_signup_info(self, name: str, phone_number: str, email: str, password: str) -> bool:

        if self.is_empty(name, phone_number, email, password):
            print(f'\nNão podem conter campos em branco')
            self.get_user_signup_info()
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
        User.__user_list.append(user)
        print("--------------- Cadastro realizado com sucesso. ---------------\n")

    @staticmethod
    def get_list():
        return User.__user_list

    def is_empty(self, name: str, phone_number: str, email: str, password: str) -> bool:
        return (name.strip() == "" or
                phone_number.strip() == "" or
                email.strip() == "" or
                password.strip() == "")
