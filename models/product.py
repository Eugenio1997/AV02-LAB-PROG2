
class Product:
    def __init__(self, name: str, price_str: str):
        self.__name = name
        self.__price = price_str

    def to_dict(self):
        return dict(name=self.name, price=self.price)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
