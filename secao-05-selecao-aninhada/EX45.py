quilos_de_morango = float(input('Kg de morango: '))
quilos_de_maca = float(input('Kg de maçã: '))

custo_morango = quilos_de_morango * 2.50 if quilos_de_morango <= 5 else quilos_de_morango * 2.20
custo_maca = quilos_de_maca * 1.80 if quilos_de_maca <= 5 else quilos_de_maca * 1.50

total_compra = custo_morango + custo_maca
peso_total_compra = quilos_de_morango + quilos_de_maca

if peso_total_compra > 8 or total_compra > 25:
    total_compra = total_compra * 0.90

print(f'Total a pagar: R$ {total_compra:.2f}')
