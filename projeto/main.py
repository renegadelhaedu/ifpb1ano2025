from Funcoes import *
from notFound import notFound
idade = list()#armazena as idades dos infectados
genero = list()#armazena as genero dos infectados
diaTeste = list()#armazena os dias de testes dos infectados
mesTeste = list()#armazena os meses de testes dos infectados
bairro = list()#armazena os bairros de testes  dos infectados
infectados = list()#ID dos Registrados
listInfectados = list()#Armazena o tipo de teste
statusInfectado = list()#Opçoes status da Pessoa
opcoesResultado = ('negativo', 'positivo-swab', 'positivo-igM-igG', 'positivo-igM', 'positivo-igG')#Opções de Resultado
opcoesStatus = ('Curado','Isolamento domiciliar','Internado','Obito')#Opçoes Status
bairrosMaisInfectados = dict()#Armazena o valor percentual de mais incidencia do bairro
bairrosInfectados = set()#Armazena os nomes dos Bairros uma unica vez
historicoSemanasMeses = dict()#Armazena o valor de crescimento de casos semanalmente
percentualSemanal = dict()#Armazena o valor percentual de crescimento de casos semanalmente


RI = 100
while(RI != 0):
    menuInicial()
    RI = int(input('DIGITE O REQUISITO: '))


    if RI == 1:
        cadastroPessoa(idade,bairro,genero,diaTeste,mesTeste,listInfectados,infectados,statusInfectado,opcoesResultado,bairrosInfectados)

    elif RI == 2:
        exibirListaInfectados(listInfectados,diaTeste,mesTeste,infectados,idade,genero,bairro,opcoesStatus,statusInfectado)

    elif RI == 3:
        alterarStatusInfectados(opcoesStatus,infectados,diaTeste,mesTeste,statusInfectado,bairro,genero,idade)

    elif (RI == 4):
        listarInfectadoPorStatus(statusInfectado,listInfectados,diaTeste,mesTeste,infectados,idade,genero,bairro,opcoesStatus)

    elif (RI == 5):
        calcularBairrosMaisInfectados(bairro,bairrosInfectados,bairrosMaisInfectados)

    elif (RI == 6):
        historicoSemMes(historicoSemanasMeses, mesTeste, diaTeste, percentualSemanal)
        taxaCrescimenoPorSemana(historicoSemanasMeses,percentualSemanal,mesTeste)

    elif (RI == 7):
        percentualMascFem(genero)

    elif (RI == 8):
        percentualFaixaEtaria(idade)

    elif (RI == 9):
        percentualCurados(statusInfectado)

    elif (RI == 10):
        historicoSemMes(historicoSemanasMeses,mesTeste,diaTeste,percentualSemanal)
        graficoEvolucaoInfectados(historicoSemanasMeses,mesTeste)

    elif (RI == 404):
        notFound()

