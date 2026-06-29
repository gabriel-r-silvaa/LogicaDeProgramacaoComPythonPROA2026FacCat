CODIGO_VALIDO = 1234
SENHA_VALIDA = 9999

codigo_digitado = int(input('Código de usuário: '))

if codigo_digitado != CODIGO_VALIDO:
    print('Usuário inválido!')
else:
    senha_digitada = int(input('Senha: '))

    if senha_digitada != SENHA_VALIDA:
        print('Senha incorreta')
    else:
        print('Acesso permitido')
