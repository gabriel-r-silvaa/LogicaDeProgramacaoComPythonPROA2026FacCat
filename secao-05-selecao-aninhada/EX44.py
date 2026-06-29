idade_primeiro_homem = int(input('Idade do 1º homem: '))
idade_segundo_homem = int(input('Idade do 2º homem: '))
idade_primeira_mulher = int(input('Idade da 1ª mulher: '))
idade_segunda_mulher = int(input('Idade da 2ª mulher: '))

if idade_primeiro_homem > idade_segundo_homem:
    homem_mais_velho = idade_primeiro_homem
    homem_mais_novo = idade_segundo_homem
else:
    homem_mais_velho = idade_segundo_homem
    homem_mais_novo = idade_primeiro_homem

if idade_primeira_mulher > idade_segunda_mulher:
    mulher_mais_velha = idade_primeira_mulher
    mulher_mais_nova = idade_segunda_mulher
else:
    mulher_mais_velha = idade_segunda_mulher
    mulher_mais_nova = idade_primeira_mulher

soma_velho_com_nova = homem_mais_velho + mulher_mais_nova
produto_novo_com_velha = homem_mais_novo * mulher_mais_velha

print(f'Soma (homem mais velho + mulher mais nova): {soma_velho_com_nova}')
print(f'Produto (homem mais novo * mulher mais velha): {produto_novo_com_velha}')
