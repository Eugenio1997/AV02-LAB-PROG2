# Autor: Eugenio Lopes Fernandes Lima
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

from validations.product_validations.create_product_validation import ProductValidations
from product.requirements.product_signup_requirements import ProductSignupRequirements


class ProductController:
    """
    Classe responsável por controlar a gestão de produtos no sistema.

    Attributes:
        __product_list (list): Lista para armazenar os produtos cadastrados.
    """
    __CONFIRMATION_YES = 'sim'
    __product_list = []  # Lista para armazenar os produtos

    def __init__(self):
        """
        Inicializa o ProductController com um gerenciador de validações de produto.
        """
        self.product_validations_manager = ProductValidations()

    @classmethod
    def add_to_inventory(cls, product_dict) -> None:
        """
        Adiciona um produto ao inventário.

        Args:
            product_dict (dict): Dicionário contendo as informações do produto, com as chaves 'name' e 'price'.

        Raises:
            ValueError: Se o dicionário fornecido não contém as chaves 'name' e 'price'.
        """
        if isinstance(product_dict, dict) and "name" in product_dict and "price" in product_dict:
            cls.__product_list.append({"name": product_dict["name"], "price": product_dict["price"]})
            print("--------------- Cadastro realizado com sucesso. ---------------\n")
        else:
            raise ValueError("O dicionário fornecido não contém as chaves 'name' e 'price'.")

    def get_product_signup_info(self) -> tuple[str, str]:
        """
        Solicita e valida as informações de cadastro de um produto.

        Returns:
            tuple[str, str]: Uma tupla contendo o nome e o preço do produto validados.
        """
        print("---------- Realizando Cadastro de Produto ----------")

        name: str = input(f'{ProductSignupRequirements.name_requirements}\nDigite o nome: ')
        price: str = input(f'{ProductSignupRequirements.price_requirements}\nDigite o preço: ')

        name, price = self.__remove_whitespaces(name, price)

        name_validated: str = self.product_validations_manager.validate_name(name)
        price_validated: str = self.product_validations_manager.validate_price(price)

        while not (name_validated and price_validated):
            print("\n---------------- Os campos são obrigatórios ----------------\n")
            name, price = self.get_product_signup_info()
            name_validated = self.product_validations_manager.validate_name(name)
            price_validated = self.product_validations_manager.validate_price(price)

        return name_validated, price_validated

    @classmethod
    def get_product_list(cls) -> list[dict[str, float]]:
        """
        Retorna a lista de produtos cadastrados.

        Returns:
            list[dict[str, float]]: Lista de produtos cadastrados.
        """
        return cls.__product_list

    @classmethod
    def update_product_list(cls, new_product_list) -> None:
        cls.__product_list = new_product_list

    def __remove_whitespaces(price: str) -> str:
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
        product_list = self.get_product_list()
        if any(str(product['name']).lower() == product_name for product in product_list):
            if confirm_delete == self.__CONFIRMATION_YES:

                deleted_product = next(
                    (product for product in product_list if str(product['name']).lower() == product_name), None)
                if deleted_product is not None:
                    product_list.remove(deleted_product)

                self.update_product_list(product_list)
                print(f"\n---- Produto '{product_name}' deletado com sucesso. \n----")
            else:
                print(f"\n----- A exclusão do produto '{product_name}' foi cancelada. -----\n")
        else:
            print(f"\n----- Produto não encontrado. -----\n")
