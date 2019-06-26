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
    pontos = {}
    vida = {}

    poderes = {
        lista_personagens[0] : ["Fisico", "Massacre", "Desafio da morte", "Carga concentrada"],
        lista_personagens[1] : ["Fisico", "Bola de fogo", "Relampago", "Ultra colapso"],
        lista_personagens[2] : ["Fisico", "Flexa critica" ,"Flexa envenenada", "Flexa da morte"],
        lista_personagens[3] : ["Fisico", "Cajado de veneno", "Chuva de gelo", "Morte lenta"]
    }

    dano = {
        "Fisico": 5,
        "Massacre": 10,
        "Desafio da morte": 10,
        "Carga concentrada": 10,
        "Bola de fogo": 10,
        "Relampago": 10,
        "Ultra colapso": 10,
        "Flexa critica": 10,
        "Flexa envenenada": 10,
        "Flexa da morte": 10,
        "Cajado de veneno": 10,
        "Chuva de gelo": 10,
        "Morte lenta": 10
    }


    for i in range(len(jogadores)):
        numero_lutador = int(input("{0}, escolha um numero referente ao perssonagem(1 a 4): ".format(jogadores[i].title())))
        while(numero_lutador < 1 or numero_lutador > 4):
            numero_lutador = int(input("{0}, escolha um numero entre(1 a 4): ".format(jogadores[i].title())))
        if(numero_lutador == 1):
            lutador = lista_personagens[0]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 100
        elif (numero_lutador == 2):
            lutador = lista_personagens[2]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 100
        elif (numero_lutador == 3):
            lutador = lista_personagens[1]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 100
        elif (numero_lutador == 4):
            lutador = lista_personagens[3]
            escolhas[jogadores[i]] = lutador
            pontos[jogadores[i]] = 0
            vida[jogadores[i]] = 100


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
        print()
        print(" luta 1                                {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))
        print()
        print("******************************************************************************************************")
        print()
        print("Batalha - {0}({1}) x {2}({3})".format(jogadores[0].title(),escolhas[jogadores[0]],jogadores[1].title(),escolhas[jogadores[1]]))
        count = 1

        print("Batalha {0}".format(count))
        print("Lutem!")

        poder_jogador_um = poderes[escolhas[jogadores[0]]]
        poder_jogador_dois = poderes[escolhas[jogadores[1]]]

        gurdar_ataque_jogador_um = []
        gurdar_ataque_jogador_dois = []

        print()


        while(vida[jogadores[0]] >= 0 or vida[jogadores[1]] >= 0):

            print("------------------------------------------------------------------------------------------------------")
            print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[1]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0],poder_jogador_um[1],poder_jogador_um[2],poder_jogador_um[3]))
            print()

            ataque_jogador_um = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[0].title())))
            ataque_jogador_um = ataque_jogador_um - 1

            while (ataque_jogador_um in gurdar_ataque_jogador_um):
                ataque_jogador_um = int(input("{0} digite um ataque disonivel: ".format(jogadores[0].title())))
                ataque_jogador_um = ataque_jogador_um - 1










            if (ataque_jogador_um > 0 and "utilizado" not in poder_jogador_um[ataque_jogador_um]):
                gurdar_ataque_jogador_um.append(ataque_jogador_um)
                poder_jogador_um.insert(ataque_jogador_um,"Utilizado")


            print()

            print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[0]].title()))
            print()
            print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0],poder_jogador_dois[1],poder_jogador_dois[2],poder_jogador_dois[3]))
            print()

            ataque_jogador_dois = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[1].title())))
            ataque_jogador_dois = ataque_jogador_dois - 1

            while(ataque_jogador_dois in gurdar_ataque_jogador_dois):
                ataque_jogador_dois = int(input("{0} digite um ataque disonivel: ".format(jogadores[1].title())))
                ataque_jogador_dois = ataque_jogador_dois - 1

            if(ataque_jogador_dois > 0 and "utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                gurdar_ataque_jogador_dois.append(ataque_jogador_dois)
                poder_jogador_dois.insert(ataque_jogador_dois,"Utilizado")

            print("------------------------------------------------------------------------------------------------------")
            print()



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
        while(contador <= 4):
            contra_x += 1
            contra_y += 1

            print("******************************************************************************************************")
            print("*                                          Tabela Lutas                                              *")
            print("******************************************************************************************************")
            print()
            print(" luta {0}                                {1}({2}) x {3}({4})".format(contador,jogadores[sequencia_lutas[contra_x]].title(),escolhas[jogadores[sequencia_lutas[contra_x]]],jogadores[sequencia_lutas[contra_y]].title(),escolhas[jogadores[sequencia_lutas[contra_y]]]))
            print()
            print("******************************************************************************************************")
            print()
            print("Batalha - {0}({1}) x {2}({3})".format(jogadores[sequencia_lutas[contra_x]].title(),escolhas[jogadores[sequencia_lutas[contra_x]]],jogadores[sequencia_lutas[contra_y]].title(),escolhas[jogadores[sequencia_lutas[contra_y]]]))

            print("Batalha {0}".format(contador))
            print("Lutem!")

            poder_jogador_um = poderes[escolhas[jogadores[sequencia_lutas[contra_x]]]]
            poder_jogador_dois = poderes[escolhas[jogadores[sequencia_lutas[contra_y]]]]

            gurdar_ataque_jogador_um = []
            gurdar_ataque_jogador_dois = []

            print()

            while (vida[jogadores[sequencia_lutas[contra_x]]] >= 0 or vida[jogadores[sequencia_lutas[contra_y]]] >= 0):

                print(
                    "------------------------------------------------------------------------------------------------------")
                print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[sequencia_lutas[contra_x]]].title()))
                print()
                print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0], poder_jogador_um[1], poder_jogador_um[2], poder_jogador_um[3]))
                print()

                ataque_jogador_um = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                ataque_jogador_um = ataque_jogador_um - 1

                while (ataque_jogador_um in gurdar_ataque_jogador_um):
                    ataque_jogador_um = int(input("{0} digite um ataque disonivel: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                    ataque_jogador_um = ataque_jogador_um - 1

                if (ataque_jogador_um > 0 and "utilizado" not in poder_jogador_um[ataque_jogador_um]):
                    gurdar_ataque_jogador_um.append(ataque_jogador_um)
                    poder_jogador_um.insert(ataque_jogador_um, "Utilizado")

                print()

                print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[sequencia_lutas[contra_y]]].title()))
                print()
                print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0], poder_jogador_dois[1], poder_jogador_dois[2], poder_jogador_dois[3]))
                print()

                ataque_jogador_dois = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_y]].title())))
                ataque_jogador_dois = ataque_jogador_dois - 1

                while (ataque_jogador_dois in gurdar_ataque_jogador_dois):
                    ataque_jogador_dois = int(input("{0} digite um ataque disonivel: ".format(jogadores[sequencia_lutas[contra_y]].title())))
                    ataque_jogador_dois = ataque_jogador_dois - 1

                if (ataque_jogador_dois > 0 and "utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                    gurdar_ataque_jogador_dois.append(ataque_jogador_dois)
                    poder_jogador_dois.insert(ataque_jogador_dois, "Utilizado")

                print(
                    "------------------------------------------------------------------------------------------------------")
                print()

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

            print(
                "******************************************************************************************************")
            print(
                "*                                          Tabela Lutas                                              *")
            print(
                "******************************************************************************************************")
            print()
            print(" luta {0}                                {1}({2}) x {3}({4})".format(contador, jogadores[sequencia_lutas[contra_x]].title(), escolhas[jogadores[sequencia_lutas[contra_x]]], jogadores[sequencia_lutas[contra_y]].title(),escolhas[jogadores[sequencia_lutas[contra_y]]]))
            print()
            print(
                "******************************************************************************************************")
            print()
            print("Batalha - {0}({1}) x {2}({3})".format(jogadores[sequencia_lutas[contra_x]].title(),escolhas[jogadores[sequencia_lutas[contra_x]]],jogadores[sequencia_lutas[contra_y]].title(),escolhas[jogadores[sequencia_lutas[contra_y]]]))

            print("Batalha {0}".format(contador))
            print("Lutem!")

            poder_jogador_um = poderes[escolhas[jogadores[sequencia_lutas[contra_x]]]]
            poder_jogador_dois = poderes[escolhas[jogadores[sequencia_lutas[contra_y]]]]

            gurdar_ataque_jogador_um = []
            gurdar_ataque_jogador_dois = []

            print()

            while (vida[jogadores[sequencia_lutas[contra_x]]] >= 0 or vida[jogadores[sequencia_lutas[contra_y]]] >= 0):

                print(
                    "------------------------------------------------------------------------------------------------------")
                print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[sequencia_lutas[contra_x]]].title()))
                print()
                print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0], poder_jogador_um[1], poder_jogador_um[2], poder_jogador_um[3]))
                print()

                ataque_jogador_um = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                ataque_jogador_um = ataque_jogador_um - 1

                while (ataque_jogador_um in gurdar_ataque_jogador_um):
                    ataque_jogador_um = int(input("{0} digite um ataque disonivel: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                    ataque_jogador_um = ataque_jogador_um - 1

                if (ataque_jogador_um > 0 and "utilizado" not in poder_jogador_um[ataque_jogador_um]):
                    gurdar_ataque_jogador_um.append(ataque_jogador_um)
                    poder_jogador_um.insert(ataque_jogador_um, "Utilizado")

                print()

                print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[sequencia_lutas[contra_y]]].title()))
                print()
                print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0], poder_jogador_dois[1],poder_jogador_dois[2], poder_jogador_dois[3]))
                print()

                ataque_jogador_dois = int(input("{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_y]].title())))
                ataque_jogador_dois = ataque_jogador_dois - 1

                while (ataque_jogador_dois in gurdar_ataque_jogador_dois):
                    ataque_jogador_dois = int(input("{0} digite um ataque disonivel: ".format(jogadores[sequencia_lutas[contra_y]].title())))
                    ataque_jogador_dois = ataque_jogador_dois - 1

                if (ataque_jogador_dois > 0 and "utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                    gurdar_ataque_jogador_dois.append(ataque_jogador_dois)
                    poder_jogador_dois.insert(ataque_jogador_dois, "Utilizado")

                print(
                    "------------------------------------------------------------------------------------------------------")
                print()

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
        while (contador <= 10):
            contra_x += 1
            contra_y += 1

            print(
                "******************************************************************************************************")
            print(
                "*                                          Tabela Lutas                                              *")
            print(
                "******************************************************************************************************")
            print()
            print(" luta {0}                                {1}({2}) x {3}({4})".format(contador, jogadores[sequencia_lutas[contra_x]].title(), escolhas[jogadores[sequencia_lutas[contra_x]]], jogadores[sequencia_lutas[contra_y]].title(),escolhas[jogadores[sequencia_lutas[contra_y]]]))
            print()
            print(
                "******************************************************************************************************")
            print()
            print("Batalha - {0}({1}) x {2}({3})".format(jogadores[sequencia_lutas[contra_x]].title(),escolhas[jogadores[sequencia_lutas[contra_x]]],jogadores[sequencia_lutas[contra_y]].title(),escolhas[jogadores[sequencia_lutas[contra_y]]]))

            print("Batalha {0}".format(contador))
            print("Lutem!")

            poder_jogador_um = poderes[escolhas[jogadores[sequencia_lutas[contra_x]]]]
            poder_jogador_dois = poderes[escolhas[jogadores[sequencia_lutas[contra_y]]]]

            gurdar_ataque_jogador_um = []
            gurdar_ataque_jogador_dois = []

            print()

            while (vida[jogadores[sequencia_lutas[contra_x]]] >= 0 or vida[jogadores[sequencia_lutas[contra_y]]] >= 0):

                print(
                    "------------------------------------------------------------------------------------------------------")
                print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[sequencia_lutas[contra_x]]].title()))
                print()
                print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_um[0], poder_jogador_um[1], poder_jogador_um[2],poder_jogador_um[3]))
                print()

                ataque_jogador_um = int(
                    input("{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                ataque_jogador_um = ataque_jogador_um - 1

                while (ataque_jogador_um in gurdar_ataque_jogador_um):
                    ataque_jogador_um = int(input("{0} digite um ataque disonivel: ".format(jogadores[sequencia_lutas[contra_x]].title())))
                    ataque_jogador_um = ataque_jogador_um - 1

                if (ataque_jogador_um > 0 and "utilizado" not in poder_jogador_um[ataque_jogador_um]):
                    gurdar_ataque_jogador_um.append(ataque_jogador_um)
                    poder_jogador_um.insert(ataque_jogador_um, "Utilizado")

                print()

                print("Escolha uma opção de ataque para causar dano ao {0}".format(escolhas[jogadores[sequencia_lutas[contra_y]]].title()))
                print()
                print("1){0} 2){1} 3){2} 4){3} ".format(poder_jogador_dois[0], poder_jogador_dois[1],poder_jogador_dois[2], poder_jogador_dois[3]))
                print()

                ataque_jogador_dois = int(
                    input("{0} digite um numero referente ao ataque: ".format(jogadores[sequencia_lutas[contra_y]].title())))
                ataque_jogador_dois = ataque_jogador_dois - 1

                while (ataque_jogador_dois in gurdar_ataque_jogador_dois):
                    ataque_jogador_dois = int(input("{0} digite um ataque disonivel: ".format(jogadores[sequencia_lutas[contra_y]].title())))
                    ataque_jogador_dois = ataque_jogador_dois - 1

                if (ataque_jogador_dois > 0 and "utilizado" not in poder_jogador_dois[ataque_jogador_dois]):
                    gurdar_ataque_jogador_dois.append(ataque_jogador_dois)
                    poder_jogador_dois.insert(ataque_jogador_dois, "Utilizado")

                print(
                    "------------------------------------------------------------------------------------------------------")
                print()


            contador += 1
