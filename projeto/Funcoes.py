def menuInicial():
    '''
    ESTA FUNCAO RESPONSAVEL POR EXIBIR TODSS OS POSSIVEIS REQUISITOS AO SER INICIADO O PROGRAMA
    '''
    print('=+' * 30)
    print('MENU PRINCIPAL\n\n0- ENCERRAR PROGRAMA\n1- Cadastro de pessoa testada\n2- Exibir lista de pacientes infectados por ordem de teste\n3- Inserir status do paciente infectado\n4- Listar infectados por status\n5- Calcular bairros mais infectados\n6- Calcular taxa de crescimento dos casos por semana\n7- Calcular o percentual de homens e mulheres infectados\n8- Calcular o percentual de infectados por faixa etária\n9- Calcular o percentual de curados\n10-Exibir um gráfico com a evolução da quantidade de infectados')
    print('=+' * 30)

#R1
def cadastroPessoa(idade,bairro,genero,diaTeste,mesTeste,listInfectados,infectados,statusInfectado,opcoesResultado,bairrosInfectados):
    '''
    ESTA FUNCAO E RESPOSAVEL PELO CADASTRO DE TODAS AS PESSOAS AO SISTEMA

    :param idade:  ira adicionar a esta lista as idades das pessoas infectadas
    :param bairro:  ira adicionar a esta lista os bairros das pessoas infectados
    :param genero:  ira adicionar a esta lista os generos das pessoas infectados
    :param diaTeste:  ira adicionar a esta lista os dias que foram feitos os testes das pessoas infectados
    :param mesTeste:  ira adicionar a esta lista os meses que foram feitos os testes das pessoas infectados
    :param listInfectados:  ira adicionar a esta lista o tipo de teste usado (vindo da tupla de opcoes de resultado)
    :param infectados:  ira adicionar a esta lista o ID da pessoas infectadas
    :param statusInfectado:  ira adicionar a esta lista o status da pessoas infectada (na primeira vez que a pessoas e cadastrada esta como em isolamento social)
    :param opcoesResultado:  ira chamar esta tupla para que seja escolhida uma das opcoes dentro dela
    :param bairrosInfectados:  ira adicionar a esta lista os bairros registrados somente uma unica vez por bairro(utilizado na R5)
    :return:  ira adicionar a todas as listas os valores que forem manipulados
    '''

    #entrada da idade da pessoa
    try:
        entradaIdade = int(input('\nIDADE: '))
    except:
        print('DIGITE UM NUMERO!')
        entradaIdade = -1
    #condicional para que o valor de entrada nao ultrapasse os parametros permitidos(pedira novamente enquanto estiver errado)
    while ((entradaIdade < 0) or (entradaIdade > 150)):
        print('!!!VALOR FORA DOS PARAMETROS!!!')
        try:
            entradaIdade = int(input('\nIDADE: '))
        except:
            print('DIGITE UM NUMERO!')
            entradaIdade = -1

    try:
        entradaGenero = input('GENERO(m- MASCULINO ou f- FEMININO): ')
        entradaGenero = entradaGenero.upper()
    except:
        entradaGenero = 'a'
    while ((entradaGenero != 'M') and (entradaGenero != 'F')):
        print('!!!VALOR FORA DOS PARAMETROS!!!')
        try:
            entradaGenero = input('\nGENERO(m- MASCULINO ou f- FEMININO): ')
            entradaGenero = entradaGenero.upper()
        except:
            entradaGenero = 'a'
    valGenero = 0
    if (entradaGenero == 'M'):
        valGenero = ('masc.')
    elif (entradaGenero == 'F'):
        valGenero = ('fem.')

    try:
        entradaDia = int(input('DIA DO TESTE: '))
    except:
        entradaDia = 0
    while (entradaDia < 1 or entradaDia > 31):
        print('!!!VALOR FORA DOS PARAMETROS!!!')
        try:
            entradaDia = int(input('\nDIA DO TESTE: '))
        except:
            entradaDia = 0

    try:
        entradaMes = int(input('MES DO TESTE: '))
    except:
        entradaMes = 0
    while (entradaMes < 1 or entradaMes > 12):
        print('!!!VALOR FORA DOS PARAMETROS!!!')
        try:
            entradaMes = int(input('\nMES DO TESTE: '))
        except:
            entradaMes = 0

    entradaBairro = input('BAIRRO: ')
    entradaBairro = entradaBairro.upper()

    print('-' * 20)
    print('RESULTADO DO TESTE COVID-19\n0- CANCELAR OPERACAO\n1- negativo\n2- positivo-swab\n3- positivo-igM-igG\n4- positivo-igM\n5- positivo-igG')
    print('-' * 20)
    try:
        valResultadoTeste = int(input('RESULTADO DO TESTE: '))
    except:
        valResultadoTeste = -1
    while ((valResultadoTeste < 0) or (valResultadoTeste > 5)):
        print('!!!VALOR FORA DOS PARAMETROS!!!')
        try:
            valResultadoTeste = int(input('RESULTADO DO TESTE: '))
        except:
            valResultadoTeste = -1

    if ((valResultadoTeste == 0) or (valResultadoTeste == 1)):
        if (valResultadoTeste == 0):
            print('OPERACAO CANCELADA!')

    elif (valResultadoTeste == 2 or valResultadoTeste == 3 or valResultadoTeste == 4 or valResultadoTeste == 5):
        idade.append(entradaIdade)
        genero.append(valGenero)
        diaTeste.append(entradaDia)
        mesTeste.append(entradaMes)
        bairro.append(entradaBairro)
        qtdPessoasInfectadas = len(idade)
        listInfectados.append(opcoesResultado[valResultadoTeste - 1])
        infectados.append(qtdPessoasInfectadas - 1)
        statusInfectado.append(1)
        #bairro so entra uma unica vez(R5)
        bairrosInfectados.add(entradaBairro)

