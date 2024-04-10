from enums import menu_options
from user.user import User
from user.authentication import Authentication
from product.product import Product


class Menu:
    def __init__(self):
        self.authenticated = False
        self.product_manager = Product()
        self.user_manager = User()
        self.auth_manager = Authentication()

    def display(self):
        if not self.authenticated:
            print("O que deseja?\n")
            print("Cadastrar-se (1)\nAutenticar-se (2)\nSair (3)\n")
        else:
            print(f'Bem-vindo! Você está autenticado.')
            print("Deseja adicionar um novo produto? (4)")
            print("Deseja listar todos os produtos existentes? (5)")
            print("Sair (3)\n")

    def handle_option(self, option: str):
        if not self.authenticated:
            if option == menu_options.Options.CADASTRAR_SE.value:
                user_data = self.user_manager.get_user_signup_info()
                if user_data is not None:
                    name, phone_number, email, password = user_data
                    self.user_manager.save(name, phone_number, email, password)
                else:
                    print("Os dados de cadastro do usuário não são válidos.")
            elif option == menu_options.Options.AUTENTICAR_SE.value:
                email, password = self.auth_manager.get_user_signin_info()
                authenticated = Authentication.authenticate_user(email, password)
                if authenticated:
                    self.authenticated = True
                    print("---------- Autenticação bem-sucedida! ----------")
                    print("\n---------- Tela de início do sistema ---------- \n")
            elif option == menu_options.Options.SAIR.value:
                print("Agradecemos por usar o nosso sistema.")
                return False
            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------.\n")
        else:
            if option == menu_options.Options.ADICIONAR_NOVO_PRODUTO.value:
                product_data = self.product_manager.get_product_signup_info()
                if product_data is not None:
                    name, price = product_data
                    Product.add_to_inventory(name, price)
                else:
                    print("Os dados de cadastro do produto não são válidos.")
            elif option == menu_options.Options.LISTAR_PRODUTOS_EXISTENTES.value:
                print(f'Os produtos existentes são: {Product.get_list()}\n')

            elif option == menu_options.Options.SAIR.value:
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
