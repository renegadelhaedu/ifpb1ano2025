'''
construa um algoritmo em python para ler a frequência
dos alunos cantores, adicionando cadas frequencia em uma lista.
o programa deve ir lendo enquanto nao for digitada nenhum frequenci
negativa.
ao final, mostre a maior, a menor e a média das frequencias
contidas na lista.

'''

talentos = []
freq = float(input('digite a frequencia de sua voz'))

while freq >= 0:
    talentos.append(freq)
    if freq <=20 or freq >= 807:
        break
    freq = float(input('digite a frequencia de sua voz'))

menor = 9999
maior = 0
soma = 0
for f in talentos:
    if f > maior:
        maior = f

    if f < menor:
        menor = f

    soma = soma + f

media = soma / len(talentos)

print(menor)
print(maior)
print(media)














