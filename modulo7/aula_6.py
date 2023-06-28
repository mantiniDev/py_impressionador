#formatação de strings
# :< alinha para esquerda
# :> alinha pra direita
# :^ alinha no centro
# :+ coloca o sinal sempre na frente do número, não importando se é positivo ou negativo
# :, coloca vircula como separador de milhar
# :_ coloca como separador de milhar
# :e formato científico
# :f número com quantidade fixa de casas decimais
# :x formato HEX minuscula - para cores
# :X formato HEX maiscula - para cores
# :% formato percentual
# round arredondar
##
email = 'lira@gmail.com'
print(f'Meu email não é : {email:^30} ta bem')

valor = 360 - 400
print(f'Valor 1 =  {valor:+}')

valor2 = 1000 + 3000
print(f'Valor 2 = {valor2:,.2f}')

valor3 = 3.500*3004034
print(f'Valor 3 = {valor3:,.2f}')


