#um jogador de futebol do palmeiras precisa contar quantos gols
#seu time levou. cada gol levado pelo palmeiras, deve ser inserido
#no algoritmo com o nome do jogador que fez o gol. o sistema
#deve contar quantos gols o palmeiras levou enquanto nao for digitado
#a palavra "acabou". ao final, deve-se mostrar quantos gols o palmeiras
# levou.

gols = 0
nome_jogador = input('quem fez o gol ')
while nome_jogador != 'acabou':
    gols += 1
    nome_jogador = input('quem fez o gol ')

#modifique este código para que o algoritmo mostre na tela
# se foi goleada, vitória apertada ou sem gols
if gols > 3:
    print('goleada')
elif gols > 0 and gols <= 3:
    print('apertado')
else:
    print('sem gols')

