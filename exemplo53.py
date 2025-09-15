'''
construa um algoritmo em python para ler o nome e a idade
dos 29 alunos do primeiro ano e ao final exiba a soma das idades de todos os alunos.
'''

soma = 0
for repeticao in range(29):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    soma = soma + idade

print('ao total, as idades somadas sao', soma)