from Funcoes import *
def notFound():
    '''

    ESTA FUNCAO SERA USADA PELO MASTER DA PROGRAMACAO PARA VER AS DESCRICOES DE TODAS AS FUNCOES, INCLUINDO ESTA :)

    '''
    buscaDEF = 100
    while (buscaDEF != 0):
        print('\nOPCAO DE DESENVOLVEDOR\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n0- ENCERRAR OPCAO DE DESENVOLVEDOR\n1- menuInicial\n2- cadastroPessoa(R1)\n3- historicoSemMes(R6/R10)\n4- exibirListaInfectados(R2)\n5- alterarStatusInfectados(R3)\n6- listarInfectadoPorStatus(R4)\n7- calcularBairrosMaisInfectados(R5)\n8- taxaCrescimenoPorSemana(R6)\n9- percentualMascFem(R7)\n10- percentualFaixaEtaria(R8)\n11- percentualCurados(R9)\n12- graficoEvolucaoInfectados(R10)\n404- notFound')
        buscaDEF = int(input('DIGITE A DEF QUE DESEJA VER: '))

        if (buscaDEF == 1):
            help(menuInicial)
        if (buscaDEF == 2):
            help(cadastroPessoa)
        if (buscaDEF == 3):
            help(historicoSemMes)
        if (buscaDEF == 4):
            help(exibirListaInfectados)
        if (buscaDEF == 5):
            help(alterarStatusInfectados)
        if (buscaDEF == 6):
            help(listarInfectadoPorStatus)
        if (buscaDEF == 7):
            help(calcularBairrosMaisInfectados)
        if (buscaDEF == 8):
            help(taxaCrescimenoPorSemana)
        if (buscaDEF == 9):
            help(percentualMascFem)
        if (buscaDEF == 10):
            help(percentualFaixaEtaria)
        if (buscaDEF == 11):
            help(percentualCurados)
        if (buscaDEF == 12):
            help(graficoEvolucaoInfectados)
        if (buscaDEF == 404):
            help(notFound)
