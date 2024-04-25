# Autor: Eugenio Lopes Fernandes Lima, Nathalya Lessa e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos
class ProductSignupRequirements:
    name_requirements = (
        f"A entrada deve consistir de caracteres alfanuméricos, espaços, pontos, vírgulas, hífens, apóstrofos, "
        f"ampersands e acentos.\n"
        f"O comprimento total da entrada deve estar entre 3 e 40 caracteres.\n"
        f"Exemplos Válidos:\n"
        f"  - Panela Turbo 5\n"
        f"  - Corta-Pizza 3000\n"
        f"  - Notebook Gamer i7\n"
        f"  - Café Gourmet Arábica 250g\n"
        f"  - Tênis Esportivo Running 39\n"
        f"  - Chaleira Elétrica 1.5L\n"
        f"  - Kit Facas 5 Peças\n"
        f"  - Óculos de Sol Vintage Redondos\n"
        f"  - Relógio Masculino Esportivo Digital\n"
        f"  - Creme H2O 50g\n"
        f"Exemplos Inválidos:\n"
        f"  - 12 (comprimento menor que 3 caracteres)\n"
        f"  - Este é um exemplo de entrada muito longa para ser válida (comprimento maior que 40 caracteres)\n"
        f"  - Entrada@ComSímbolos (símbolos não permitidos, como '@' e outros não especificados nos requisitos)\n"
        f"  - Entrada Com Espaços 123 (números não são permitidos, apenas caracteres alfanuméricos e acentos)\n"
        f"  - Entrada+Teste (o símbolo '+' não está na lista de caracteres permitidos)"
    )

    price_requirements = (
        f"\nO preço deve ser um número válido com até duas casas decimais.\n"
        f"Permite até três dígitos antes da vírgula (ou ponto).\n"
        f"Permite separador de milhares com vírgula.\n"
        f"Exemplos de formatos válidos: 1,000.00 ou 999.99\n"
        f"Exemplos de formatos inválidos: 100,001 ou 1234 ou abc\n"
    )