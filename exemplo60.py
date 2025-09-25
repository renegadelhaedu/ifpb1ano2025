#construa um algoritmo em python para receber o nome, altura e peso
#de 150 pessoas. o programa deve ir recebendo os dados, calculando
#o IMC e informando se a pessoa está bem, regular ou precisa de ajuda

for i in range(150):
    n = input('\nDigite seu nome: ')
    a = float(input('Digite sua altura: '))
    p = float(input('Digite seu peso: '))
    imc = p / (a * a)
    imc = round(imc, 2)
    if imc < 18.5:
        print(n,'você está em estado de magreza.', imc)
    elif imc >= 18.5 and imc <= 24.9:
        print(n,'você está no peso ideal.', imc)
    elif imc >= 25 and imc <= 29.9:
        print(n, 'Você está acima do normal.', imc)
    else:
        print(n, 'Você está muito acima do normal.', imc)
