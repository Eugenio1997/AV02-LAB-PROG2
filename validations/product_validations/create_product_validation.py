# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

import re
import time

from product.requirements.product_signup_requirements import ProductSignupRequirements


class ProductValidations:
    """
    Classe responsável por realizar validações relacionadas a produtos.

    Methods:
        validate_name: Valida o nome de um produto.
        validate_price: Valida o preço de um produto.
        convert_to_float: Converte uma string de preço para um valor float.
    """

    def __init__(self):
        """
        Inicializa o objeto ProductValidations.
        """

    def __validate_product_signup_info(self, input_value, pattern, requirements_message) -> str or None or False:
        """
        Valida um valor de entrada com base em um padrão de expressão regular.

        Args:
            input_value (str): O valor a ser validado.
            pattern (str): O padrão de expressão regular para validação.
            requirements_message (str): A mensagem de requisitos a ser exibida em caso de entrada inválida.

        Returns:
            Union[float, str]: O valor validado (como float se for numérico, ou como string caso contrário).
        """
        input_value_float = 0

        if re.match(pattern, input_value):
            input_value_copy = input_value
            input_value_copy = input_value_copy.replace('.', '').replace(',', '')

            if input_value_copy.isdigit():
                input_value_float = float(input_value.replace(',', ''))
                return input_value_float

            return input_value

    def validate_name(self, name):
        """
        Valida o nome de um produto.

        Args:
            name (str): O nome a ser validado.

        Returns:
            str: O nome validado.
        """
        name_pattern = r'^[a-zA-Z0-9\s.,\-\'&áéíóúÁÉÍÓÚçãõâêîôûÇÃÕÂÊÎÔÛ]{3,40}$'
        requirements_message = ProductSignupRequirements.name_requirements
        return self.__validate_product_signup_info(name, name_pattern, requirements_message)

    def validate_price(self, price):
        """
        Valida o preço de um produto.

        Args:
            price (str): O preço a ser validado.

        Returns:
            Union[float, str]: O preço validado como float, ou a string original caso não seja numérico.
        """
        price_pattern = r'^\d{1,3}(?:,\d{3})*(?:\.\d{2})?$'
        requirements_message = ProductSignupRequirements.price_requirements
        return self.__validate_product_signup_info(price, price_pattern, requirements_message)

    def is_empty_product_name(self, product_name: str) -> bool:

        if not any(product_name):
            print(f"\n---- O nome do produto não foi informado. Você será redirecionado para a tela principal \n----")
            time.sleep(0.5)
            return True

        return False
