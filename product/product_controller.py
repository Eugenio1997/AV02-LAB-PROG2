# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos
from typing import Any, List

from models.user import User
from user.user_session import UserSession
from validations.product_validations.create_product_validation import ProductValidations
from product.requirements.product_signup_requirements import ProductSignupRequirements


class ProductController:
    """
    Classe responsável por controlar a gestão de produtos no sistema.

    Attributes:
        __product_dict (dict): Dicionário para armazenar os produtos cadastrados.
    """
    __CONFIRMATION_YES = 'sim'
    __product_dict: dict[str, List[Any]] = {}  # Dicionário para armazenar os produtos

    def __init__(self):
        """
        Inicializa o ProductController com um gerenciador de validações de produto.
        """
        self.product_validations_manager = ProductValidations()

    @classmethod
    def add_to_inventory(cls, product_dict: dict[str, float], authenticated_user_email: str) -> bool:
        """
        Adiciona um produto ao inventário.

        Args:
            authenticated_user_email (str): O email do usuário, atualmente, autenticado.
            product_dict (dict): Dicionário contendo as informações do produto, com as chaves 'name' e 'price'.

        Raises:
            ValueError: Se o dicionário fornecido não contém as chaves 'name' e 'price'.
        """
        if isinstance(product_dict, dict) and "name" in product_dict and "price" in product_dict:
            # procurar a lista correspondente ao usuário logado
            product_list_from_authenticated_user = cls.get_product_list_from_user(authenticated_user_email)
            product_list_from_authenticated_user.append(product_dict)
            cls.update_product_list_from_authenticated_user(product_list_from_authenticated_user)

            return True
        else:
            raise ValueError("O dicionário fornecido não contém as chaves 'name' e 'price'.")

    def get_product_signup_info(self) -> tuple[str, str] or tuple[None, None]:
        """
        Solicita e valida as informações de cadastro de um produto.

        Returns:
            tuple[str, str]: Uma tupla contendo o nome e o preço do produto validados.
        """
        print("---------- Realizando Cadastro de Produto ----------")

        name = input(f'{ProductSignupRequirements.name_requirements}\nDigite o nome: ')
        name_validated = self.product_validations_manager.validate_name(name)

        price = input(f'{ProductSignupRequirements.price_requirements}\nDigite o preço: ')
        price = self.__remove_whitespaces(price)
        price_validated = self.product_validations_manager.validate_price(price)

        return name_validated, price_validated

    @classmethod
    def get_product_list_from_user(cls, user_email) -> list[dict[str, float]]:
        """

        Args:
            user_email: user's email authenticated or registered.
        Returns:
            product_list: A lista de produtos de um usuário com base em seu e-mail como chave do dicionario denominado cls.__product_dict
        """
        if user_email in cls.__product_dict:
            product_list = cls.__product_dict[user_email]
            return product_list
        elif not any([user_email]):
            return []
        else:
            raise ValueError(f"Nenhuma lista encontrada para o email: {user_email}")

    @classmethod
    def create_product_list_for_registered_user(cls, registered_user_email: str) -> None:
        """
            Cria uma lista para cada usuário cadastrado baseado no email dele.

        Args:
            registered_user_email: O email do usuário no momento de seu cadastro.

        Returns:
            None
        """

        if registered_user_email in cls.__product_dict:
            return

        cls.__product_dict[registered_user_email] = []

    @classmethod
    def update_product_list_from_authenticated_user(cls, new_product_list: list[dict[str, float]]) -> None:
        """
            Atualiza, com uma nova lista de produtos, a lista do usuário autenticado.
        Args:
            new_product_list (list[dict[str, float]]): A nova lista, atualizada, de produtos do usuário autenticado.
        Returns:
            None
        """
        authenticated_user_email: str = UserSession.get_authenticated_user_email()
        cls.__product_dict[authenticated_user_email] = new_product_list

    def __remove_whitespaces(self, price: str) -> str:
        """
        Remove espaços em branco de uma string.

        Args:
            price (str): O preço a ser processado.

        Returns:
            str: O preço sem espaços em branco.
        """
        return price.replace(" ", "")

    def confirm_delete(self) -> None:
        """
        Solicita ao usuário o nome do produto a ser deletado e confirma a exclusão.

        Retorna:
            None
        """
        product_name = input("Informe o nome do produto que deseja deletar: ")
        if self.product_validations_manager.is_empty_product_name(product_name):
            return

        confirm_delete: str = input(f'Tem certeza de que deseja excluir o {product_name}? (Sim/Nao): ')
        self.__delete_product(product_name.lower(), confirm_delete.lower())

    def __delete_product(self, product_name: str, confirm_delete: str) -> None:
        """
        Exclui um produto da lista de produtos.

        Parâmetros:
            product_name (str): Nome do produto a ser excluído.
            confirm_delete (str): Confirmação da exclusão (Sim/Não).

        Retorna:
            None
        """
        product_list = self.get_product_list_from_user(UserSession.get_authenticated_user_email())
        if any(str(product_dict['name']).lower() == product_name for product_dict in product_list):
            if confirm_delete == self.__CONFIRMATION_YES:

                deleted_product = next(
                    (product_dict for product_dict in product_list if
                     str(product_dict['name']).lower() == product_name), None)
                if deleted_product is not None:
                    product_list.remove(deleted_product)

                self.update_product_list_from_authenticated_user(product_list)
                print(f"\n---- Produto '{product_name}' deletado com sucesso. \n----")
            else:
                print(f"\n----- A exclusão do produto '{product_name}' foi cancelada. -----\n")
        else:
            print(f"\n----- Produto não encontrado. -----\n")

    def confirm_edit(self):
        product_name = input("Informe o nome do produto que deseja editar: ")
        if self.product_validations_manager.is_empty_product_name(product_name):
            return

        confirm_edit: str = input(f"Tem certeza de que deseja editar o '{product_name}'? (Sim/Nao): ")
        self.__edit_product(product_name.lower(), confirm_edit.lower())

    def __edit_product(self, product_name: str, confirm_delete: str):
        product_list = self.get_product_list_from_user(UserSession.get_authenticated_user_email())
        if any(str(product_dict["name"]).lower() == product_name for product_dict in product_list):
            if confirm_delete == self.__CONFIRMATION_YES:
                for product_dict in product_list:
                    if str(product_dict["name"]).lower() == product_name:
                        name: str = input(f"Informe o novo nome do produto '{product_name}': ")
                        price: str = input(f"Informe o novo preço do produto\n '{product_name}': ")
                        if (name is None or name == '') and (price is None or price == ''):
                            print(f"\n---- Produto '{product_name}' editado com sucesso. \n----")
                            return
                        elif (name is None or name == '') and (price is not None or price != ''):
                            product_dict['price'] = self.product_validations_manager.validate_price(price)
                        elif (name is not None or name != '') and (price is None or price == ''):
                            product_dict['name'] = self.product_validations_manager.validate_name(name)
                        else:
                            product_dict['name'] = self.product_validations_manager.validate_name(name)
                            product_dict['price'] = self.product_validations_manager.validate_price(price)

                self.update_product_list_from_authenticated_user(product_list)
                print(f"\n---- Produto '{product_name}' editado com sucesso. \n----")

            else:
                print(f"\n----- A edição do produto {product_name} foi cancelada. -----\n")
        else:
            print(f"\n----- Produto não encontrado. -----\n")
