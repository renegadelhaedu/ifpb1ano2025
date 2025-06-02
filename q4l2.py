'''
faça um programa em python que pergunte ao usuário qual
o time que ele é torcedor. se o usuário informar que é
o palmeiras, pergunte quantos titulos mundiais ele possui.
se a quantidade for maior que zero, deseje os parabéns.
caso nao, diga: só lamento!
'''
time = input('digite qual seu time')
if time == 'palmeiras':
    titulos = int(input('quantos títulos mundiais o palmeiras possui?'))
    if titulos > 0:
        print('só se for no baralho ou dominó')
    else:
        print('só lamento')
else:
    print('sorte a sua')














