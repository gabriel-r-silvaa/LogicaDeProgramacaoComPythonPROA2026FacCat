SENHA_DO_SISTEMA = 1234

senha_informada = int(input('Digite a senha: '))

if senha_informada == SENHA_DO_SISTEMA:
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')
