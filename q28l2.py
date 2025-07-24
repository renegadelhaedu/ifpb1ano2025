tipo = input('qual o tipo de carne').lower()
qtde = float(input('qual a quantidade de carne'))
pag = input('voce vai pagar usando cartao tabajara?')

if tipo == 'file' and qtde <= 5:
    preco = 4.9 * qtde
elif tipo == 'file' and qtde > 5:
    preco = 5.8 * qtde
elif tipo == 'alcatra' and qtde <= 5:
    preco = 5.9 * qtde
elif tipo == 'alcatra' and qtde > 5:
    preco = 6.8 * qtde
elif tipo == 'picanha' and qtde <= 5:
    preco = 6.9 * qtde
elif tipo == 'picanha' and qtde > 5:
    preco = 7.8 * qtde
else:
    preco = 0

if preco > 0:
    if pag == 'sim':
        preco = preco * 0.95
        print('voce recebeu desconto por comprar no tabajara')

    print('voce tem que pagar em reais', preco)
else:
    print('nao trabalhamos com este tipo de carne')
