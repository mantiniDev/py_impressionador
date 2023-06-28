produtos = ['tv', 'carro', 'armario', 'teclado']
estoque = [1000, 2000, 500, 200]

produto = input('Insira o nome do produto em letras minuscula.\n')


if produto in produtos:
    i = produtos.index(produto)
    print(f'O Produto {produto} consta no estoque na quantidade de {estoque[i]}')
else :
    print(f'Não temos o {produto} em estoque')
