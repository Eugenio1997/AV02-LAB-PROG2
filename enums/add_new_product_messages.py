# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

from enum import Enum


class AddNewProductMessages(Enum):
    SUCCESS = "--------- Produto cadastrado com sucesso! ---------"
    INVALID_VALUES = "------- Campos inválidos. Por favor, tente novamente. -------"
    BLANK_FIELDS = "------- Campos em branco. Preencha todos os campos obrigatórios. -------"
    MAX_RETRIES = "------- Máximo de retentativas alcançado. Tente novamente mais tarde. -------"


