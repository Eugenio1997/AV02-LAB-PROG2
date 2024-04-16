from validations.product_validations.create_product_validation import ProductValidations
from product.requirements.product_signup_requirements import ProductSignupRequirements


class ProductController:
    """
    Classe responsável por controlar a gestão de produtos no sistema.

    Attributes:
        __product_list (list): Lista para armazenar os produtos cadastrados.
    """

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

    def __remove_whitespaces(self, name: str, price: str) -> tuple[str, str]:
        """
        Remove espaços em branco de uma string.

        Args:
            name (str): O nome a ser processado.
            price (str): O preço a ser processado.

        Returns:
            tuple[str, str]: Uma tupla contendo o nome e o preço sem espaços em branco.
        """
        return name.replace(" ", ""), price.replace(" ", "")
