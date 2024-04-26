# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

from validations.user_validations.create_user_validation import UserValidations
from user.requirements.user_signup_requirements import UserSignupRequirements


class UserController:
    """Classe para gerenciamento de usuários."""

    __user_list = []  # Lista para armazenar os usuários

    def __init__(self):
        """Inicializa o UserController."""
        self.user_validations_manager = UserValidations()

    def get_user_signup_info(self) -> tuple[str, str, str, str]:
        """Obtém as informações de cadastro do usuário.

        Retorna:
            tuple[str, str, str, str]: Uma tupla contendo as informações validadas do usuário.
        """
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

        return name_validated, email_validated, phone_number_validated, password_validated

    @classmethod
    def save(cls, user_dict: dict[str, str]) -> bool:
        """Salva as informações do usuário.

        Args:
            user_dict (dict[str, str]): Dicionário contendo as informações do usuário.

        Raises:
            ValueError: Se o dicionário não contiver as chaves necessárias.

        """
        if not any([cls.email_exists(user_dict["email"])]):
            if isinstance(user_dict,
                          dict) and "name" in user_dict and "phone_number" in user_dict and "email" in user_dict and "password" in user_dict:
                cls.__user_list.append(
                    dict(name=user_dict["name"], phone_number=user_dict["phone_number"], email=user_dict["email"],
                         password=user_dict["password"]))
                return True
            else:
                raise ValueError("O dicionário fornecido não contém as chaves 'name', 'phone_number', 'email' e "
                                 "'password'")

        return False

    @classmethod
    def get_user_list(cls):
        """Obtém a lista de usuários cadastrados.

        Returns:
            list[dict[str, str]]: Uma lista de dicionários contendo informações dos usuários.
        """
        return cls.__user_list

    def __remove_whitespaces(self, email: str, password: str) -> tuple[
        str, str]:
        """Remove espaços em branco de strings.

        Args:
            email (str): O email a ser processado.
            password (str): A senha a ser processada.

        Returns:
            tuple[str, str]: Uma tupla contendo as strings processadas.

        """
        email = email.replace(" ", "")
        password = password.replace(" ", "")

        return email, password

    @classmethod
    def email_exists(cls, email: str) -> bool:
        user_list = cls.get_user_list()
        return any(user for user in user_list if user["email"] == email)
