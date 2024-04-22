# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

from enum import Enum

class Options(Enum):
    REGISTER = "1"
    AUTHENTICATE = "2"
    EXIT = "3"
    ADD_NEW_PRODUCT = "4"
    LIST_PRODUCTS = "5"
    DELETE_PRODUCT = "6"
    EDIT_PRODUCT = "7"
