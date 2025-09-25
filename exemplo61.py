#Meu amigo Lucas foi para a festa de sao joao e precisa de um programa
#em python para perguntar se as meninas querem dançar com ele.
#faça um algoritmo que leia a resposta de 15 pessoas para a pergunta.
#o programa ao final deve exibir o percentual de respostas positivas
# e o percentual de respostas negativas

sim = 0
nao = 0
for i in range(15):
    m = input('aceita dançar?')
    if m == 'sim':
        sim += 1
    else:
        nao += 1
per1 = (sim/15) * 100
per2 = (nao/15) * 100
print(round(per1,2))
print(round(per2,2))