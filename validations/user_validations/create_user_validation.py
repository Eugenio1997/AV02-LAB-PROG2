import re
from user.requirements.user_signup_requirements import UserSignupRequirements


class UserValidations:

    def __init__(self):
        pass

    def __validate_signup_info(self, input_value, pattern, requirements_message):
        while True:
            if re.match(pattern, input_value):
                return input_value
            else:
                print(requirements_message)
                input_value = input(f"\nDigite o valor novamente: ")

    def validate_name(self, name):
        name_pattern = r'^[a-zA-Z]{3,20}(?: [a-zA-Z]{3,20})*$'
        requirements_message = UserSignupRequirements.name_requirements
        return self.__validate_signup_info(name, name_pattern, requirements_message)

    def validate_email(self, email):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        requirements_message = UserSignupRequirements.email_requirements
        return self.__validate_signup_info(email, email_pattern, requirements_message)

    def validate_phone_number(self, phone_number):
        phone_number_pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
        requirements_message = UserSignupRequirements.phone_number_requirements
        return self.__validate_signup_info(phone_number, phone_number_pattern, requirements_message)

    def validate_password(self, password):
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!\"§$%&/()=?+\*\#\'^°,\;.:<>äöüÄÖÜß?|@~´`\\])[A-Za-z\d!\"§$%&/()=?+\*\#\'^°,\;.:<>äöüÄÖÜß?|@~´`\\]{8,}$'
        requirements_message = UserSignupRequirements.password_requirements
        return self.__validate_signup_info(password, password_pattern, requirements_message)


