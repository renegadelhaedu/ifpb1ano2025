#questao 4 da lista 3
from exemplo26 import qtde_alunos

popA = 80000
popB = 200000
qtde_anos = 0
while popA < popB:

    popA = popA * 1.03
    popB = popB * 1.015
    qtde_anos = qtde_anos + 1

print('a quantidade de anos que demorou foi ', qtde_anos)