#cria os dicionarios que seram usados na R6 e R10
def historicoSemMes (historicoSemanasMeses,mesTeste,diaTeste,percentualSemanal):
    '''
    ESTA FUNCAO ADICIONA AOS DICIONARIOS DE HISTORICO DE SEMANAS E MESES A OCORRENCIA DE CASOS NAS RESPECTIVAS DATAS(SERA UTILIZADO NA R6 E R10)

    :param historicoSemanasMeses:  ira adicionar a este dicionario as datas e suas respectivas ocorrencias de infectados
    :param mesTeste:  ira chamar esta lista para utilizar os valores de meses registrados
    :param diaTeste:  ira chamar esta lista para utilizar os valores de dias registrados
    :param percentualSemanal:  ira adicionar a este dicionario as datas e suas respectivos percentuais de crescimento em infectados
    :return: retornara os dicionarios para serem utilizados nos demais requisitos(R6 e R10)
    '''
    if (len(mesTeste) != 0):

        semanaMes = 0
        for entradas in range(len(mesTeste)):
            entradaMes = mesTeste[entradas]
            entradaDia = diaTeste[entradas]

            if (entradaDia >= 1) and (entradaDia <= 7):
                semanaMes = 0
            elif (entradaDia >= 8) and (entradaDia <= 14):
                semanaMes = 1
            elif (entradaDia >= 15) and (entradaDia <= 21):
                semanaMes = 2
            elif (entradaDia >= 22) and (entradaDia <= 31):
                semanaMes = 3

            if (entradaMes not in historicoSemanasMeses):
                historicoSemanasMeses[entradaMes] = [0, 0, 0, 0]
                percentualSemanal[entradaMes] = [0, 0, 0, 0]

            dados = historicoSemanasMeses[entradaMes][semanaMes] + 1
            historicoSemanasMeses[entradaMes][semanaMes] = dados

        primeiroMes = (min(mesTeste))
        ultimoMes = (max(mesTeste)) + 1
        for incluso in range(primeiroMes, ultimoMes):
            if (incluso not in historicoSemanasMeses):
                historicoSemanasMeses[incluso] = [0, 0, 0, 0]
                percentualSemanal[incluso] = [0, 0, 0, 0]
    else:
        print('\n!!NAO HA PESSOAS CADASTRADAS!!\nPARA REGISTRAR PESSOAS ESCOLHA O REQUISITO 1\n')

