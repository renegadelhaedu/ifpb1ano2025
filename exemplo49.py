#o professor Paulo decidiu fazer compras no mix mateus.
# considere fazer um algoritmo para ler o valor de cada produto
#comprado pelo professor e repita a leitura dos valores até que
#professor paulo digite o valor 0. ao final, mostre quanto ele
# irá pagar no total

valor_total = 0
produto = float(input('digite o valor do produto'))

while produto != 0:
    valor_total += produto
    produto = float(input('digite o valor do produto'))

print('o valor foi de', valor_total)