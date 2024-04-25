# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos
class ProductSignupRequirements:
    name_requirements = (
        f"A entrada deve consistir de caracteres alfanuméricos, espaços, pontos, vírgulas, hífens, apóstrofos e "
        f"ampersands.\n"
        f"O comprimento total da entrada deve estar entre 3 e 20 caracteres.\n"
        f"Exemplos Válidos:\n"
        f"  - João Silva\n"
        f"  - Maria & José\n"
        f"  - Teste-123\n"
        f"  - M. Lopes\n"
        f"  - Fernandes'\n"
        f"Exemplos Inválidos:\n"
        f"  - 12 (comprimento menor que 3 caracteres)\n"
        f"  - Este é um exemplo de entrada muito longa para ser válida (comprimento maior que 20 caracteres)\n"
        f"  - Entrada@ComSímbolos (símbolos não permitidos, como '@' e letras acentuadas não especificadas nos requisitos)\n"
        f"  - Entrada Com Espaços 123 (números não são permitidos, pois apenas caracteres alfanuméricos são aceitos)\n"
        f"  - Entrada+Teste (o símbolo '+' não está na lista de caracteres permitidos)"
    )

    price_requirements = (
        f"\nO preço deve ser um número válido com até duas casas decimais.\n"
        f"Permite até três dígitos antes da vírgula (ou ponto).\n"
        f"Permite separador de milhares com vírgula.\n"
        f"Exemplos de formatos válidos: 1,000.00 ou 999.99\n"
        f"Exemplos de formatos inválidos: 100,001 ou 1234 ou abc\n"
    )