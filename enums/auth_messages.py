# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos

from enum import Enum


class AuthMessages(Enum):
    SUCCESS = "--------- Autenticação bem-sucedida! ---------"
    INVALID_CREDENTIALS = "------- Credenciais inválidas. Por favor, tente novamente. -------"
    BLANK_FIELDS = "------- Campos em branco. Preencha todos os campos obrigatórios. -------"
    MAX_RETRIES = "------- Máximo de retentativas alcançado. Tente novamente mais tarde. -------"


