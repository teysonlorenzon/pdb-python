#menu Principal

quer_jogar = input("Deseja iniciar o jogo King's Game? (sim/nao): ")


if(quer_jogar.lower() == "sim"):
    print("******************************************************************************************************")
    print("*                                            KING'S Game                                             *")
    print("******************************************************************************************************")
    print("*                                                                                                    *")
    print("*                       Escolha o numero referente a quatidade de jogadores                          *")
    print("*                                                                                                    *")
    print("*                               (2): 2 Jogadores  (4): 4 Jogadores                                   *")
    print("*                               (3): 3 Jogadores  (5): 5 Jogadores                                   *")
    print("*                                                                                          (1): Sair *")
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
            jogadores.append(jogador)

    elif (numero_jogadores == 3):
        for i in range(1,4):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador)


    elif (numero_jogadores == 4):
        for i in range(1,5):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador)

    elif (numero_jogadores == 5):
        for i in range(1,6):
            jogador = input("Jogador {0}: ".format(i))
            jogadores.append(jogador)
