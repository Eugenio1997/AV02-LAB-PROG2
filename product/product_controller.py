from validations.product_validations.create_product_validation import ProductValidations
from product.requirements.product_signup_requirements import ProductSignupRequirements

class ProductController:
    __product_list = [] # Lista para armazenar os produtos

    def __init__(self):
        self.product_validations_manager = ProductValidations()

    @classmethod
    def add_to_inventory(cls, product_dict) -> None:
        if isinstance(product_dict, dict) and "name" in product_dict and "price" in product_dict:
            cls.__product_list.append(dict(name=product_dict["name"], price=product_dict["price"]))
            print("--------------- Cadastro realizado com sucesso. ---------------\n")
        else:
            raise ValueError("O dicionário fornecido não contém as chaves 'name' e 'price'.")

    def get_product_signup_info(self) -> [str, str]:

        print("---------- Realizando Cadastro de Produto ----------")

        name: str = input(f'{ProductSignupRequirements.name_requirements}\nDigite o nome: ')
        price: str = input(f'{ProductSignupRequirements.price_requirements}\nDigite o preço: ')

        name, price = self.__remove_whitespaces(name, price)

        name_valided: str = self.product_validations_manager.validate_name(name)
        price_valided: str = self.product_validations_manager.validate_price(price)

        while not [name_valided, price_valided]:
            print("\n---------------- Os campos são obrigatórios ----------------\n")
            name_valided, price_valided = self.get_product_signup_info()

        # return validated_product_data
        return name_valided, price_valided

    @classmethod
    def get_product_list(cls) -> list[dict[str, float]]:
        return cls.__product_list

    def __remove_whitespaces(self, name: str, price: str) -> tuple[
        str, str]:

        name = name.replace(" ", "")
        price = price.replace(" ", "")

        return name, price
