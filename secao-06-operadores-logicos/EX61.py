nome_produto = input('Descrição do produto: ')
quantidade_adquirida = int(input('Quantidade adquirida: '))
preco_unitario = float(input('Preço unitário: R$ '))

valor_bruto = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
    percentual_desconto = 0.02
elif quantidade_adquirida <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05

valor_desconto = valor_bruto * percentual_desconto
total_a_pagar = valor_bruto - valor_desconto

print(f'Produto: {nome_produto}')
print(f'Total: R$ {valor_bruto:.2f}')
print(f'Desconto ({percentual_desconto * 100:.0f}%): R$ {valor_desconto:.2f}')
print(f'Total a pagar: R$ {total_a_pagar:.2f}')
