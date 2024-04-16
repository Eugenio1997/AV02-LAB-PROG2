from enums import menu_options
from models.user import User
from user.user_controller import UserController
from user.authentication import Authentication
from product.product_controller import ProductController
from models.product import Product


class Menu:
    def __init__(self):
        self.authenticated = False
        self.product_manager = ProductController()
        self.user_manager = UserController()
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
                user_signup_data = self.user_manager.get_user_signup_info()
                if user_signup_data is not None:
                    name, email, phone_number, password = user_signup_data
                    new_user = User(name, email, phone_number, password)
                    user_dict = new_user.to_dict()
                    self.user_manager.save(user_dict)
                else:
                    print("\n---------------- Os dados de cadastro do usuário não são válidos ----------------\n")

            elif option == menu_options.Options.AUTENTICAR_SE.value:
                user_signin_data = self.auth_manager.get_user_signin_info()
                if user_signin_data is not None:
                    email, password = user_signin_data
                    authenticated = self.auth_manager.authenticate_user(email, password)
                    if authenticated:
                        self.authenticated = True
                        print("---------- Autenticação bem-sucedida! ----------")
                        print("\n---------- Tela de início do sistema ---------- \n")
            elif option == menu_options.Options.SAIR.value:
                print("Agradecemos por usar o nosso sistema.")
                return False
            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------\n")
        else:
            if option == menu_options.Options.ADICIONAR_NOVO_PRODUTO.value:
                product_data = self.product_manager.get_product_signup_info()
                if product_data is not None:
                    name, price = product_data
                    new_product = Product(name, price)
                    self.product_manager.add_to_inventory(new_product.to_dict())
                else:
                    raise ValueError("NULL não é permitido para 'preço'.")
            elif option == menu_options.Options.LISTAR_PRODUTOS_EXISTENTES.value:
                print(f'Os produtos existentes são: {self.product_manager.get_product_list()}\n')

            elif option == menu_options.Options.SAIR.value:
                print("Agradecemos por usar o nosso sistema.")
                return False

            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------\n")
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
