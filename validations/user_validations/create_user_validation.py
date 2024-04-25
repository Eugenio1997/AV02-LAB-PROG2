# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

import re
from user.requirements.user_signup_requirements import UserSignupRequirements


class UserValidations:
    """Classe para realizar validações de usuário."""

    def __init__(self):
        """Inicializa um objeto UserValidations."""
        pass

    def __validate_signup_info(self, input_value, pattern, requirements_message):

        if re.match(pattern, input_value):
            return input_value


    def validate_name(self, name):
        """
        Valida o nome do usuário.

        Args:
            name (str): O nome do usuário a ser validado.

        Returns:
            str: O nome validado, se válido.
        """
        name_pattern = r'^[a-zA-Z]{3,20}(?: [a-zA-Z]{3,20})*$'
        requirements_message = UserSignupRequirements.name_requirements
        return self.__validate_signup_info(name, name_pattern, requirements_message)

    def validate_email(self, email):
        """
        Valida o email do usuário.

        Args:
            email (str): O email do usuário a ser validado.

        Returns:
            str: O email validado, se válido.
        """
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        requirements_message = UserSignupRequirements.email_requirements
        return self.__validate_signup_info(email, email_pattern, requirements_message)

    def validate_phone_number(self, phone_number):
        """
        Valida o número de telefone do usuário.

        Args:
            phone_number (str): O número de telefone do usuário a ser validado.

        Returns:
            str: O número de telefone validado, se válido.
        """
        phone_number_pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
        requirements_message = UserSignupRequirements.phone_number_requirements
        return self.__validate_signup_info(phone_number, phone_number_pattern, requirements_message)

    def validate_password(self, password):
        """
        Valida a senha do usuário.

        Args:
            password (str): A senha do usuário a ser validada.

        Returns:
            str: A senha validada, se válida.
        """
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!\"§$%&/()=?+\*\#\'^°,\;.:<>äöüÄÖÜß?|@~´`\\])[A-Za-z\d!\"§$%&/()=?+\*\#\'^°,\;.:<>äöüÄÖÜß?|@~´`\\]{8,}$'
        requirements_message = UserSignupRequirements.password_requirements
        return self.__validate_signup_info(password, password_pattern, requirements_message)
