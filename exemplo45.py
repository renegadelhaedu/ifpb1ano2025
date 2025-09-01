#construa uma calculadora que leia 2 numeros repetidamente e após isso
#pergunte qual das 4 operações básicas da matemática o usuário quer efetuar.
#o programa deve encerrar quando o usuário fornecer dois números iguais a 0.
#ao digitar 0 e 0 deve ser imediatamente encerrado.

n1 = 99
n2 = 99
while n1 != 0 and n2 != 0:
    n1 = int(input('digite o numero'))
    n2 = int(input('digite o numero'))
    if n1 == 0 and n2 == 0:
        break
    op = input('qual a operacao')
    if op == 'soma':
        print(n1 + n2)
    elif op == 'subtracao':
        print(n1 - n2)
    elif op == 'multiplicacao':
        print(n1 * n2)
    elif op == 'divisao':
        print(n1 / n2)
    else:
        print('operacao incorreta')



print('o sistema encerrou. tenha um bom dia')
