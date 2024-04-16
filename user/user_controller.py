from validations.user_validations.create_user_validation import UserValidations
from user.requirements.user_signup_requirements import UserSignupRequirements


class UserController:
    __user_list = []  # Lista para armazenar os usuários

    def __init__(self):
        self.user_validations_manager = UserValidations()

    def get_user_signup_info(self) -> tuple[str, str, str, str]:
        # Solicita os dados de cadastro ao usuário
        print("---------- Realizando Cadastro ----------")
        name: str = input(f'{UserSignupRequirements.name_requirements}\nDigite seu nome: ')
        email: str = input(f'{UserSignupRequirements.email_requirements}\nDigite seu email: ')
        phone_number: str = input(
            f'{UserSignupRequirements.phone_number_requirements}\nDigite seu número de telefone: ')
        password: str = input(f'{UserSignupRequirements.password_requirements}\nDigite sua senha: ')

        email, password = self.__remove_whitespaces(email, password)

        name_validated: str = self.user_validations_manager.validate_name(name)
        phone_number_validated: str = self.user_validations_manager.validate_phone_number(phone_number)
        email_validated: str = self.user_validations_manager.validate_email(email)
        password_validated: str = self.user_validations_manager.validate_password(password)

        while not [name_validated, phone_number_validated, email_validated, password_validated]:
            print("\n---------------- Os campos são obrigatórios ----------------\n")
            name_validated, phone_number_validated, email_validated, password_validated = self.get_user_signup_info()

        # return validated_user_data
        return name_validated, phone_number_validated, email_validated, password_validated

    @classmethod
    def save(cls, user_dict: dict[str, str]) -> None:
        if isinstance(user_dict,
                      dict) and "name" in user_dict and "phone_number" in user_dict and "email" in user_dict and "password" in user_dict:
            cls.__user_list.append(
                dict(name=user_dict["name"], phone_number=user_dict["phone_number"], email=user_dict["email"],
                     password=user_dict["password"]))
            print("--------------- Cadastro realizado com sucesso. ---------------\n")
        else:
            raise ValueError("O dicionário fornecido não contém as chaves 'name', 'phone_number', 'email' e 'password'")

    @classmethod
    def get_user_list(cls):
        return cls.__user_list

    def __remove_whitespaces(self, email: str, password: str) -> tuple[
        str, str]:

        email = email.replace(" ", "")
        password = password.replace(" ", "")

        return email, password
