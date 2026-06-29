numero_conta = input('Número da conta: ')
saldo_anterior = float(input('Saldo: R$ '))
valor_debito = float(input('Débito: R$ '))
valor_credito = float(input('Crédito: R$ '))

saldo_atualizado = saldo_anterior - valor_debito + valor_credito

print(f'Conta: {numero_conta}')
print(f'Saldo atual: R$ {saldo_atualizado:.2f}')

if saldo_atualizado >= 0:
    print('Saldo Positivo')
else:
    print('Saldo Negativo')