#R2
def exibirListaInfectados(listInfectados,diaTeste,mesTeste,infectados,idade,genero,bairro,opcoesStatus,statusInfectado):
    '''
    ESTA FUNCAO IRA EXIBIR OS INFECTADOS PELA ORDEM DE TESTE (ID)

    :param listInfectados:  ira chamar esta lista com os tipos de testes usados
    :param diaTeste:  ira chamar esta lista com os dias de teste dos infectados
    :param mesTeste:  ira chamar esta lista com os meses de teste dos infectados
    :param infectados:  ira chamar esta lista com os ID's dos infectados
    :param idade:  ira chamar esta lista com as idades dos infectados
    :param genero: ira chamar esta lista com os generos dos infectados
    :param bairro: ira chamar esta lista com os bairros dos infectados
    :param opcoesStatus: ira chamar esta tupla para utilizar os dados de status definidos
    :param statusInfectado:  ira chamar esta lista com os valores de status dos infectados
    :return:  uma tabela contendo todos os dados dos infectados
    '''
    if len(listInfectados) == 0:
        print('\nNAO HA PESSOAS REGISTRADAS\n')
    else:
        print('\n\x1b[4;30;47m' + '|  ID  |  Idade  |  Genero  |  Data de Notificacao  |           Bairro          |      Metodo Aplicado    |' + '\x1b[0m')
        for x in range(len(listInfectados)):

            DT = ''
            MT = ''
            if (diaTeste[x] < 10):
                DT = '0'
            if (mesTeste[x] < 10):
                MT = '0'

            valSpaceID = 8 - (len(str(infectados[x])))
            leftID = int((valSpaceID - 1) / 2)
            rightID = int(leftID - 1)
            if (valSpaceID % 2 == 0):
                leftID = int(valSpaceID / 2)
                rightID = int(valSpaceID - leftID)

            # espaçamento idade
            valSpaceIdade = 9 - (len(str(idade[x])))
            leftIdade = int((valSpaceIdade - 1) / 2) + 1
            rightIdade = int(valSpaceIdade - leftIdade)
            if (valSpaceIdade % 2 == 0):
                leftIdade = int(valSpaceIdade / 2)
                rightIdade = int(valSpaceIdade - leftIdade)

            valSpaceGen = 10 - len(genero[x])
            leftGen = int((valSpaceGen - 1) / 2) + 1
            rightGen = int(valSpaceGen - leftGen)
            if (valSpaceGen % 2 == 0):
                leftGen = int(valSpaceGen / 2)
                rightGen = int(valSpaceGen - leftGen)

            valSpaceBai = 27 - (len(bairro[x]))
            leftBai = int((valSpaceBai - 1) / 2) + 1
            rightBai = int((valSpaceBai - leftBai))
            if (valSpaceBai % 2 == 0):
                leftBai = int(valSpaceBai / 2)
                rightBai = int(valSpaceBai - leftBai)

            valSpaceMet = 25 - (len(str(opcoesStatus[statusInfectado[x]])))
            leftMet = int((valSpaceMet - 1) / 2) + 1
            rightMet = int(valSpaceMet - leftMet)
            if (valSpaceMet % 2 == 0):
                leftMet = int(valSpaceMet / 2)
                rightMet = int(valSpaceMet - leftMet)


            valData = ('         {}{}/{}{}         '.format(DT, diaTeste[x], MT, mesTeste[x]))
            valPrint = '|{}{}{}|{}{}{}|{}{}{}|{}|{}{}{}|{}{}{}|'.format((' ' * leftID), infectados[x],(' ' * rightID), (' ' * leftIdade),idade[x], (' ' * rightIdade),(' ' * leftGen), genero[x],(' ' * rightGen), valData, (' ' * leftBai),bairro[x], (' ' * rightBai),(' ' * leftMet),opcoesStatus[statusInfectado[x]],(' ' * rightMet))
            if (statusInfectado[x] == 0):
                print('\x1b[4;30;42m' + str(valPrint) + '\x1b[0m')
            elif (statusInfectado[x] == 1):
                print('\x1b[4;30;46m' + str(valPrint) + '\x1b[0m')
            elif (statusInfectado[x] == 2):
                print('\x1b[4;30;43m' + str(valPrint) + '\x1b[0m')
            elif (statusInfectado[x] == 3):
                print('\x1b[4;30;41m' + str(valPrint) + '\x1b[0m')

            #print('\nID: {}\nIDADE: {}\nGENERO: {}\nDIA DO TESTE: {}{}\nMES DO TESTE: {}{}\nBAIRRO: {}\nRESULTADO DO TESTE DE COVID-19: {}\nSTATUS DO INFECTADO: {}\n'.format(infectados[x], idade[x], genero[x], DT, diaTeste[x], MT, mesTeste[x], bairro[x], listInfectados[x],opcoesStatus[statusInfectado[x]]))


