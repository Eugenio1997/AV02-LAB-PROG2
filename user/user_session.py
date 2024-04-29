# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

class UserSession:
    """
    Esta classe faz o gerenciamento e fornecimento dos dados do usuário cadastrado ou autenticado
    """

    email: str = ''
    password: str = ''
    name: str = ''
    phone_number: str = ''

    @staticmethod
    def set_registered_user(email: str, password: str, name: str, phone_number: str) -> None:
        UserSession.email = email
        UserSession.password = password
        UserSession.name = name
        UserSession.phone_number = phone_number

    @staticmethod
    def set_authenticated_user(email: str, password: str) -> None:
        UserSession.email = email
        UserSession.password = password

    @staticmethod
    def get_registered_user() -> tuple[str, str, str, str]:
        return UserSession.email, UserSession.password, UserSession.name, UserSession.phone_number

    @staticmethod
    def get_registered_user_email() -> str:
        return UserSession.email

    @staticmethod
    def get_authenticated_user_email() -> str:
        return UserSession.email

    @staticmethod
    def get_registered_user_name() -> str:
        return UserSession.name
