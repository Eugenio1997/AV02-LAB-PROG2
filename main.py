from enum import Enum

from product import product
from user.authentication import Authentication
from user.user import User


class MenuOption(Enum):
    CADASTRAR_SE = 1
    AUTENTICAR_SE = 2
    SAIR = 3
    ADICIONAR_NOVO_PRODUTO = 4
    LISTAR_PRODUTOS_EXISTENTES = 5


class Menu:
    def __init__(self):
        self.authenticated = False  # Variável para controlar se o usuário está autenticado

    def display(self):
        if not self.authenticated:  # Verifica se o usuário não está autenticado
            print("O que deseja?\n")
            print("Cadastrar-se (1)\nAutenticar-se (2)\nSair (3)\n")
        else:
            print(f'Bem-vindo! Você está autenticado.')
            print("Deseja adicionar um novo produto? (4)")
            print("Deseja listar todos os produtos existentes? (5)")
            print("Sair (0)\n")

    def handle_option(self, option):
        if not self.authenticated:
            if option == MenuOption.CADASTRAR_SE.value:
                name, phone_number, email, password = User.get_signup_data()
                User.save(name, phone_number, email, password)

            elif option == MenuOption.AUTENTICAR_SE.value:
                email, password = Authentication.get_data()
                authenticated = Authentication.authenticate_user(email, password)
                if authenticated:
                    self.authenticated = True  # Define a variável como True após a autenticação bem-sucedida
                    print("---------- Autenticação bem-sucedida! ----------")
                    print("\n---------- Tela de início do sistema ---------- \n")

            elif option == MenuOption.SAIR.value:
                print("Agradecemos por usar o nosso sistema.")
                return False

        else:  # Se o usuário estiver autenticado
            if option == MenuOption.ADICIONAR_NOVO_PRODUTO.value:
                name, preco = product.Product.get_data()
                product.Product.add_to_inventory(name=name, preco=preco)
            elif option == MenuOption.LISTAR_PRODUTOS_EXISTENTES.value:
                print(f'Os produtos existentes são: {product.Product.get_list()}\n')
            elif option == 0:  # Opção 0 para sair
                print("Agradecemos por usar o nosso sistema.")
                return False

        return True


class App:
    def __init__(self):
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.display()
            option = int(input("Digite a sua opção aqui: "))
            should_continue = self.menu.handle_option(option)
            if not should_continue:
                break


if __name__ == "__main__":
    app = App()
    app.run()
