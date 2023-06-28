produtos = ['tv', 'carro', 'armario', 'teclado']
vendas = [1000, 2000, 500, 200]

tamanho = len(produtos)

print(f'O tamanho da lista é {tamanho}')

mais_vendido = max(vendas)
menos_vendido = min(vendas)

i = vendas.index(mais_vendido)
produto_mais_vendido = produtos[i]

i = vendas.index(menos_vendido)
produto_menos_vendido = produtos[i]

print(
    f'O Produto mais vendido, com {mais_vendido} vendas foi o {produto_mais_vendido}')
print(
    f'O Produto menos vendido, com {menos_vendido} vendas foi o {produto_menos_vendido}')
