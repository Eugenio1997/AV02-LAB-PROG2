import time
from typing import Optional, Tuple, List

from enums.add_new_product_messages import AddNewProductMessages
from enums.auth_messages import AuthMessages
from enums.menu_options import Options
from enums.user_signup_messages import UserSignupMessages


class Utils:
    MAX_RETRIES = 3

    @staticmethod
    def check_and_reset_retries_count(retry_count: int, counter: int, is_authenticated: bool, user_saved: bool, product_saved: bool,
                                      option: str) -> \
            tuple[int, int]:

        if retry_count == Utils.MAX_RETRIES and counter == 0:
            if not is_authenticated and option == Options.AUTHENTICATE.value:
                print(f"{AuthMessages.MAX_RETRIES.value}\n")
            elif not is_authenticated and not user_saved and option == Options.REGISTER.value:
                print(f"{UserSignupMessages.MAX_RETRIES.value}\n")
            elif is_authenticated and not product_saved and option == Options.ADD_NEW_PRODUCT.value:
                print(f"{AddNewProductMessages.MAX_RETRIES.value}\n")
        retry_count = 0
        counter = 3
        time.sleep(0.5)
        return retry_count, counter
