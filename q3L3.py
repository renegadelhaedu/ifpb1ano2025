#questao 3 da lista 3

nome = input('digite seu nome')
while len(nome) <= 3:
    nome = input('ei abestado, mais de 3 viu')

idade = int(input('digite sua idade'))
while idade < 0 or idade > 150:
    idade = int(input('repita sua idade'))

salario = float(input('digite seu salario'))
while salario <= 0:
    salario = float(input('digite seu salario'))

civ = input('digite seu estado civil')
while civ != 's' or civ != 'c' or :
    civ = input('digite seu estado civil novamente')