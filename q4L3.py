#questao 4 da lista 3

popA = int(input('digite a populacao do pais A '))
popB = int(input('digite a populacao do pais B '))
txA = float(input('digite a taxa de crescimento do pais A '))
txB = float(input('digite a taxa de crescimento do pais B '))
qtde_anos = 0
while popA < popB:

    popA = popA * (1 + (txA / 100))
#    popA = popA + (popA * (txA / 100)) #ou esse

    popB = popB * (1 + (txB / 100))
    qtde_anos = qtde_anos + 1

print('a quantidade de anos que demorou foi ', qtde_anos)
