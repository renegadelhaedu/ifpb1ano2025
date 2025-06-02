salario = float(input('digite seu salario'))

if salario <= 280:
    final = salario * 1.20
    perc = 20
else:
    if salario <= 700:
        final = salario * 1.15
        perc = 15
    else:
        if salario <= 1500:
            final = salario * 1.10
            perc = 10
        else:
            if salario > 1500:
                final = salario * 1.05
                perc = 5

print(salario)
print(perc)
print(final - salario)
print(final)









