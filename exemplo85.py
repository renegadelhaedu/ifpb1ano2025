#FUNÇÕES

#3 função sem parâmetros de entrada, com retorno

def dar_bomdia():
    qtde = 0
    for i in range(3):
        resposta = input('digite sim se Lucas veio hoje')
        if resposta == 'sim':
            qtde = qtde + 1
    return qtde

saida = dar_bomdia()
print(f'Lucas veio {saida} vezes esta semana')