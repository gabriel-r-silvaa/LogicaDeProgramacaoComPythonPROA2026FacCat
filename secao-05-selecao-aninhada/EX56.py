primeiro_operando = float(input('Primeiro valor: '))
segundo_operando = float(input('Segundo valor: '))
operacao_escolhida = int(input('Operação (1-Adição, 2-Subtração, 3-Divisão, 4-Multiplicação): '))

if operacao_escolhida == 1:
    resultado_operacao = primeiro_operando + segundo_operando
elif operacao_escolhida == 2:
    resultado_operacao = primeiro_operando - segundo_operando
elif operacao_escolhida == 3:
    resultado_operacao = primeiro_operando / segundo_operando
elif operacao_escolhida == 4:
    resultado_operacao = primeiro_operando * segundo_operando

print(f'Resultado: {resultado_operacao}')
