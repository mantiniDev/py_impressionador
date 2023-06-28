cpf = input('Digite o número do CPF: ')

if len(cpf) == 11 and cpf.isnumeric():
    print('CPF digitado corretamente')
else:
    print('Digite o CPF corretamente.') 