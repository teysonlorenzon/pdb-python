#menu Principal

quer_jogar = input("Deseja iniciar o jogo King's Game? (sim/nao): ")


if(quer_jogar.lower() == "sim"):

    personagens = open("personagens.txt", "r")
    lista_personagens = personagens.read().split("\n")


    print("******************************************************************************************************")
    print("*                                            KING'S Game                                             *")
    print("******************************************************************************************************")
    print("*                                                                                                    *")
    print("*                       Escolha o numero referente a quatidade de jogadores                          *")
    print("*                                                                                                    *")
    print("*                               (2): 2 Jogadores  (4): 4 Jogadores                                   *")
    print("*                               (3): 3 Jogadores  (5): 5 Jogadores                                   *")
    print("*                                                                                          (1): Sair *")
    print("*----------------------------------------------------------------------------------------------------*")
    print("*                                               Regras                                               *")
    print("* 1) Digite o nome dos jogadores                                                                     *")
    print("* 2) Escolha os personagens                                                                          *")
    print("* 3) Os dois melhores jogadores, se enfrentam na final                                               *")
    print("******************************************************************************************************")


    numero_jogadores = int(input("Digite o numero referente a quantidade de jogadores (2 a 5) (1 para sair): "))
    while (numero_jogadores < 1 or numero_jogadores > 5):
        numero_jogadores = int(input("Respeite os numeros do menu (1 a 5): "))

    jogadores = []

    if (numero_jogadores == 1):
        print("Jogo encerrado!")

    elif (numero_jogadores == 2):
        for i in range(1,3):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador.lower())

    elif (numero_jogadores == 3):
        for i in range(1,4):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador.lower())


    elif (numero_jogadores == 4):
        for i in range(1,5):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador.lower())

    elif (numero_jogadores == 5):
        for i in range(1,6):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador.lower())


    print()
    #escolhendo os Personagens

    print("******************************************************************************************************")
    print("*                                            Personagens                                             *")
    print("******************************************************************************************************")
    print("*                                                                                                    *")
    print("*                               (1): {0}  (3): {1}                                            *".format(lista_personagens[0],lista_personagens[1]))
    print("*                               (2): {0}   (4): {1}                                          *".format(lista_personagens[2],lista_personagens[3]))
    print("*                                                                                                    *")
    print("******************************************************************************************************")

    escolhas = {}

    for i  in range(len(jogadores)):
        numero_lutador = int(input("{0}, escolha um numero referente ao perssonagem(1 a 4): ".format(jogadores[i].title())))
        while(numero_lutador < 1 or numero_lutador > 4):
            numero_lutador = int(input("{0}, escolha um numero entre(1 a 4): ".format(jogadores[i].title())))
        if(numero_lutador == 1):
            lutador = lista_personagens[0]
            escolhas[jogadores[i]] = lutador
        elif (numero_lutador == 2):
            lutador = lista_personagens[2]
            escolhas[jogadores[i]] = lutador
        elif (numero_lutador == 3):
            lutador = lista_personagens[1]
            escolhas[jogadores[i]] = lutador
        elif (numero_lutador == 4):
            lutador = lista_personagens[3]
            escolhas[jogadores[i]] = lutador

    print()
    for i in range(len(jogadores)):
        print("Otima escolha {0}, você agora é um {1}".format(jogadores[i].title(), escolhas[jogadores[i]]))


    print()

    print(" Ha muito tempo, um necromante muito poderoso chamado Tarzariuz que tinha um conhecimento muito maior que")
    print("qualquer outro necromante ou mago já existente na terra estava no caminho de se tornar um Lich e dar ")
    print("continuação a suas pesquisas malévolas. Então ele pediu a ajuda de seus três discípulos para auxiliá-lo ")
    print("no ritual de transformação, Kanin, Trasdan e o mais poderoso dos três, Dantis deixando assim sua filactéria")
    print("imune a ataques magico e imune a ataques físicos. Juntos completaram o ritual.")
    print(" O mundo caiu em trevas , e assim iniciou uma batalha pelo poder ,o primeiro a conquitar o titulo seria o rei")
    print("com o poder de mudar o mundo para melhor")

    print()


    if(numero_jogadores == 2):

        print("******************************************************************************************************")
        print("*                                          Tabela Lutas                                              *")
        print("******************************************************************************************************")
        print(" luta 1                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))

    elif(numero_jogadores == 3):

        print("******************************************************************************************************")
        print("*                                          Tabela Lutas                                              *")
        print("******************************************************************************************************")
        print(" luta 1                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 2                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 3                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" final                                Ganhador 1 x Ganhador 2")

    elif(numero_jogadores == 4):

        print("******************************************************************************************************")
        print("*                                          Tabela Lutas                                              *")
        print("******************************************************************************************************")
        print(" luta 1                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 2                                {0}({1}) x {2}({3})".format(jogadores[2].title(),escolhas[jogadores[2]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 3                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 4                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 5                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 6                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" final                                Ganhador 1 x Ganhador 2")

    elif(numero_jogadores == 5):

        print("******************************************************************************************************")
        print("*                                          Tabela Lutas                                              *")
        print("******************************************************************************************************")
        print(" luta 1                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 2                                {0}({1}) x {2}({3})".format(jogadores[2].title(),escolhas[jogadores[2]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 3                                {0}({1}) x {2}({3})".format(jogadores[4].title(),escolhas[jogadores[4]],jogadores[0].title(),escolhas[jogadores[0]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 4                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 5                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 6                                {0}({1}) x {2}({3})".format(jogadores[4].title(),escolhas[jogadores[4]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 7                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 8                                {0}({1}) x {2}({3})".format(jogadores[2].title(),escolhas[jogadores[2]],jogadores[0].title(),escolhas[jogadores[0]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 9                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[4].title(),escolhas[jogadores[4]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 10                               {0}({1}) x {2}({3})".format(jogadores[4].title(),escolhas[jogadores[4]],jogadores[3].title(),escolhas[jogadores[3]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" final                                Ganhador 1 x Ganhador 2")
