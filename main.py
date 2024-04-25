# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos
import time

from enums.add_new_product_messages import AddNewProductMessages
from enums.auth_messages import AuthMessages
from enums.menu_options import Options
from enums.user_signup_messages import UserSignupMessages
from models.user import User
from user.user_controller import UserController
from user.authentication import Authentication
from product.product_controller import ProductController
from models.product import Product
from validations.auth_validations.authenticate_user_validation import AuthenticateUserValidations


class Menu:
    MAX_RETRIES = 3
    retry_count = 0
    email: str
    password: str
    user_exists: bool
    counter: int = 3

    def __init__(self):
        self.authenticated = False
        self.product_manager = ProductController()
        self.user_manager = UserController()
        self.auth_manager = Authentication()
        self.auth_validations_manager = AuthenticateUserValidations()

    def display(self):
        product_list = self.product_manager.get_product_list()
        if not self.authenticated:
            print("O que deseja?\n")
            print("Cadastrar-se (1)\nAutenticar-se (2)\nParar execução do programa (3)\n")
        else:
            print(f'Bem-vindo! Você está autenticado.')
            print("Deseja adicionar um novo produto? (4)")
            print("Deseja listar todos os produtos? (5)")
            if len(product_list) > 0:
                print("Deseja deletar algum produto? (6)")
            if len(product_list) > 0:
                print("Deseja editar algum produto? (7)")
            print("Deslogar-se (8)\n")

    def handle_option(self, option: str):
        user_saved: bool = False
        if not self.authenticated:
            if option == Options.REGISTER.value:

                while self.retry_count < self.MAX_RETRIES:

                    self.counter -= 1
                    self.retry_count += 1

                    user_signup_data = self.user_manager.get_user_signup_info()
                    name, email, phone_number, password = user_signup_data
                    new_user = User(name, email, phone_number, password)
                    user_dict = new_user.to_dict()
                    if all([name, email, phone_number, password]):
                        user_saved = self.user_manager.save(user_dict)
                        if user_saved:
                            print(f"\n{UserSignupMessages.SUCCESS.value}\n")
                            break
                        else:
                            print(f"\n{UserSignupMessages.EMAIL_IN_USE.value}\n")
                            if self.counter >= 1:
                                print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")
                    elif not any([name, email, phone_number, password]):
                        print(f"\n{UserSignupMessages.BLANK_FIELDS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")
                    else:
                        print(f"\n{UserSignupMessages.INVALID_CREDENTIALS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")

                if self.retry_count == self.MAX_RETRIES:
                    if not user_saved:
                        print(f"{UserSignupMessages.MAX_RETRIES.value}\n")
                    if self.retry_count == 3 and self.counter == 0:
                        self.retry_count = 0
                        self.counter = 3
                    time.sleep(0.5)

            elif option == Options.AUTHENTICATE.value:

                while self.retry_count < self.MAX_RETRIES:

                    self.counter -= 1
                    self.retry_count += 1
                    self.email, self.password = self.auth_manager.get_user_signin_info()
                    self.user_exists: bool = self.auth_validations_manager.validate_user_existence(self.email)
                    if self.user_exists:
                        authenticated = self.auth_manager.authenticate_user(self.email, self.password)
                        if authenticated:
                            self.authenticated = True
                            print(f"\n{AuthMessages.SUCCESS.value}\n")
                            print("\n---------- Tela de início do sistema ---------- \n")
                            break
                        else:
                            print(f"\n{AuthMessages.INVALID_CREDENTIALS.value}\n")
                            if self.counter >= 1:
                                print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")
                    elif not any([self.email, self.password]):
                        print(f"\n{AuthMessages.BLANK_FIELDS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")
                    else:
                        print(f"\n{AuthMessages.INVALID_CREDENTIALS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")

                if self.retry_count == self.MAX_RETRIES:
                    if not self.authenticated:
                        print(f"{AuthMessages.MAX_RETRIES.value}\n")
                    if self.retry_count == 3 and self.counter == 0:
                        self.retry_count = 0
                        self.counter = 3
                    time.sleep(0.5)


            elif option == Options.EXIT.value:
                print("\n---------------- Agradecemos por usar o nosso sistema. ----------------\n")
                return False
            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------\n")
        else:

            if option == Options.ADD_NEW_PRODUCT.value:
                self.counter = 3
                self.retry_count = 0
                while self.retry_count < self.MAX_RETRIES:

                    self.counter -= 1
                    self.retry_count += 1
                    name_validated, price_validated = self.product_manager.get_product_signup_info()

                    if all([name_validated, price_validated]):

                        new_product = Product(name_validated, price_validated)
                        product_saved = self.product_manager.add_to_inventory(new_product.to_dict())
                        if product_saved:
                            print(f"\n{AddNewProductMessages.SUCCESS.value}\n")
                            break
                    elif not any([name_validated, price_validated]):
                        print(f"\n{AddNewProductMessages.BLANK_FIELDS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")

                    else:
                        print(f"\n{AddNewProductMessages.INVALID_VALUES.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")

                    if self.retry_count == self.MAX_RETRIES:
                        print(f"{AddNewProductMessages.MAX_RETRIES.value}\n")
                        if self.retry_count == 3 and self.counter == 0:
                            self.retry_count = 0
                            self.counter = 3
                        time.sleep(0.5)

            elif option == Options.LIST_PRODUCTS.value:
                print(f'Os produtos cadastrados são: {self.product_manager.get_product_list()}\n')

            elif option == Options.DELETE_PRODUCT.value:
                self.product_manager.confirm_delete()

            elif option == Options.EDIT_PRODUCT.value:
                self.product_manager.confirm_edit()
            
            elif option == Options.LOGOUT.value:
                print("\n---------------- Logout realizado com sucesso!. ----------------\n")
                self.authenticated = False


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
