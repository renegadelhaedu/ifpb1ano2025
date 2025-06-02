qtde = int(input('digite a quantiade de horas'))
valor = float(input('digite o valor da hora '))
salario = qtde * valor

sind = salario * 0.97
fgts = salario * 0.89

if salario <= 900:
    ir = 0
else:
    if salario <= 1500:
        ir = salario * 0.95 #retirando 5%
    else:
        if salario <= 2500:
            ir = salario * 0.90
        else:
            if salario > 2500:
                ir = salario * 0.80

print(sind)
print(fgts)
print(ir)
liquido = salario - sind - fgts - ir
print(liquido)

