'''
desenvolva um sistema para encontrarmos um amor para nosso amigo
Denilson (quem autorizou foi a prima dele). Ele precisa de um sistema
que leia o nome e vá fazendo perguntas para ao final, o algoritmo determinar se vai
dar match com nosso grande amigo e cupido Denilson.
'''

nome = input('digite seu nome')
idade = int(input('digite sua idade'))

if idade >= 15 and idade <= 20:
    print('uhuuu. ta na minha faixa de idade')
    cidade = input('digite a cidade que voce mora')

    if cidade == 'sousa':
        perto = True
    elif cidade == 'uirauna':
        perto = True
    elif cidade == 'cajazeiras':
        perto = True
    elif cidade == 'aparecida':
        perto = True
    else:
        perto = False

    if perto == True:
        print('uhmmm. mora pertinho. Gostei')
        altura = float(input('digite sua altura'))

        if altura >= 1.5 and altura <= 1.8:
            print('adorei a altura. nos meus padroes')
        else:
            diferenca = (1.7 - altura) * 100
            print('fora dos padroes pois nossa diferenca de altura é', diferenca)
    else:
        print('mora nao, se esconde')

else:
    print('quem sabe no futuro')