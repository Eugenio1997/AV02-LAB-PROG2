class Product:
    __product_list = []

    def __init__(self):
        pass

    @staticmethod
    def add_to_inventory(name: str, price: float) -> None:
        Product.__product_list.append({"name": name, "price": price})
        print("--------------- Cadastro realizado com sucesso. ---------------\n")

    def get_product_signup_info(self) -> [str, str]:
        print("---------- Realizando Cadastro de Produto ----------")
        name: str = input("Digite o nome: ")
        price: str = input("Digite o preço: ")

        is_valid: bool = self.validate_product_signup_info(name, price)

        if is_valid:
            return name, price
        else:
            return None

    def is_empty(self, name: str, price: str) -> bool:
        return name.strip() == "" or price.strip() == ""

    @staticmethod
    def get_list() -> list[dict[str, float]]:
        return Product.__product_list

    def validate_product_signup_info(self, name: str, price: str) -> bool:
        if self.is_empty(name, price):
            print(f'\nNão podem conter campos em branco')
            self.get_product_signup_info()
        else:
            return True  # A entrada não está em branco