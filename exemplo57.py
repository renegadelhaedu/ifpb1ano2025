#estrutura de repetição for
'''
exiba todos os números de 1 até 50, exceto o 11
'''
numero = int(input('me diga um numero '))
qtde = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        qtde += 1

if qtde == 2:
    print('primo')
else:
    print('nao é primo')