#R3
def alterarStatusInfectados(opcoesStatus,infectados,diaTeste,mesTeste,statusInfectado,bairro,genero,idade):
    '''

    ESTA FUNCAO PERMITE ALTERAR O STATUS DE ALGUM INFECTADO QUE FOR SELCIONADO

    :param opcoesStatus:  ira chamar esta tupla para utilizar os dados de status definidos
    :param infectados:  ira chamar esta lista com os ID's dos infectados
    :param diaTeste:  ira chamar esta lista com os dias de teste dos infectados
    :param mesTeste:  ira chamar esta lista com os meses de teste dos infectados
    :param statusInfectado:   ira chamar esta lista com os valores de status dos infectados e possivelmente alterar valores
    :param bairro:  ira chamar esta lista com os bairros dos infectados
    :param genero:  ira chamar esta lista com os generos dos infectados
    :param idade:   ira chamar esta lista com as idades dos infectados
    :return:  primeiramente apresentara os dados do ID selecionado, perguntar se os estao corretos  e possivelmente modificar o status da pessoa
    '''
    try:
        infectadoBusca = int(input('\nDIGITE O ID DE BUSCA: '))
    except:
        infectadoBusca = -1
    while (infectadoBusca not in infectados):
        print('O ID NAO CORRESPONDE AOS DADOS REGISTRADOS, TENTE NOVAMENTE!')
        try:
            infectadoBusca = int(input('\nDIGITE O ID DE BUSCA: '))
        except:
            infectadoBusca = -1

    #esta parte ira manipular os valores e aplicar as devidas cores para entao exibi-las
    #espaçamento ID
    valSpaceID = 8 - (len(str(infectados[infectadoBusca])))
    leftID = int((valSpaceID - 1) / 2)
    rightID = int(leftID - 1)
    if (valSpaceID % 2 == 0):
        leftID = int(valSpaceID / 2)
        rightID = int(valSpaceID - leftID)

    #espaçamento idade
    valSpaceIdade = 9 - (len(str(idade[infectadoBusca])))
    leftIdade = int((valSpaceIdade - 1) / 2) + 1
    rightIdade = int(valSpaceIdade - leftIdade)
    if (valSpaceIdade % 2 == 0):
        leftIdade = int(valSpaceIdade / 2)
        rightIdade = int(valSpaceIdade - leftIdade)

    valSpaceGen = 10 - len(genero[infectadoBusca])
    leftGen = int((valSpaceGen - 1) / 2) + 1
    rightGen = int(valSpaceGen - leftGen)
    if (valSpaceGen % 2 == 0):
        leftGen = int(valSpaceGen / 2)
        rightGen = int(valSpaceGen - leftGen)

    valSpaceBai = 27 - (len(bairro[infectadoBusca]))
    leftBai = int((valSpaceBai - 1) / 2) + 1
    rightBai = int((valSpaceBai - leftBai))
    if (valSpaceBai % 2 == 0):
        leftBai = int(valSpaceBai / 2)
        rightBai = int(valSpaceBai - leftBai)

    valSpaceMet = 25 - (len(str(opcoesStatus[statusInfectado[infectadoBusca]])))
    leftMet = int((valSpaceMet - 1) / 2) + 1
    rightMet = int(valSpaceMet - leftMet)
    if (valSpaceMet % 2 == 0):
        leftMet = int(valSpaceMet / 2)
        rightMet = int(valSpaceMet - leftMet)

    DT = ''
    MT = ''
    if (diaTeste[infectadoBusca] < 10):
        DT = '0'
    if (mesTeste[infectadoBusca] < 10):
        MT = '0'

    print('\n\x1b[4;30;47m' + '|  ID  |  Idade  |  Genero  |  Data de Notificacao  |           Bairro          |      Metodo Aplicado    |' + '\x1b[0m')
    valData = ('         {}{}/{}{}         '.format(DT, diaTeste[infectadoBusca], MT, mesTeste[infectadoBusca]))
    valPrint = '|{}{}{}|{}{}{}|{}{}{}|{}|{}{}{}|{}{}{}|'.format((' ' * leftID),infectados[infectadoBusca],(' ' * rightID),(' ' * leftIdade),idade[infectadoBusca],(' ' * rightIdade),(' ' * leftGen),genero[infectadoBusca],(' ' * rightGen),valData,(' ' * leftBai),bairro[infectadoBusca],(' ' * rightBai),(' ' * leftMet),opcoesStatus[statusInfectado[infectadoBusca]],(' ' * rightMet))
    if (statusInfectado[infectadoBusca] == 0):
        print('\x1b[4;30;42m' + str(valPrint) + '\x1b[0m')
    elif (statusInfectado[infectadoBusca] == 1):
        print('\x1b[4;30;46m' + str(valPrint) + '\x1b[0m')
    elif (statusInfectado[infectadoBusca] == 2):
        print('\x1b[4;30;43m' + str(valPrint) + '\x1b[0m')
    elif (statusInfectado[infectadoBusca] == 3):
        print('\x1b[4;30;41m' + str(valPrint) + '\x1b[0m')

    valconfirmacao = input('Estes dados correspondem ao individuo procurado?\nS- sim\nN- nao\n>')
    confirmacao = valconfirmacao.upper()
    while(confirmacao != 'S' and confirmacao != 'N'):
        valconfirmacao = input('!!VAlOR DIGITADO ESTA FORA DOS PARAMETROS, TENTE NOVAMENTE!!\nEstes dados correspondem ao individuo procurado?\nS- sim\nN- nao\n>')
        confirmacao = valconfirmacao.upper()

    if (confirmacao == 'S'):

        print('STATUS DO PACIENTE\n0- CANCELAR OPERACAO\n1- Curado\n2- Isolamento domiciliar\n3- Internado\n4- Obito')
        valStatus = int(input('STATUS ATUAL DO INFECTADO: '))
        while ((valStatus < 0) or (valStatus > 4)):
            print('!!!VALOR FORA DOS PARAMETROS!!!')
            valStatus = int(input('DIGITE NOVAMENTE O STATUS ATUAL DO INFECTADO: '))

        if (valStatus == 0):
            print('OPERACAO CANCELADA')
        if (valStatus != 0):
            statusInfectado[infectadoBusca] = (valStatus - 1)
            print('\nSTATUS MODIFICADO COM SUCESSO!\n')


