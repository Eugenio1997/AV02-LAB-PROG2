

class Product:
    __products = []

    def __init__(self, name, price):
        self.name = name,
        self.price = price

    @staticmethod
    def add_to_inventory(name: str, price: float) -> None:
        Product.__products.append({"name": name, "price": price})
        print("--------------- Cadastro realizado com sucesso. ---------------\n")

    @staticmethod
    def get_product_signup_info() -> [str, str]:
        print("---------- Realizando Cadastro de Produto ----------")
        name: str = input("Digite o nome: ")
        price: str = input("Digite o preço: ")

        is_valid: bool = Product.validate_product_signup_info(name, price)

        if is_valid:
            return name, price
        else:
            return None

    @staticmethod
    def is_empty(name: str, price: str) -> bool:
        return name.strip() == "" or price.strip() == ""

    @staticmethod
    def get_list() -> list[dict[str, float]]:
        return Product.__products

    @staticmethod
    def validate_product_signup_info(name: str, price: str) -> bool:

        if Product.is_empty(name, price):
            print(f'\nNão podem conter campos em branco')
            Product.get_product_signup_info()
        else:
            return True  # A entrada não está em branco
