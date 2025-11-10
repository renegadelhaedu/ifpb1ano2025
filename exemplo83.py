#FUNÇÕES

#1 função sem parâmetros de entrada, sem retorno

def dar_bomdia():
    nome = input('quem veio hoje?')
    for i in range(3):
        print(f'bom dia!!! {nome} veio hoje de novo')

dar_bomdia()