#R4
def listarInfectadoPorStatus(statusInfectado,listInfectados,diaTeste,mesTeste,infectados,idade,genero,bairro,opcoesStatus):
    '''

    ESTA FUNCAO IRA EXIBIR OS DADOS DOS INFECTADOS CONFORME O STATUS DESEJADO

    :param statusInfectado:  ira chamar esta lista com os valores de status dos infectados e possivelmente alterar valores
    :param listInfectados:  ira chamar esta lista com os tipos de testes usados
    :param diaTeste: ira chamar esta lista com os dias de teste dos infectados
    :param mesTeste:  ira chamar esta lista com os meses de teste dos infectados
    :param infectados:  ira chamar esta lista com os ID's dos infectados
    :param idade:   ira chamar esta lista com as idades dos infectados
    :param genero:   ira chamar esta lista com as generos dos infectados
    :param bairro:   ira chamar esta lista com os bairros dos infectados
    :param opcoesStatus:  ira chamar esta tupla para utilizar os dados de status definidos
    :return:  apresentara uma tabela contendo todos os dados das pessoas que estao com o status procurado
    '''
    copyStatusinfectados = statusInfectado.copy()
    if (len(listInfectados) == 0):
        print('\nNAO HA PESSOAS REGISTRADAS\n')

    else:
        print('\nSTATUS DE BUSCA\n0- CANCELAR OPERACAO\n1- Curado\n2- Isolamento domiciliar\n3- Internado\n4- Obito')
        statusBusca = int(input('DIGITE O STATUS DE BUSCA: '))
        while (statusBusca > 5) or (statusBusca < 0):
            print('!!!VALOR FORA DOS PARAMETROS!!!')
            statusBusca = int(input('DIGITE NOVAMENTE O STATUS DE BUSCA: '))
        if (statusInfectado.count(statusBusca - 1) == 0):
            print('\n!!!NAO HA PESSOAS REGISTRADAS COM O STATUS PROCURADO!!!\n')

        else:
            print('\n\x1b[4;30;47m' + '|  ID  |  Idade  |  Genero  |  Data de Notificacao  |           Bairro          |      Metodo Aplicado    |' + '\x1b[0m')
            for exibir in range(statusInfectado.count(statusBusca - 1)):
                indexInfectado = copyStatusinfectados.index(statusBusca - 1)
                copyStatusinfectados[indexInfectado] = 'removed'
                DT = ''
                MT = ''
                if (diaTeste[indexInfectado] < 10):
                    DT = '0'
                if (mesTeste[indexInfectado] < 10):
                    MT = '0'

                valSpaceID = 8 - (len(str(infectados[indexInfectado])))
                leftID = int((valSpaceID - 1) / 2)
                rightID = int(leftID - 1)
                if (valSpaceID % 2 == 0):
                    leftID = int(valSpaceID / 2)
                    rightID = int(valSpaceID - leftID)

                # espaçamento idade
                valSpaceIdade = 9 - (len(str(idade[indexInfectado])))
                leftIdade = int((valSpaceIdade - 1) / 2) + 1
                rightIdade = int(valSpaceIdade - leftIdade)
                if (valSpaceIdade % 2 == 0):
                    leftIdade = int(valSpaceIdade / 2)
                    rightIdade = int(valSpaceIdade - leftIdade)

                valSpaceGen = 10 - len(genero[indexInfectado])
                leftGen = int((valSpaceGen - 1) / 2) + 1
                rightGen = int(valSpaceGen - leftGen)
                if (valSpaceGen % 2 == 0):
                    leftGen = int(valSpaceGen / 2)
                    rightGen = int(valSpaceGen - leftGen)

                valSpaceBai = 27 - (len(bairro[indexInfectado]))
                leftBai = int((valSpaceBai - 1) / 2) + 1
                rightBai = int((valSpaceBai - leftBai))
                if (valSpaceBai % 2 == 0):
                    leftBai = int(valSpaceBai / 2)
                    rightBai = int(valSpaceBai - leftBai)

                valSpaceMet = 25 - (len(str(opcoesStatus[statusInfectado[indexInfectado]])))
                leftMet = int((valSpaceMet - 1) / 2) + 1
                rightMet = int(valSpaceMet - leftMet)
                if (valSpaceMet % 2 == 0):
                    leftMet = int(valSpaceMet / 2)
                    rightMet = int(valSpaceMet - leftMet)

                valData = ('         {}{}/{}{}         '.format(DT, diaTeste[indexInfectado], MT, mesTeste[indexInfectado]))
                valPrint = '|{}{}{}|{}{}{}|{}{}{}|{}|{}{}{}|{}{}{}|'.format((' ' * leftID), infectados[indexInfectado],(' ' * rightID), (' ' * leftIdade),idade[indexInfectado], (' ' * rightIdade),(' ' * leftGen), genero[indexInfectado],(' ' * rightGen), valData, (' ' * leftBai),bairro[indexInfectado], (' ' * rightBai),(' ' * leftMet), opcoesStatus[statusInfectado[indexInfectado]],(' ' * rightMet))
                if (statusInfectado[indexInfectado] == 0):
                    print('\x1b[4;30;42m' + str(valPrint) + '\x1b[0m')
                elif (statusInfectado[indexInfectado] == 1):
                    print('\x1b[4;30;46m' + str(valPrint) + '\x1b[0m')
                elif (statusInfectado[indexInfectado] == 2):
                    print('\x1b[4;30;43m' + str(valPrint) + '\x1b[0m')
                elif (statusInfectado[indexInfectado] == 3):
                    print('\x1b[4;30;41m' + str(valPrint) + '\x1b[0m')


