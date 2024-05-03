from user.user_session import UserSession


class UserInterface:
    @staticmethod
    def display(authenticated: bool, product_list: list[dict[str, float]]):
        if not authenticated:
            print("O que deseja?\n")
            print("Cadastrar-se (1)\nAutenticar-se (2)\nParar execução do programa (3)\n")
        else:
            print(f'Bem-vindo {UserSession.get_authenticated_user_email()}! Você está autenticado.')
            print("Deseja adicionar um novo produto? (4)")
            print("Deseja listar todos os produtos? (5)")
            if len(product_list) > 0:
                print("Deseja deletar algum produto? (6)")
            if len(product_list) > 0:
                print("Deseja editar algum produto? (7)")
            print("Deslogar-se (8)\n")
