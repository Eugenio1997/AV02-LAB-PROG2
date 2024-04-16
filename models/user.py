class User:
    """Classe que representa um usuário."""

    def __init__(self, name: str, email: str, phone_number: str, password: str):
        """
        Inicializa um objeto User.

        Args:
            name (str): O nome do usuário.
            email (str): O endereço de email do usuário.
            phone_number (str): O número de telefone do usuário.
            password (str): A senha do usuário.
        """
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__password = password

    def to_dict(self) -> dict:
        """
        Converte o objeto User para um dicionário.

        Returns:
            dict: Um dicionário contendo as informações do usuário.
        """
        return dict(name=self.name, email=self.email, phone_number=self.phone_number, password=self.password)

    @property
    def name(self) -> str:
        """
        Obtém o nome do usuário.

        Returns:
            str: O nome do usuário.
        """
        return self.__name

    @property
    def email(self) -> str:
        """
        Obtém o endereço de email do usuário.

        Returns:
            str: O endereço de email do usuário.
        """
        return self.__email

    @property
    def phone_number(self) -> str:
        """
        Obtém o número de telefone do usuário.

        Returns:
            str: O número de telefone do usuário.
        """
        return self.__phone_number

    @property
    def password(self) -> str:
        """
        Obtém a senha do usuário.

        Returns:
            str: A senha do usuário.
        """
        return self.__password