import random

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
    print("*                                         (1): 1 Jogador                                             *")
    print("*                               (2): 2 Jogadores  (4): 4 Jogadores                                   *")
    print("*                               (3): 3 Jogadores  (5): 5 Jogadores                                   *")
    print("*                                                                                          (6): Sair *")
    print("*----------------------------------------------------------------------------------------------------*")
    print("*                                               Regras                                               *")
    print("* 1) Digite o nome dos jogadores                                                                     *")
    print("* 2) Escolha os personagens                                                                          *")
    print("* 3) Os dois melhores jogadores, se enfrentam na final                                               *")
    print("******************************************************************************************************")

    numero_jogadores = int(input("Digite o numero referente a quantidade de jogadores (1 a 5) (6 para sair): "))
    while (numero_jogadores < 1 or numero_jogadores > 5):
        numero_jogadores = int(input("Respeite os numeros do menu (1 a 6): "))

    jogadores = []

    if (numero_jogadores == 1):
            jogador = input("Jogador 1: ")
            jogadores.append(jogador.lower())


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
    elif (numero_jogadores == 6):
        print("Fim de Jogo")



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
    pontos = {}
    vida = {}
    sequencia_lutas = {}

    poderes = {
        lista_personagens[0]: "Fisico,Massacre,Desafio da Morte,Carga Concentrada",
        lista_personagens[1]: "Fisico,Bola de Fogo,Relampago,Ultra Colapso",
        lista_personagens[2]: "Fisico,Flexa Critica,Flexa Envenenada,Flexa da Morte",
        lista_personagens[3]: "Fisico,Cajado de Veneno,Chuva de Gelo,Morte Lenta"
    }

    dano = {
        "Fisico": 5,
        "Massacre": 10,
        "Desafio da Morte": 10,
        "Carga Concentrada": 10,
        "Bola de Fogo": 10,
        "Relampago": 10,
        "Ultra Colapso": 10,
        "Flexa Critica": 10,
        "Flexa Envenenada": 10,
        "Flexa da Morte": 10,
        "Cajado de Veneno": 10,
        "Chuva de Gelo": 10,
        "Morte Lenta": 10,
        "Destruidor de Mundos": 10,
        "Demolição Paranormal": 10,
        "Mundo Abominavel": 10
    }



    for i in range(len(jogadores)):
        numero_lutador = int(input("{0}, escolha um numero referente ao perssonagem(1 a 4): ".format(jogadores[i].title())))
        while(numero_lutador < 1 or numero_lutador > 4):
            numero_lutador = int(input("{0}, escolha um numero entre(1 a 4): ".format(jogadores[i].title())))
        if(numero_lutador == 1):
            lutador = lista_personagens[0]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 70
        elif (numero_lutador == 2):
            lutador = lista_personagens[2]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 70
        elif (numero_lutador == 3):
            lutador = lista_personagens[1]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 70
        elif (numero_lutador == 4):
            lutador = lista_personagens[3]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 70


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


    def criar_senario_luta(contra_x, contra_y, numero_luta):

        print(
            "******************************************************************************************************")
        print(
            "*                                          Tabela Lutas                                              *")
        print(
            "******************************************************************************************************")
        print()
        print(" luta {0}                                {1}({2}) x {3}({4})".format(contador, jogadores[
            sequencia_lutas[contra_x]].title(), escolhas[jogadores[sequencia_lutas[contra_x]]], jogadores[
                                                                                        sequencia_lutas[
                                                                                            contra_y]].title(),
                                                                                    escolhas[jogadores[
                                                                                        sequencia_lutas[contra_y]]]))
        print()
        print(
            "******************************************************************************************************")
        print()
        print("Batalha - {0}({1}) x {2}({3})".format(jogadores[sequencia_lutas[contra_x]].title(),
                                                     escolhas[jogadores[sequencia_lutas[contra_x]]],
                                                     jogadores[sequencia_lutas[contra_y]].title(),
                                                     escolhas[jogadores[sequencia_lutas[contra_y]]]))

        print("Batalha {0}".format(numero_luta))
        print("Lutem!")

        poder_jogador_um = poderes[escolhas[jogadores[sequencia_lutas[contra_x]]]].split(",")
        poder_jogador_dois = poderes[escolhas[jogadores[sequencia_lutas[contra_y]]]].split(",")

        gurdar_ataque_jogador_um = []
        gurdar_ataque_jogador_dois = []

        pontos_de_vida_um = 1
        pontos_de_vida_dois = 1

        termina = 1

        while (termina != 0):
            print(
                "------------------------------------------------------------------------------------------------------")
            print("Escolha uma opção de ataque para causar dano ao {0}".format(
                escolhas[jogadores[sequencia_lutas[contra_y]]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0], poder_jogador_um[1], poder_jogador_um[2],
                                                    poder_jogador_um[3]))
            print()

            ataque_jogador_um = int(
                input(
                    "{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_x]].title())))
            ataque_jogador_um = ataque_jogador_um - 1

            while (ataque_jogador_um in gurdar_ataque_jogador_um):
                ataque_jogador_um = int(
                    input("{0} digite um ataque disponivel: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                ataque_jogador_um = ataque_jogador_um - 1

            ataque = poder_jogador_um[ataque_jogador_um]

            dano_jogador_um = dano[ataque]
            vida_jogador_dois = vida[jogadores[sequencia_lutas[contra_y]]]
            dano_critico = 0

            if (ataque == poder_jogador_um[0]):
                critico = random.randint(1, 20)
                if (critico > 18):
                    dano_critico = dano_jogador_um + 10
                    vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_critico
                    print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                        jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[0], dano_critico,
                        jogadores[sequencia_lutas[contra_y]].title()))
                else:
                    vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_jogador_um
                    print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                        jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[0], dano_jogador_um,
                        jogadores[sequencia_lutas[contra_y]].title()))

            if (ataque_jogador_um > 0 and "Utilizado" not in poder_jogador_um[ataque_jogador_um]):
                gurdar_ataque_jogador_um.append(ataque_jogador_um)

                if (ataque == poder_jogador_um[1]):
                    critico = random.randint(1, 20)
                    if (critico > 16):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                                jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[1], dano_critico,
                                jogadores[sequencia_lutas[contra_y]].title()))
                    else:
                        vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[1], dano_jogador_um,
                            jogadores[sequencia_lutas[contra_y]].title()))

                elif (ataque == poder_jogador_um[2]):
                    critico = random.randint(1, 20)
                    if (critico > 12):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                                jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[2], dano_critico,
                                jogadores[sequencia_lutas[contra_y]].title()))
                    else:
                        vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[2], dano_jogador_um,
                            jogadores[sequencia_lutas[contra_y]].title()))

                elif (ataque == poder_jogador_um[3]):
                    critico = random.randint(1, 20)
                    if (critico > 10):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                                jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[3], dano_critico,
                                jogadores[sequencia_lutas[contra_y]].title()))
                    else:
                        vida[jogadores[sequencia_lutas[contra_y]]] = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[sequencia_lutas[contra_x]].title(), poder_jogador_um[3], dano_jogador_um,
                            jogadores[sequencia_lutas[contra_y]].title()))

                poder_jogador_um[ataque_jogador_um] = "Utilizado"

            print()
            print(
                "------------------------------------------------------------------------------------------------------")

            print("Escolha uma opção de ataque para causar dano ao {0}".format(
                escolhas[jogadores[sequencia_lutas[contra_x]]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0], poder_jogador_dois[1],
                                                    poder_jogador_dois[2], poder_jogador_dois[3]))
            print()

            ataque_jogador_dois = int(
                input("{0} digite um numero referente ao ataque: ".format(
                    escolhas[jogadores[sequencia_lutas[contra_y]]].title())))
            ataque_jogador_dois = ataque_jogador_dois - 1

            while (ataque_jogador_dois in gurdar_ataque_jogador_dois):
                ataque_jogador_dois = int(input(
                    "{0} digite um ataque disonivel: ".format(escolhas[jogadores[sequencia_lutas[contra_y]]].title())))
                ataque_jogador_dois = ataque_jogador_dois - 1

            ataque = poder_jogador_dois[ataque_jogador_dois]

            dano_jogador_dois = dano[ataque]
            vida_jogador_um = vida[jogadores[sequencia_lutas[contra_x]]]
            dano_critico = 0

            if (ataque == poder_jogador_dois[0]):
                critico = random.randint(1, 20)
                if (critico > 18):
                    dano_critico = dano_jogador_um + 10
                    vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_critico
                    print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                        jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[0], dano_critico,
                        jogadores[sequencia_lutas[contra_x]].title()))
                else:
                    vida[jogadores[0]] = vida_jogador_um - dano_jogador_dois
                    print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                        jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[0], dano_jogador_dois,
                        jogadores[sequencia_lutas[contra_x]]))

            if (ataque_jogador_dois > 0 and "Utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                gurdar_ataque_jogador_dois.append(ataque_jogador_dois)

                if (ataque == poder_jogador_dois[1]):
                    critico = random.randint(1, 20)
                    if (critico > 16):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                                jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[1], dano_critico,
                                jogadores[sequencia_lutas[contra_x]].title()))
                    else:
                        vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_jogador_dois
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[1], dano_jogador_dois,
                            jogadores[sequencia_lutas[contra_x]].title()))

                elif (ataque == poder_jogador_dois[2]):
                    critico = random.randint(1, 20)
                    if (critico > 12):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                                jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[2], dano_critico,
                                jogadores[sequencia_lutas[contra_x]].title()))
                    else:
                        vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_jogador_dois
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[3], dano_jogador_dois,
                            jogadores[sequencia_lutas[contra_x]].title()))

                elif (ataque == poder_jogador_dois[3]):
                    critico = random.randint(1, 20)
                    if (critico > 10):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                                jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[3], dano_critico,
                                jogadores[sequencia_lutas[contra_x]].title()))
                    else:
                        vida[jogadores[sequencia_lutas[contra_x]]] = vida_jogador_um - dano_jogador_dois
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[sequencia_lutas[contra_y]].title(), poder_jogador_dois[3], dano_jogador_dois,
                            jogadores[sequencia_lutas[contra_x]].title()))

                poder_jogador_dois[ataque_jogador_dois] = "Utilizado"

            pontos_de_vida_um = vida[jogadores[sequencia_lutas[contra_x]]]
            pontos_de_vida_dois = vida[jogadores[sequencia_lutas[contra_y]]]

            print(
                "------------------------------------------------------------------------------------------------------")
            if (pontos_de_vida_um <= 0 and pontos_de_vida_dois <= 0):
                print("Empatou")
                print("Jogue novamente para desempatar")
                poder_jogador_um = poderes[escolhas[jogadores[sequencia_lutas[contra_x]]]].split(",")
                poder_jogador_dois = poderes[escolhas[jogadores[sequencia_lutas[contra_y]]]].split(",")

                gurdar_ataque_jogador_um = []
                gurdar_ataque_jogador_dois = []

                pontos_de_vida_um = 0
                pontos_de_vida_dois = 0

                vida[jogadores[sequencia_lutas[contra_x]]] = 70
                vida[jogadores[sequencia_lutas[contra_y]]] = 70

                termina = 1

            elif (pontos_de_vida_um <= 0):
                vida[jogadores[sequencia_lutas[contra_x]]] = 70
                vida[jogadores[sequencia_lutas[contra_y]]] = 70
                pontos[jogadores[sequencia_lutas[contra_y]]] = pontos[jogadores[sequencia_lutas[contra_x]]] + 100
                pontos_de_vida_um = 0
                termina = 0
            elif (pontos_de_vida_dois <= 0):
                vida[jogadores[sequencia_lutas[contra_x]]] = 70
                vida[jogadores[sequencia_lutas[contra_y]]] = 70
                pontos[jogadores[sequencia_lutas[contra_x]]] = pontos[jogadores[sequencia_lutas[contra_y]]] + 100
                pontos_de_vida_dois = 0
                termina = 0
            print(
                "Vida {0}: {1} | Vida {2}: {3}".format(jogadores[sequencia_lutas[contra_x]].title(), pontos_de_vida_um,
                                                       jogadores[sequencia_lutas[contra_y]].title(),
                                                       pontos_de_vida_dois))
            print()



    def criar_senario_luta_individual(x,y,luta):

        print("******************************************************************************************************")
        print("*                                          Tabela Lutas                                              *")
        print("******************************************************************************************************")
        print()
        print(" luta {0}                                {1}({2}) x {3}({4})".format(luta,jogadores[x].title(),
                                                                                  escolhas[jogadores[x]],
                                                                                  jogadores[y].title(),
                                                                                  escolhas[jogadores[y]]))
        print()
        print("******************************************************************************************************")
        print()
        print("Batalha - {0}({1}) x {2}({3})".format(jogadores[x].title(), escolhas[jogadores[x]], jogadores[y].title(),
                                                     escolhas[jogadores[y]]))
        count = 1

        print("Batalha {0}".format(count))
        print("Lutem!")

        poder_jogador_um = poderes[escolhas[jogadores[x]]].split(",")
        poder_jogador_dois = poderes[escolhas[jogadores[y]]].split(",")

        gurdar_ataque_jogador_um = []
        gurdar_ataque_jogador_dois = []

        pontos_de_vida_um = 1
        pontos_de_vida_dois = 1

        termina = 1

        print()

        while (termina != 0):
            print(
                "------------------------------------------------------------------------------------------------------")
            print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[y]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0], poder_jogador_um[1], poder_jogador_um[2],
                                                    poder_jogador_um[3]))
            print()

            ataque_jogador_um = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[x].title())))
            ataque_jogador_um = ataque_jogador_um - 1

            while (ataque_jogador_um in gurdar_ataque_jogador_um):
                ataque_jogador_um = int(input("{0} digite um ataque disponivel: ".format(jogadores[x].title())))
                ataque_jogador_um = ataque_jogador_um - 1

            ataque = poder_jogador_um[ataque_jogador_um]

            dano_jogador_um = dano[ataque]
            vida_jogador_dois = vida[jogadores[y]]
            dano_critico = 0

            if (ataque == poder_jogador_um[0]):
                critico = random.randint(1, 20)
                if (critico > 18):
                    dano_critico = dano_jogador_um + 10
                    vida[jogadores[y]] = vida_jogador_dois - dano_critico
                    print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                        jogadores[x].title(), poder_jogador_um[0], dano_critico, jogadores[y].title()))
                else:
                    vida[jogadores[y]] = vida_jogador_dois - dano_jogador_um
                    print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                        jogadores[x].title(), poder_jogador_um[0], dano_jogador_um, jogadores[y].title()))

            if (ataque_jogador_um > 0 and "Utilizado" not in poder_jogador_um[ataque_jogador_um]):
                gurdar_ataque_jogador_um.append(ataque_jogador_um)

                if (ataque == poder_jogador_um[1]):
                    critico = random.randint(1, 20)
                    if (critico > 16):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[y]] = vida_jogador_dois - dano_critico
                        print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                            jogadores[x].title(), poder_jogador_um[1], dano_critico, jogadores[y].title()))
                    else:
                        vida[jogadores[y]] = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[x].title(), poder_jogador_um[1], dano_jogador_um, jogadores[y].title()))

                elif (ataque == poder_jogador_um[2]):
                    critico = random.randint(1, 20)
                    if (critico > 12):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[y]] = vida_jogador_dois - dano_critico
                        print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                            jogadores[x].title(), poder_jogador_um[2], dano_critico, jogadores[y].title()))
                    else:
                        vida[jogadores[y]] = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[x].title(), poder_jogador_um[2], dano_jogador_um, jogadores[y].title()))

                elif (ataque == poder_jogador_um[3]):
                    critico = random.randint(1, 20)
                    if (critico > 10):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[y]] = vida_jogador_dois - dano_critico
                        print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                            jogadores[x].title(), poder_jogador_um[3], dano_critico, jogadores[y].title()))
                    else:
                        vida[jogadores[y]] = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[x].title(), poder_jogador_um[3], dano_jogador_um, jogadores[y].title()))

                poder_jogador_um[ataque_jogador_um] = "Utilizado"

            print()
            print(
                "------------------------------------------------------------------------------------------------------")

            print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[x]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0], poder_jogador_dois[1], poder_jogador_dois[2],
                                                    poder_jogador_dois[3]))
            print()

            ataque_jogador_dois = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[y].title())))
            ataque_jogador_dois = ataque_jogador_dois - 1

            while (ataque_jogador_dois in gurdar_ataque_jogador_dois):
                ataque_jogador_dois = int(input("{0} digite um ataque disonivel: ".format(jogadores[y].title())))
                ataque_jogador_dois = ataque_jogador_dois - 1

            ataque = poder_jogador_dois[ataque_jogador_dois]

            dano_jogador_dois = dano[ataque]
            vida_jogador_um = vida[jogadores[x]]
            dano_critico = 0

            if (ataque == poder_jogador_dois[0]):
                critico = random.randint(1, 20)
                if (critico > 18):
                    dano_critico = dano_jogador_um + 10
                    vida[jogadores[x]] = vida_jogador_um - dano_critico
                    print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                        jogadores[y].title(), poder_jogador_dois[0], dano_critico, jogadores[x].title()))
                else:
                    vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                    print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                        jogadores[y].title(), poder_jogador_dois[0], dano_jogador_dois, jogadores[x]))

            if (ataque_jogador_dois > 0 and "Utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                gurdar_ataque_jogador_dois.append(ataque_jogador_dois)

                if (ataque == poder_jogador_dois[1]):
                    critico = random.randint(1, 20)
                    if (critico > 16):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[x]] = vida_jogador_um - dano_critico
                        print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                            jogadores[y].title(), poder_jogador_dois[1], dano_critico, jogadores[x].title()))
                    else:
                        vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[y].title(), poder_jogador_dois[1], dano_jogador_dois, jogadores[x].title()))

                elif (ataque == poder_jogador_dois[2]):
                    critico = random.randint(1, 20)
                    if (critico > 12):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[x]] = vida_jogador_um - dano_critico
                        print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                            jogadores[y].title(), poder_jogador_dois[2], dano_critico, jogadores[x].title()))
                    else:
                        vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[y].title(), poder_jogador_dois[3], dano_jogador_dois, jogadores[x].title()))

                elif (ataque == poder_jogador_dois[3]):
                    critico = random.randint(1, 20)
                    if (critico > 10):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[x]] = vida_jogador_um - dano_critico
                        print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo {3}".format(
                            jogadores[y].title(), poder_jogador_dois[3], dano_critico, jogadores[x].title()))
                    else:
                        vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo {3}".format(
                            jogadores[y].title(), poder_jogador_dois[3], dano_jogador_dois, jogadores[x].title()))

                poder_jogador_dois[ataque_jogador_dois] = "Utilizado"

            pontos_de_vida_um = vida[jogadores[x]]
            pontos_de_vida_dois = vida[jogadores[y]]

            print(
                "------------------------------------------------------------------------------------------------------")
            if (pontos_de_vida_um <= 0 and pontos_de_vida_dois <= 0):
                print("Empatou")
                print("Jogue novamente para desempatar")
                poder_jogador_um = poderes[escolhas[jogadores[x]]].split(",")
                poder_jogador_dois = poderes[escolhas[jogadores[y]]].split(",")

                gurdar_ataque_jogador_um = []
                gurdar_ataque_jogador_dois = []

                pontos_de_vida_um = 0
                pontos_de_vida_dois = 0

                vida[jogadores[x]] = 70
                vida[jogadores[y]] = 70

                termina = 1

            elif (pontos_de_vida_um <= 0):
                vida[jogadores[x]] = 70
                vida[jogadores[y]] = 70
                pontos[jogadores[y]] = pontos[jogadores[y]] + 100
                pontos_de_vida_um = 0
                termina = 0
            elif (pontos_de_vida_dois <= 0):
                vida[jogadores[x]] = 70
                vida[jogadores[y]] = 70
                pontos[jogadores[x]] = pontos[jogadores[x]] + 100
                pontos_de_vida_dois = 0
                termina = 0

            print("Vida {0}: {1} | Vida {2}: {3}".format(jogadores[x].title(), pontos_de_vida_um, jogadores[y].title(),
                                                         pontos_de_vida_dois))
        print()

        maior = 0
        vencedor = ""
        pos_venc = 0
        print("------------------------------------------------------------------------------------------------------")
        print("Pontuação Final")
        print()
        for i in range(len(jogadores)):
            print("{0}:{1} pontos".format(jogadores[i].title(), pontos[jogadores[i]]))

        for i in range(len(jogadores)):
            if (pontos[jogadores[i]] > maior):
                maior = pontos[jogadores[i]]
                vencedor = jogadores[i]
                pos_venc = i


        print()
        print("Parabens {0},foi consedido o poder sagrado capaz de mudar o mundo".format(vencedor.title()))
        print("------------------------------------------------------------------------------------------------------")
        print()
        print(" Passou um ano após a batalha final, a qual o guerreiro sagrado foi escolhido diante de muitas")
        print("batalhas sangrentas, e agora ele ira enfrentar o causador de todo o mal, o poderoso e grandiozo")
        print("rei do terror Tarzariuz")
        print(" O gurreiro sagrado vai até o covil de Tarzariuz, e inicia uma batalha pela esperança da humanidade")
        print()
        print("******************************************************************************************************")
        print()
        print("Batalha Final - Tarzariuz x {0}({1})".format(vencedor.title(), escolhas[vencedor]))
        print("Lutem!")
        print()

        poder_final = poderes[escolhas[jogadores[pos_venc]]]
        batalha_final(pos_venc,poder_final)

    game_over_boolean = False

    def batalha_final(x,poder_final):
        vida_tarzarius = 70
        vida[jogadores[x]] = 70


        poder_jogador_um = poder_final.split(",")
        poder_jogador_dois = "Fisico,Destruidor de Mundos,Demolição Paranormal,Mundo Abominavel".split(",")

        gurdar_ataque_jogador_um = []
        gurdar_ataque_jogador_dois = []

        pontos_de_vida_um = 1

        termina = 1

        print()

        while (termina != 0):
            print(
                "------------------------------------------------------------------------------------------------------")
            print("Escolha uma opção de ataque para causar dano ao Tarzarius")
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0], poder_jogador_um[1], poder_jogador_um[2],
                                                    poder_jogador_um[3]))
            print()

            ataque_jogador_um = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[x].title())))
            ataque_jogador_um = ataque_jogador_um - 1

            while (ataque_jogador_um in gurdar_ataque_jogador_um):
                ataque_jogador_um = int(input("{0} digite um ataque disponivel: ".format(jogadores[x].title())))
                ataque_jogador_um = ataque_jogador_um - 1

            ataque = poder_jogador_um[ataque_jogador_um]

            dano_jogador_um = dano[ataque]
            vida_jogador_dois = vida_tarzarius
            dano_critico = 0

            if (ataque == poder_jogador_um[0]):
                critico = random.randint(1, 20)
                if (critico > 18):
                    dano_critico = dano_jogador_um + 10
                    vida_tarzarius = vida_jogador_dois - dano_critico
                    print("{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo Tarzarius".format(
                        jogadores[x].title(), poder_jogador_um[0], dano_critico))
                else:
                    vida_tarzarius = vida_jogador_dois - dano_jogador_um
                    print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo Tarzarius".format(
                        jogadores[x].title(), poder_jogador_um[0], dano_jogador_um))

            if (ataque_jogador_um > 0 and "Utilizado" not in poder_jogador_um[ataque_jogador_um]):
                gurdar_ataque_jogador_um.append(ataque_jogador_um)

                if (ataque == poder_jogador_um[1]):
                    critico = random.randint(1, 20)
                    if (critico > 16):
                        dano_critico = dano_jogador_um + 10
                        vida_tarzarius = vida_jogador_dois - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo Tarzarius".format(
                                jogadores[x].title(), poder_jogador_um[0], dano_critico))
                    else:
                        vida_tarzarius = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo Tarzarius".format(
                            jogadores[x].title(), poder_jogador_um[0], dano_jogador_um))

                elif (ataque == poder_jogador_um[2]):
                    critico = random.randint(1, 20)
                    if (critico > 12):
                        dano_critico = dano_jogador_um + 10
                        vida_tarzarius = vida_jogador_dois - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo Tarzarius".format(
                                jogadores[x].title(), poder_jogador_um[0], dano_critico))
                    else:
                        vida_tarzarius = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo Tarzarius".format(
                            jogadores[x].title(), poder_jogador_um[0], dano_jogador_um))

                elif (ataque == poder_jogador_um[3]):
                    critico = random.randint(1, 20)
                    if (critico > 10):
                        dano_critico = dano_jogador_um + 10
                        vida_tarzarius = vida_jogador_dois - dano_critico
                        print(
                            "{0} atacou com {1} e causou um dano critico de {2} pontos de vida no inimigo Tarzarius".format(
                                jogadores[x].title(), poder_jogador_um[0], dano_critico))
                    else:
                        vida_tarzarius = vida_jogador_dois - dano_jogador_um
                        print("{0} atacou com {1} e causou um dano de {2} pontos de vida no inimigo Tarzarius".format(
                            jogadores[x].title(), poder_jogador_um[0], dano_jogador_um))

                poder_jogador_um[ataque_jogador_um] = "Utilizado"

            print()
            print(
                "------------------------------------------------------------------------------------------------------")

            print("Tarzarius atacou o {0}".format(escolhas[jogadores[x]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0], poder_jogador_dois[1], poder_jogador_dois[2],
                                                    poder_jogador_dois[3]))
            print()

            ataque_jogador_dois = jogadas_de_tarzarius()
            ataque_jogador_dois = ataque_jogador_dois - 1

            while (ataque_jogador_dois in gurdar_ataque_jogador_dois):
                ataque_jogador_dois = jogadas_de_tarzarius()
                ataque_jogador_dois = ataque_jogador_dois - 1

            ataque = poder_jogador_dois[ataque_jogador_dois]

            dano_jogador_dois = dano[ataque]
            vida_jogador_um = vida[jogadores[x]]
            dano_critico = 0

            if (ataque == poder_jogador_dois[0]):
                critico = random.randint(1, 20)
                if (critico > 18):
                    dano_critico = dano_jogador_um + 10
                    vida[jogadores[x]] = vida_jogador_um - dano_critico
                    print("Tarzarius atacou com {0} e causou um dano critico de {1} pontos de vida no inimigo {2}".format(
                        poder_jogador_dois[0], dano_critico, jogadores[x].title()))
                else:
                    vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                    print("Tarzarius atacou com {0} e causou um dano de {1} pontos de vida no inimigo {2}".format(
                        poder_jogador_dois[0], dano_jogador_dois, jogadores[x]))

            if (ataque_jogador_dois > 0 and "Utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                gurdar_ataque_jogador_dois.append(ataque_jogador_dois)

                if (ataque == poder_jogador_dois[1]):
                    critico = random.randint(1, 20)
                    if (critico > 16):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[x]] = vida_jogador_um - dano_critico
                        print(
                            "Tarzarius atacou com {0} e causou um dano critico de {1} pontos de vida no inimigo {2}".format(
                                poder_jogador_dois[0], dano_critico, jogadores[x].title()))
                    else:
                        vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                        print("Tarzarius atacou com {0} e causou um dano de {1} pontos de vida no inimigo {2}".format(
                            poder_jogador_dois[0], dano_jogador_dois, jogadores[x]))

                elif (ataque == poder_jogador_dois[2]):
                    critico = random.randint(1, 20)
                    if (critico > 12):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[x]] = vida_jogador_um - dano_critico
                        print(
                            "Tarzarius atacou com {0} e causou um dano critico de {1} pontos de vida no inimigo {2}".format(
                                poder_jogador_dois[0], dano_critico, jogadores[x].title()))
                    else:
                        vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                        print("Tarzarius atacou com {0} e causou um dano de {1} pontos de vida no inimigo {2}".format(
                            poder_jogador_dois[0], dano_jogador_dois, jogadores[x]))

                elif (ataque == poder_jogador_dois[3]):
                    critico = random.randint(1, 20)
                    if (critico > 10):
                        dano_critico = dano_jogador_um + 10
                        vida[jogadores[x]] = vida_jogador_um - dano_critico
                        print(
                            "Tarzarius atacou com {0} e causou um dano critico de {1} pontos de vida no inimigo {2}".format(
                                poder_jogador_dois[0], dano_critico, jogadores[x].title()))
                    else:
                        vida[jogadores[x]] = vida_jogador_um - dano_jogador_dois
                        print("Tarzarius atacou com {0} e causou um dano de {1} pontos de vida no inimigo {2}".format(
                            poder_jogador_dois[0], dano_jogador_dois, jogadores[x]))

                poder_jogador_dois[ataque_jogador_dois] = "Utilizado"

            pontos_de_vida_um = vida[jogadores[x]]
            pontos_de_vida_dois = vida_tarzarius

            print(
                "------------------------------------------------------------------------------------------------------")
            if (pontos_de_vida_um <= 0 and pontos_de_vida_dois <= 0):
                print("Empatou")
                print("Jogue novamente para desempatar")
                poder_jogador_um = poderes[escolhas[jogadores[x]]].split(",")
                poder_jogador_dois = "Fisico,Destruidor de Mundos,Demolição Paranormal,Mundo Abominavel".split(",")

                gurdar_ataque_jogador_um = []
                gurdar_ataque_jogador_dois = []

                pontos_de_vida_um = 0
                pontos_de_vida_dois = 0

                vida[jogadores[x]] = 70
                vida_tarzarius = 70

                termina = 1

            elif (pontos_de_vida_um <= 0):
                vida[jogadores[x]] = 70
                game_over_boolean = False
                vida_tarzarius = 70
                pontos_de_vida_um = 0

                termina = 0
            elif (pontos_de_vida_dois <= 0):
                vida[jogadores[x]] = 70
                pontos[jogadores[x]] = pontos[jogadores[x]] + 1000
                game_over_boolean = True
                vida_tarzarius = 70
                pontos_de_vida_dois = 0
                termina = 0

            print("Vida {0}: {1} | Vida {2}: {3}".format(jogadores[x].title(), pontos_de_vida_um, "tarzarius".title(),
                                                         pontos_de_vida_dois))
        print()
        game_over(game_over_boolean,jogadores[x])


    def game_over(boleana,nome_jogador):
        if(boleana == True):
            print("Fantástico {0} você derrotou o poderoso Tarzarius, e conseguio salvar o mundo da escuridão".format(nome_jogador.title()))
            print()
            print("                                   .-=========-.   ")
            print("                                    '-=======-'    ")
            print("                                   _|         |_    ")
            print("                                  ((|    1º   |))   ")
            print("                                   \|         |/    ")
            print("                                    \__     __/     ")
            print("                                      _`) (`_       ")
            print("                                    _/_______\_     ")
            print("                                   /           \    ")
            print("                                  / KING'S GAME \   ")
            print("                                 /_______________\  ")
            print()
            print("                                Pontos: {0}".format(pontos[nome_jogador]))
        else:
            print("Você não foi capaz de vencer o poderoso Tarzarius")
            print()
            print("                            ,--.   ")
            print("                           {    }  ")
            print("                           K,   }  ")
            print("                          /  ~Y`   ")
            print("                     ,   /   /     ")
            print("                    {_'-K.__/      ")
            print("                      `/-.__L._    ")
            print("                      /  ' /`\_}   ")
            print("                     /  ' /        ")
            print("             ____   /  ' /         ")
            print("      ,-'~~~~    ~~/  ' /_         ")
            print("    ,'             ``~~~  ',       ")
            print("   (                        Y      ")
            print("  {                         I      ")
            print(" {      -                    `,    ")
            print(" |       ',                   )    ")
            print(" |        |   ,..__      __. Y     ")
            print(" |    .,_./  Y ' / ^Y   J   )|     ")
            print(" \           |' /   |   |   ||     ")
            print("  \          L_/    . _ (_,.'(     ")
            print("   \,   ,      ^^""' / |      )    ")
            print("     \_  \          /,L]     /     ")
            print("       '-_~-,       ` `   ./`      ")
            print("          `'{_            )        ")
            print("              ^^\..___,.--`        ")


    ataques_proibidos = []

    def jogadas_de_tarzarius():
        randon_ataque = random.randint(1,4)
        ataque_tarzarius = randon_ataque

        while(randon_ataque in ataques_proibidos):
            randon_ataque = random.randint(1, 4)
            ataque_tarzarius = randon_ataque

        if (randon_ataque > 1):
            ataques_proibidos.append(ataque_tarzarius)

        return int(ataque_tarzarius)



    if( numero_jogadores == 1):
        print("------------------------------------------------------------------------------------------------------")
        print()
        print(" Passou um ano após a batalha final, a qual o guerreiro sagrado foi escolhido diante de muitas")
        print("batalhas sangrentas, e agora ele ira enfrentar o causador de todo o mal, o poderoso e grandiozo")
        print("rei do terror Tarzariuz")
        print(" O gurreiro sagrado vai até o covil de Tarzariuz, e inicia uma batalha pela esperança da humanidade")
        print()
        print("******************************************************************************************************")
        print()
        print("Batalha Final - Tarzariuz x {0}({1})".format(jogadores[0].title(), escolhas[jogadores[0]]))
        print("Lutem!")
        print()

        poder_final = poderes[escolhas[jogadores[0]]]
        batalha_final(0, poder_final)

    if(numero_jogadores == 2):

        criar_senario_luta_individual(0,1,"unica")



    elif(numero_jogadores == 3):

        print("******************************************************************************************************")
        print("*                                          Tabela Lutas                                              *")
        print("******************************************************************************************************")
        print()
        print(" luta 1                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 2                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" luta 3                                {0}({1}) x {2}({3})".format(jogadores[1].title(),escolhas[jogadores[1]],jogadores[2].title(),escolhas[jogadores[2]]))
        print("------------------------------------------------------------------------------------------------------")
        print(" final                                Ganhador 1 x Ganhador 2")
        print()
        print("******************************************************************************************************")

        contador = 1


        sequencia_lutas = {
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 2,
            6: 2
        }

        contra_x = 0
        contra_y = 3
        while(contador <= 3):
            contra_x += 1
            contra_y += 1

            criar_senario_luta(contra_x, contra_y, contador)

            contador += 1


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
        print()
        print("******************************************************************************************************")

        contador = 1

        sequencia_lutas = {
            1: 0,
            2: 2,
            3: 0,
            4: 1,
            5: 0,
            6: 1,
            7: 1,
            8: 3,
            9: 2,
            10: 3,
            11: 3,
            12: 2
        }

        contra_x = 0
        contra_y = 6
        while (contador <= 6):
            contra_x += 1
            contra_y += 1

            criar_senario_luta(contra_x, contra_y, contador)

            contador += 1


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
        print()
        print("******************************************************************************************************")

        contador = 1

        sequencia_lutas = {
            1: 0,
            2: 2,
            3: 4,
            4: 1,
            5: 0,
            6: 4,
            7: 1,
            8: 2,
            9: 1,
            10: 1,
            11: 3,
            12: 0,
            13: 2,
            14: 3,
            15: 2,
            16: 3,
            17: 0,
            18: 4,
            19: 3
        }

        contra_x = 0
        contra_y = 10
        while (contador <= 9):
            contra_x += 1
            contra_y += 1

            criar_senario_luta(contra_x, contra_y, contador)

            contador += 1



if(numero_jogadores > 2):
    maior = pontos[jogadores[0]]
    ganhador_um = 0
    ganhador_dois = 0
    tirar = ""

    print("------------------------------------------------------------------------------------------------------")
    print("Pontuação Final")
    print()
    for i in range(len(jogadores)):
        print("{0}:{1} pontos".format(jogadores[i].title(),pontos[jogadores[i]]))

    for i in range(len(jogadores)):
        if(pontos[jogadores[i]] >= maior):
            maior = pontos[jogadores[i]]
            ganhador_um = i
            tirar = jogadores[i]

    guarda_pontos_ante = maior
    pontos[tirar] = 0
    maior = 0

    for i in range(len(jogadores)):
        if (pontos[jogadores[i]] >= maior):
            maior = pontos[jogadores[i]]
            ganhador_dois = i

    pontos[tirar] = guarda_pontos_ante


    criar_senario_luta_individual(ganhador_um,ganhador_dois,"final")





