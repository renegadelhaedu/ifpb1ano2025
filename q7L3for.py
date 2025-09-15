#questao 7 da lista 3
maior = 0
for cont in range(5):
    numero = int(input('digite um numero'))
    if numero > maior:
        maior = numero
print('o maior numero de todos foi ', maior)