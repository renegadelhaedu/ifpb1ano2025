#desenvolva um programa/algoritmo em python que leia do usuário os seguintes dados:
#s0 é o deslocamento inicial
#v0 é a velocidade inicial
#t é o tempo gasto para percorrer
#a é a aceleração
#O algoritmo deve ao final exibir o valor do deslocamento final realizado.

s0 = float(input('digite seu desclocamento inicial'))
v0 = float(input('digite sua velocidade inicial'))
t = float(input('digite o tempo gasto'))
a = float(input('digite a aceleracao realizada'))

s =  s0 + (v0 * t) + ((a * (t * t)) / 2)

print('o desclocamento final foi ', s)