megasena = []

for i in range(6):
    n = int(input('diga uma dezena entre 1 e 60'))
    while n < 1 or n > 60 or n in megasena:
        n = int(input('diga uma dezena entre 1 e 60'))

    megasena.append(n)

print(megasena)
