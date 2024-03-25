class Product:
    products = []

    def __init__(self, name, preco):
        self.name = name,
        self.preco = preco

    @staticmethod
    def add_to_inventory(name, preco):
        product = {
            "name": name,
            "preco": preco
        }
        Product.products.append(product)
        print("--------------- Cadastro realizado com sucesso. ---------------\n")

    @staticmethod
    def get_data():
        print("---------- Realizando Cadastro de Produto ----------")
        name = input("Digite o nome: ")
        preco = input("Digite o preço: ")

        return name, preco

    @staticmethod
    def get_list():
        return Product.products
