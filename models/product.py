class Product:
    """
    Representa um produto com um nome e um preço.

    Attributes:
        name (str): O nome do produto.
        price_str (str): O preço do produto em formato de string.

    Methods:
        to_dict(): Converte o produto em um dicionário.

    Properties:
        name (str): Retorna o nome do produto.
        price (str): Retorna o preço do produto como uma string.
    """

    def __init__(self, name: str, price_str: str):
        """
        Inicializa um novo objeto Product.

        Args:
            name (str): O nome do produto.
            price_str (str): O preço do produto em formato de string.
        """
        self.__name = name
        self.__price = price_str

    def to_dict(self):
        """
        Converte o produto em um dicionário.

        Returns:
            dict: Um dicionário contendo as informações do produto.
        """
        return dict(name=self.name, price=self.price)

    @property
    def name(self):
        """
        Getter para o nome do produto.

        Returns:
            str: O nome do produto.
        """
        return self.__name

    @property
    def price(self):
        """
        Getter para o preço do produto em formato de string.

        Returns:
            str: O preço do produto.
        """
        return self.__price
