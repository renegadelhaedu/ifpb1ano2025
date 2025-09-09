#o prefeito de sousa lhe contratou para desenvolver um programa que
# leia as  temperaturas, e informe ao final a menor e a maior
# temperaturas informadas, bem como a média das temperaturas. o programa deve
#ler temperaturas enquanto elas forem maiores que 16.
maior = 0
menor = 100
qtde = 0
soma = 0
temp = float(input('digite a temperatura '))
while temp > 16:
    qtde += 1
    soma += temp
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    temp = float(input('digite a temperatura '))

media = soma / qtde
print('a media foi' , media)
print('a menor foi' , menor)
print('a maior foi' , maior)