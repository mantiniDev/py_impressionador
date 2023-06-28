produtos = ['tv', 'carro', 'armario', 'teclado']
estoque = [1000, 2000, 500, 200]

produtos.append('iphone11')

print(produtos)

try:
    produtos.remove('iphone11')
except:
    print(f'Não existe o iphone13')

print(produtos)