#R5
def calcularBairrosMaisInfectados(bairro,bairrosInfectados,bairrosMaisInfectados):
    '''

    :param bairro:  ira chamar esta lista com os bairros dos infectados
    :param bairrosInfectados:  ira chamar este set contendo os bairros dos infectados (que contem os nomes dos bairros uma unica vez)
    :param bairrosMaisInfectados: ira adicionar a esta lista a quantidade de vezes que houveram casos em determinado bairro
    :return:  ira exibir uma tabela contendo em ordem decrescente o percentual de ocorrencia dos bairros registrados
    '''
    qtdCasosTotal = len(bairro)

    for entradaListaCB in bairrosInfectados:
        bairrosMaisInfectados[entradaListaCB] = bairro.count(entradaListaCB)

    from operator import itemgetter
    ordered = dict(reversed(sorted(bairrosMaisInfectados.items(), key=itemgetter(1))))
    #print(ordered)
    print('\n\x1b[4;30;47m' + '|           Bairro          |   Qtd.   |     %     |' + '\x1b[0m')
    for percent in ordered:
        percentual = ((100 / qtdCasosTotal) * bairrosMaisInfectados[percent])
        dados = (bairrosMaisInfectados[percent], percentual)
        bairrosMaisInfectados[percent] = dados

        totalB = 27 - len(percent)
        leftB = int((totalB - 1) / 2) + 1
        rightB = int(totalB - leftB)
        if (totalB % 2 == 0):
            leftGen = int(totalB / 2)
            rightGen = int(totalB - leftGen)

        totalQ = 10 - len(str(bairrosMaisInfectados[percent][0]))
        leftQ = int((totalQ - 1) / 2) + 1
        rightQ = int(totalQ - leftQ)
        if (totalQ % 2 == 0):
            leftQ = int(totalQ / 2)
            rightQ = int(totalQ - leftQ)

        totalP = 10 - len(str('%.2f' %bairrosMaisInfectados[percent][1]))
        leftP = int((totalP - 1) / 2) + 1
        rightP = int(totalP - leftP)
        if (totalP % 2 == 0):
            leftP = int(totalP / 2)
            rightP = int(totalP - leftP)

        itemPrint = ('|{}{}{}|{}{}{}|{}{}%{}|').format((' ' * leftB),percent,(' ' * rightB),(' ' * leftQ),bairrosMaisInfectados[percent][0],(' ' * rightQ),(' ' * leftP),'%.2f' %bairrosMaisInfectados[percent][1],(' ' * rightP))
        print('\x1b[4;30;44m' + str(itemPrint) + '\x1b[0m')
    print('\n')


