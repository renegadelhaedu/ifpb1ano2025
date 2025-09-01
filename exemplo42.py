idade = 37
soma = 0
while idade <= 40:
    kms = int(input('diga quantos km vc caminhou quando tinha ' + str(idade)))
    soma = soma + kms
    idade = idade + 1

print('eu percorri no total', soma)
