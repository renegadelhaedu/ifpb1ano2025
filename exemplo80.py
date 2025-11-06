#funções
#1-ajuda a modularizar o código
#2-possibilita o reaproveitamento do código
#3-melhor organizaçõa do código

#def contar_vogais(nome):

def somar_numeros(num1, num2):
    soma = num1 + num2
    return soma

def dividir_numeros_mod(num1, num2):
    if num2 == 0:
        return num1
    else:
        saida = num1 / num2
        return saida

#para usar, precisa definir a função antes
resp1 = somar_numeros(1,5)
resp2 = dividir_numeros_mod(99,2)
print(resp1)
print(resp2)