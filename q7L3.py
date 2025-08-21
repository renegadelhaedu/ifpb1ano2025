#questao 7 da lista 3
maior = 0
cont = 0

while cont < 5:
    numero = int(input('digite um numero'))
    if numero > maior:
        maior = numero
    cont += 1

print('o maior numero de todos foi ', maior)