#R6
#perguntar quanto a quantidade de semanas por mes se esta realmente correto
def taxaCrescimenoPorSemana(historicoSemanasMeses,percentualSemanal,mesTeste):
    '''

    ESTA FUNCAO IRA CALCULAR E EXIBIR O VALOR PERCENTUAL DO CRESCIMENTO DE CASOS SEMANALMENTE

    :param historicoSemanasMeses:  ira chamar este dicionario e utilizar as datas e suas respectivas ocorrencias de infectados semanais
    :param percentualSemanal:  ira chamar este dicionario e modificar os valores(antes igual a zero) para os valores percentuais de crescimento em casos
    :param mesTeste:  ira chamar esta lista com os meses de teste dos infectados
    :return: ira exibir uma tabela contendo todas as semanas de todos os meses cadastrados e seus respectivos percentuais de crescimento em casos
    '''
    if (len(mesTeste) != 0):
        primeiroMes = (min(mesTeste))
        ultimoMes = (max(mesTeste)) + 1
        total = 0
        for calcPercen in range(primeiroMes, ultimoMes):
            for quad in range(4):
                calculo = 0
                crescimentoSemana = historicoSemanasMeses[calcPercen][quad]
                if ((crescimentoSemana != 0) and (total != 0)):
                    calculo = (100 / total) * crescimentoSemana

                total = total + crescimentoSemana
                percentualSemanal[calcPercen][quad] = calculo

        print('\n\x1b[4;30;47m' + '|        Semana/Mes        |    Aumento dos Casos%    |' + '\x1b[0m')
        for exib in range(primeiroMes, ultimoMes):
            for other in range(4):

                semanMes = ('{}/{}').format(other + 1,exib)

                totalSM = 26 - len(str(semanMes))
                leftSM = int((totalSM - 1) / 2) + 1
                rightSM = int(totalSM - leftSM)
                if (totalSM % 2 == 0):
                    leftSM = int(totalSM / 2)
                    rightSM = int(totalSM - leftSM)


                totalAC = 25 - len(str('%.2f' %percentualSemanal[exib][other]))
                leftAC = int((totalAC - 1) / 2) + 1
                rightAC = int(totalAC - leftAC)
                if (totalAC % 2 == 0):
                    leftAC = int(totalAC / 2)
                    rightAC = int(totalAC - leftAC)

                percVal = ('%.2f' %percentualSemanal[exib][other])
                itemCasSem = ('|{}{}{}|{}{}%{}|').format((' ' * leftSM), str(semanMes), (' ' * rightSM), (' ' * leftAC),percVal, (' ' * rightAC))
                print('\x1b[4;30;44m' + str(itemCasSem) + '\x1b[0m')

#R7
def percentualMascFem(genero):
    '''

    IRA CALCULAR O PERCENTUAL DE HOMENS E MULHERES INFECTADOS

    :param genero:  ira chamar esta lista com as generos dos infectados, ler e calcular quantas vezes se repetem
    :return: ira exibir uma tabela contendo o valor em percentual de homens e mulheres em relacao ao total
    '''
    if (len(genero) > 0):
        totalGeneros = len(genero)
        totalMasc = genero.count('masc.')
        totalFem = genero.count('fem.')

        calculoMasc = (100 / totalGeneros) * (totalMasc)
        calculoFem = (100 / totalGeneros) * (totalFem)

        print('\x1b[4;30;47m' + '|   HOMENS   |   MULHERES   |' + '\x1b[0m')  # print do titulo

        totalH = 11 - len(str("%.2f" %calculoMasc))
        leftH = int((totalH - 1) / 2) + 1
        rightH = int(totalH - leftH)
        if (totalH % 2 == 0):
            leftH = int(totalH / 2)
            rightH = int(totalH - leftH)

        totalM = 13 - len(str("%.2f" %calculoFem))
        leftM = int((totalM - 1) / 2) + 1
        rightM = int(totalM - leftM)
        if (totalM % 2 == 0):
            leftM = int(totalM / 2)
            rightM = int(totalM - leftM)

        printPercenHM = ('|{}{:.2f}%{}|{}{:.2f}%{}|').format((' ' * leftH),calculoMasc, (' ' * rightH), (' ' * leftM),calculoFem, (' ' * rightM))
        print('\x1b[4;30;44m' + str(printPercenHM) + '\x1b[0m')

    else:
        print('!!!NAO HA PESSOAS CADASTRADAS!!!\nCadastre pessoas para poder utilizar este requisito')


