# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos
import time
from typing import Optional

from enums.add_new_product_messages import AddNewProductMessages
from enums.auth_messages import AuthMessages
from enums.menu_options import Options
from enums.user_signup_messages import UserSignupMessages
from interface.user_interface import UserInterface
from models.user import User
from user.user_controller import UserController
from user.authentication import Authentication
from product.product_controller import ProductController
from models.product import Product
from user.user_session import UserSession
from utils import Utils
from validations.auth_validations.authenticate_user_validation import AuthenticateUserValidations


class Menu:
    MAX_RETRIES = 3
    retry_count = 0
    email: str
    password: str
    phone_number: str
    name: str
    user_exists: bool
    counter: int = 3
    product_saved: bool = False

    def __init__(self):
        self.authenticated = False
        self.product_manager = ProductController()
        self.user_manager = UserController()
        self.auth_manager = Authentication()
        self.auth_validations_manager = AuthenticateUserValidations()

    def display(self):
        product_list = self.product_manager.get_product_list_from_user(
            UserSession.get_authenticated_user_email())

        UserInterface.display(self.authenticated, product_list)

    def handle_option(self, option: str):
        user_saved: bool = False
        if not self.authenticated:
            if option == Options.REGISTER.value:

                while self.retry_count < self.MAX_RETRIES:

                    self.counter -= 1
                    self.retry_count += 1

                    user_signup_data = self.user_manager.get_user_signup_info()
                    self.name, self.email, self.phone_number, self.password = user_signup_data
                    UserSession.set_registered_user(self.email, self.password, self.name, self.phone_number)
                    new_user = User(self.name, self.email, self.phone_number, self.password)
                    user_dict = new_user.to_dict()
                    if all([self.name, self.email, self.phone_number, self.password]):
                        user_saved = self.user_manager.save(user_dict)
                        if user_saved:
                            print(f"\n{UserSignupMessages.SUCCESS.value}\n")
                            self.product_manager.create_product_list_for_registered_user(
                                UserSession.get_registered_user_email())
                            break
                        else:
                            print(f"\n{UserSignupMessages.EMAIL_IN_USE.value}\n")
                            if self.counter >= 1:
                                print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")
                    elif not any([self.name, self.email, self.phone_number, self.password]):
                        print(f"\n{UserSignupMessages.BLANK_FIELDS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")
                    else:
                        print(f"\n{UserSignupMessages.INVALID_CREDENTIALS.value}\n")
                        if self.counter >= 1:
                            print(f"---------------- Tentativas restantes - ({self.counter}) ---------------- \n")

                self.retry_count, self.counter = Utils.check_and_reset_retries_count(self.retry_count, self.counter,
                                                                                     self.authenticated, user_saved,
                                                                                     self.product_saved, option)

            elif option == Options.AUTHENTICATE.value:

                while self.retry_count < self.MAX_RETRIES:

                    self.counter -= 1
                    self.retry_count += 1
                    self.email, self.password = self.auth_manager.get_user_signin_info()
                    UserSession.set_authenticated_user(self.email, self.password)
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

                self.retry_count, self.counter = Utils.check_and_reset_retries_count(self.retry_count, self.counter,
                                                                                     self.authenticated, user_saved,
                                                                                     self.product_saved, option)
            elif option == Options.EXIT.value:
                print(
                    f"\n---------------- Agradecemos por usar o nosso sistema, {UserSession.get_authenticated_user_email()}. ----------------\n")
                return False
            else:
                print("\n---------------- Escolha alguma das opções exibidas ----------------\n")
        else:

            if option == Options.ADD_NEW_PRODUCT.value:

                while self.retry_count < self.MAX_RETRIES:

                    self.counter -= 1
                    self.retry_count += 1
                    name_validated, price_validated = self.product_manager.get_product_signup_info()

                    if all([name_validated, price_validated]):

                        new_product = Product(name_validated, price_validated)
                        self.product_saved = self.product_manager.add_to_inventory(new_product.to_dict(),
                                                                                   UserSession.get_authenticated_user_email())
                        if self.product_saved:
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

                self.retry_count, self.counter = Utils.check_and_reset_retries_count(self.retry_count, self.counter,
                                                                                     self.authenticated, user_saved,
                                                                                     self.product_saved, option)

            elif option == Options.LIST_PRODUCTS.value:
                authenticated_user_email = UserSession.get_authenticated_user_email()
                product_table = self.product_manager.get_product_list_from_user_in_tabular_format(
                    authenticated_user_email)
                if product_table is not None:
                    print(f'\n\nOs produtos cadastrados são:\n\n{product_table}\n\n')

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
