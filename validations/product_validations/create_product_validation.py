import re
from product.requirements.product_signup_requirements import ProductSignupRequirements


class ProductValidations:

    def __init__(self):
        pass

    def __validate_product_signup_info(self, input_value, pattern, requirements_message):
        input_value_float = 0
        while True:
            if re.match(pattern, input_value):
                input_value_copy = input_value
                input_value_copy = input_value_copy.replace('.', '').replace(',', '')

                if input_value_copy.isdigit():
                    input_value_float = self.convert_to_float(input_value)

                return input_value_float
            else:
                print(requirements_message)
                input_value = input(f"\nDigite o valor novamente: ")

    def validate_name(self, name):
        name_pattern = r'^[a-zA-Z0-9\s.,\-\'&]{3,20}$'
        requirements_message = ProductSignupRequirements.name_requirements
        return self.__validate_product_signup_info(name, name_pattern, requirements_message)

    def validate_price(self, price):
        price_pattern = r'^\d{1,3}(?:,\d{3})*(?:\.\d{2})?$'
        requirements_message = ProductSignupRequirements.price_requirements
        return self.__validate_product_signup_info(price, price_pattern, requirements_message)

    def convert_to_float(self, price):
        return float(price)
