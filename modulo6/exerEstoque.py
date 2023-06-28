nomeProduto = input('Inserir o nome do poduto: ')
categoria = input('Inserir o nome do poduto (alimento, bebidas, limpeza): ')
quantidade = input('Inserir a quantidade de produtos: ')

if nomeProduto and categoria and quantidade:
    quantidade = int(quantidade)
    if categoria == 'alimentos' and quantidade < 50:
        print(f'Solicitar {nomeProduto} á equipe de compras, temos apenas {quantidade} em estoque')
    elif categoria == 'bebidas' and quantidade < 75:
        print(f'Solicitar {nomeProduto} á equipe de compras, temos apenas {quantidade} em estoque')
    elif categoria == 'limpeza' and quantidade < 30:
        print(f'Solicitar {nomeProduto} á equipe de compras, temos apenas {quantidade} em estoque')
    else:
        print(f'Produto {nomeProduto} inserido corretamente')
else:
    print('Preencha corretamente os campos')
        
