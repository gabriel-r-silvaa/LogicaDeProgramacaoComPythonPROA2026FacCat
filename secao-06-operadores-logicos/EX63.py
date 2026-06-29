from datetime import date

codigo_funcionario = input('Código do funcionário: ')
ano_nascimento = int(input('Ano de nascimento: '))
ano_ingresso = int(input('Ano de ingresso na empresa: '))

ano_atual = date.today().year
idade_funcionario = ano_atual - ano_nascimento
tempo_servico = ano_atual - ano_ingresso

print(f'Idade: {idade_funcionario} anos')
print(f'Tempo de trabalho: {tempo_servico} anos')

pode_aposentar = (
    idade_funcionario >= 65 or
    tempo_servico >= 30 or
    (idade_funcionario >= 60 and tempo_servico >= 25)
)

if pode_aposentar:
    print('Requerer aposentadoria')
else:
    print('Não requerer aposentadoria')
