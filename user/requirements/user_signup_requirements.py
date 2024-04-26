# Autor: Eugenio Lopes Fernandes Lima e Eliatan Almeida
# Contato: eugeniolopesfernandeslima1997@outlook.com
# Descrição: Sistema de gerenciamento de produtos
class UserSignupRequirements:
    password_requirements = (
        f"\nPor favor, digite uma senha que atenda aos seguintes critérios:\n"
        f"- Pelo menos 8 caracteres\n"
        f"- Pelo menos 1 letra maiúscula\n"
        f"- Pelo menos 1 letra minúscula\n"
        f"- Pelo menos 1 número\n"
        f"- Pelo menos 1 caractere especial"
    )

    phone_number_requirements = (
        f"\nPor favor, digite um número que atenda aos seguintes critérios:\n"
        f"- O código de área deve estar entre parênteses e consistir em dois dígitos numéricos (XX).\n"
        f"- Após o código de área, digite um espaço.\n"
        f"- Em seguida, digite o número de telefone, começando com o dígito '9'.\n"
        f"- O número de telefone deve ter um total de 9 dígitos após o '9', seguidos por um hífen e mais 4 dígitos.\n\n"
        f"Exemplos válidos de números de telefone neste formato são:\n"
        f"- (11) 91234-5678\n"
        f"- (21) 97654-3210\n"
        f"- (47) 93333-4444\n"
        f"- (99) 98888-7777\n\n"
        f"Por favor, certifique-se de seguir exatamente este formato ao inserir o número de telefone."
    )

    email_requirements = (
        f"\nPor favor, digite um endereço de e-mail que atenda aos seguintes critérios:\n"
        f"- Deve conter um único símbolo '@'\n"
        f"- Deve conter pelo menos um caractere antes do '@'\n"
        f"- Deve conter pelo menos um caractere depois do '@'\n"
        f"- Deve conter um ponto '.' após o '@', seguido por pelo menos dois caracteres\n"
        f"- Não deve conter espaços em branco\n"
        f"- Pode conter letras maiúsculas, minúsculas, números e os seguintes caracteres especiais: !#$%&'*+-/=?^_`{{|}}~\n\n"
        f"Exemplos válidos de endereços de e-mail:\n"
        f"- usuario@example.com\n"
        f"- meu_email123@gmail.com\n"
        f"- contato@site.com.br\n"
    )

    name_requirements = (
        f"\nO nome deve conter apenas letras (maiúsculas e minúsculas).\n"
        f"Deve ter entre 3 e 20 caracteres de comprimento.\n"
        f"Deve começar com uma letra (maiúscula ou minúscula).\n"
        f"Se houver mais de uma palavra, elas devem ser separadas por um único espaço.\n"
    )

