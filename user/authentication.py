# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

from user.user_controller import UserController


class Authentication:
    """
    Classe responsável pela autenticação de usuários.

    Attributes:
        user_manager (UserController): Instância do UserController para gerenciamento de usuários.
    """

    def __init__(self):
        """
        Inicializa a classe Authentication.
        """
        self.user_manager = UserController()

    def authenticate_user(self, email: str, password: str):

        user_list = self.user_manager.get_user_list()

        for user in user_list:
            if user.get('email') == email and user.get('password') == password:
                return True
        return False

    def get_user_signin_info(self) -> tuple[str, str]:
        """
        Solicita e retorna as informações de login do usuário.

        Returns:
            tuple[str, str] | None: Uma tupla contendo o email e a senha do usuário ou None se houver campos em branco.
        """
        print("---------- Realizando Autenticação ----------")
        email = input("Digite seu email: ")
        password = input("Digite sua senha: ")

        if self.is_empty_signin_data(email, password):
            print(f'\n---------------- Não podem conter campos em branco ----------------\n')

        return email, password

    def is_empty_signin_data(self, email: str, password: str) -> bool:
        """
        Verifica se o email e a senha estão em branco.

        Args:
            email (str): O email a ser verificado.
            password (str): A senha a ser verificada.

        Returns:
            bool: True se ambos estiverem em branco, False caso contrário.
        """
        return not any([email, password])
