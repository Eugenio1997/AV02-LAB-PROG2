from enums import menu_options
from product import product
from user.authentication import Authentication
from user.user import User


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

    def handle_option(self, option: str):
        if not self.authenticated:

            if option == menu_options.Options.CADASTRAR_SE.value:
                user_data = User.get_user_signup_info()
                if user_data is not None:
                    name, phone_number, email, password = user_data
                    User.save(name, phone_number, email, password)
                else:
                    print("Os dados de cadastro do usuário não são válidos.")

            elif option == menu_options.Options.AUTENTICAR_SE.value:
                email, password = Authentication.get_user_signin_info()
                authenticated = Authentication.authenticate_user(email, password)
                if authenticated:
                    self.authenticated = True  # Define a variável como True após a autenticação bem-sucedida
                    print("---------- Autenticação bem-sucedida! ----------")
                    print("\n---------- Tela de início do sistema ---------- \n")

            elif option == menu_options.Options.SAIR.value:
                print("Agradecemos por usar o nosso sistema.")
                return False

            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------.\n")



        else:  # Se o usuário estiver autenticado

            if option == menu_options.Options.ADICIONAR_NOVO_PRODUTO.value:
                product_data = product.Product.get_product_signup_info()
                if product_data is not None:
                    name, price = product_data
                    new_product = product.Product(name=name, price=price)
                    product.Product.add_to_inventory(new_product.name, new_product.price)
                else:
                    print("Os dados de cadastro do produto não são válidos.")
            elif option == menu_options.Options.LISTAR_PRODUTOS_EXISTENTES.value:
                print(f'Os produtos existentes são: {product.Product.get_list()}\n')

            elif option == 0:  # Opção 0 para sair
                print("Agradecemos por usar o nosso sistema.")
                return False

            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------.\n")

        return True


class App:
    def __init__(self):
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.display()
            option = input("Digite a sua opção aqui: ")
            should_continue = self.menu.handle_option(option)
            if not should_continue:
                break


if __name__ == "__main__":
    app = App()
    app.run()
