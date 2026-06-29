PRECO_GASOLINA = 3.30
PRECO_ALCOOL = 2.90

litros_vendidos = float(input('Litros vendidos: '))
tipo_combustivel = input('Tipo de combustível (A-álcool, G-gasolina): ').upper()

if tipo_combustivel == 'A':
    preco_unitario = PRECO_ALCOOL
    percentual_desconto = 0.03 if litros_vendidos <= 20 else 0.05
else:
    preco_unitario = PRECO_GASOLINA
    percentual_desconto = 0.04 if litros_vendidos <= 20 else 0.06

valor_bruto = litros_vendidos * preco_unitario
valor_desconto = valor_bruto * percentual_desconto
valor_final_abastecimento = valor_bruto - valor_desconto

print(f'Valor a pagar: R$ {valor_final_abastecimento:.2f}')