#R8
def percentualFaixaEtaria(idade):
    '''

    ESTA FUNCAO IRA CALCULAR O PERCENTUAL DE PESSOAS EM DETERMINADA FAIXA ETARIA

    :param idade:  ira chamar esta lista com as idades dos infectados para calcular em que faixa etaria a pessoa esta
    :return: ira exibir uma tabela contendo as faixas de idade e seus respectivos percentuais de pessoas nela
    '''
    faixas = ('0 e 10','11 e 20','21 e 40','41 e 60','61 e 80','80')
    idadesFaixa = {'zeroDez': 0,'onzeVinte': 0,'vinteumQuarenta': 0,'quarenUmSessenta': 0,'sessenUmOitenta': 0,'maisOitenta': 0}
    percenIdades = {'zeroDez': 0,'onzeVinte': 0,'vinteumQuarenta': 0,'quarenUmSessenta': 0,'sessenUmOitenta': 0,'maisOitenta': 0}
    totalIdade = len(idade)

    for testIdade in range(totalIdade):

        if ((idade[testIdade] >= 0) and (idade[testIdade] <= 10)):
            idadesFaixa['zeroDez'] = (idadesFaixa['zeroDez'] + 1)
        if ((idade[testIdade] >= 11) and (idade[testIdade] <= 20)):
            idadesFaixa['onzeVinte'] = (idadesFaixa['onzeVinte'] + 1)
        if ((idade[testIdade] >= 21) and (idade[testIdade] <= 40)):
            idadesFaixa['vinteumQuarenta'] = (idadesFaixa['vinteumQuarenta'] + 1)
        if ((idade[testIdade] >= 41) and (idade[testIdade] <= 60)):
            idadesFaixa['quarenUmSessenta'] = (idadesFaixa['quarenUmSessenta'] + 1)
        if ((idade[testIdade] >= 61) and (idade[testIdade] <= 80)):
            idadesFaixa['sessenUmOitenta'] = (idadesFaixa['sessenUmOitenta'] + 1)
        if ((idade[testIdade] > 80) and (idade[testIdade] <= 150)):
            idadesFaixa['maisOitenta'] = (idadesFaixa['maisOitenta'] + 1)

    for calc in idadesFaixa:

        percen = (100 / totalIdade) * (idadesFaixa[calc])
        percenIdades[calc] = percen

    print('\n\x1b[4;30;47m' + '|   FAIXAS DE IDADE   |    %    |' + '\x1b[0m')
    fase = 0
    for exibir in percenIdades:

        totalIdade = 16 - len(faixas[fase])
        leftIdade = int((totalIdade - 1) / 2) + 1
        rightIdade = int(totalIdade - leftIdade)
        if (totalIdade % 2 == 0):
            leftIdade = int(totalIdade / 2)
            rightIdade = int(totalIdade - leftIdade)

        totalPercen = 8 - len(str(('{:.2f}').format(percenIdades[exibir])))
        leftPercen = int((totalPercen - 1) / 2) + 1
        rightPercen = int(totalPercen - leftPercen)
        if (totalPercen % 2 == 0):
            leftPercen = int(totalPercen / 2)
            rightPercen = int(totalPercen - leftPercen)


        itemIdade = ('|{}{} anos{}|{}{:.2f}%{}|').format((' '*leftIdade),faixas[fase],(' '*rightIdade),(' '*leftPercen),percenIdades[exibir],(' '*rightPercen))
        print('\x1b[4;30;45m' + str(itemIdade) + '\x1b[0m')
        fase += 1

#R9
def percentualCurados(statusInfectado):
    '''

    ESTA FUNCAO IRA CALCULAR O PERCENTUAL DE CURADOS EM RELACAO AO TOTAL DE INFECTADOS

    :param statusInfectado:  ira chamar esta lista com os valores de status dos infectados, ler e calcular o percentual de curados
    :return:  ira exibir uma tabela contendo o valor em percentual de pessoas curadas
    '''

    totalInfect = len(statusInfectado)
    totalCurados = statusInfectado.count(0)
    percentDeCurados = (100 / totalInfect) * (totalCurados)


    totalPC = 22 - len(str('%.2f' %percentDeCurados))
    leftPC = int((totalPC - 1) / 2) + 1
    rightPC = int(totalPC - leftPC)
    if (totalPC % 2 == 0):
        leftPC = int(totalPC / 2)
        rightPC = int(totalPC - leftPC)

    itemUCura = ('\x1b[4;30;47m' + '| PERCENTUAL DE CURADOS |' + '\x1b[0m')
    itemDCura = ('\x1b[4;30;44m' + '|{}{}%{}|'.format((' '*leftPC),'%.2f' %percentDeCurados,(' '*rightPC)) + '\x1b[0m')
    print('\n')
    print(itemUCura)
    print(itemDCura,'\n')

#R10
def graficoEvolucaoInfectados(historicoSemanasMeses,mesTeste):
    '''

    ESTA FUNCAO IRA EXIBIR UMA GRAFICO INDICANDO O CRESCIMENTO AO LONGO DAS SEMANAS QUE FORAM REGISTRADAS

    :param historicoSemanasMeses:  ira chamar este dicionario e utilizar as datas e suas respectivas ocorrencias de infectados
    :param mesTeste:  ira chamar esta lista contendo os meses que foram registrados e calcular o primeiro e ultimo mes que foram registrados
    :return:  ira exibir um grafico demonstrando o quanto cresceu semanalmente ao longo dos meses registrados
    '''

    import matplotlib.pyplot as plt
    if(len(mesTeste) != 0):
        casosAcumulados = [0]
        indicadoSemMes = list()
        leitura = len(historicoSemanasMeses) + 1
        primeiroMes = (min(mesTeste))
        ultimoMes = max(mesTeste) + 1

        totalSemanas = 1
        for contagemCasos in range(primeiroMes,ultimoMes):
            for seman in range(4):
                valCasosAcumulados = historicoSemanasMeses[contagemCasos][seman] + casosAcumulados[len(casosAcumulados) - 1]
                casosAcumulados.append(valCasosAcumulados)
                valIndicadoSemMes = ('{}'.format(totalSemanas))
                indicadoSemMes.append(valIndicadoSemMes)
                totalSemanas += 1

        print('\nPREPARANDO GRAFICO...\n')

        casosAcumulados.remove(0)
        plt.plot(indicadoSemMes, casosAcumulados)

        plt.ylabel('Quantidade de casos acumulados')
        plt.xlabel('Semanas desde a primeira infeccao')
        plt.show()










