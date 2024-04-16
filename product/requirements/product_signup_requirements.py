class ProductSignupRequirements:
    name_requirements = (
        f"A entrada deve consistir de caracteres alfanuméricos, espaços, pontos, vírgulas, hífens, apóstrofos e ampersands.\n"
        f"O comprimento deve estar entre 3 e 20 caracteres.\n"
        f"Caracteres especiais são permitidos conforme especificado acima."
    )

    price_requirements = (
        f"\nO preço deve ser um número válido com até duas casas decimais.\n"
        f"Permite até três dígitos antes da vírgula (ou ponto).\n"
        f"Permite separador de milhares com vírgula.\n"
        f"Exemplos de formatos válidos: 1,000.00 ou 999.99\n"
        f"Exemplos de formatos inválidos: 100,001 ou 1234 ou abc\n"
    )