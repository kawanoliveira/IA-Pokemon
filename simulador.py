import pandas as pd
import os
import classes as cs
import dano

########################## CARREGAR TIMES ##########################

def carregar_time():
    relative_path = os.path.join(os.path.dirname(__file__))

    player1 = [128, 65, 143, 121, 103, 76]
    player2 = [135, 131, 113, 94, 112, 149]

    atk1 = [[14, 65, 39, 12], [99, 105, 115, 153], [14, 65, 39, 116], [142, 154, 105, 13], [99, 123, 42, 137], [39, 109, 139, 42]]
    atk2 = [[154, 93, 32, 153], [13, 14, 21, 154], [115, 153, 127, 68], [67, 42, 14, 89], [14, 39, 109, 139], [13, 154, 65, 166]]

    k = 0
    for i in player1:
        linha_desejada = pd.read_csv((relative_path + "\\pkm.csv"), sep=';', skiprows=lambda x: x != i, nrows=1, header=None)
        player1[k]  = cs.Pokemon(*linha_desejada.values[0], moves=atk1[k])
        for j in range(len(player1[k].moves)):
            player1[k].moves[j] = cs.Attack(*(pd.read_csv((relative_path + "\\atk.csv"), sep=';', skiprows=lambda x: x != player1[k].moves[j] - 1, nrows=1, header=None)).values[0])
        k += 1
    k = 0
    for i in player2:
        linha_desejada = pd.read_csv((relative_path + "\\pkm.csv"), sep=';', skiprows=lambda x: x != i, nrows=1, header=None)
        player2[k]  = cs.Pokemon(*linha_desejada.values[0], moves=atk2[k])
        for j in range(len(player2[k].moves)):
            player2[k].moves[j] = cs.Attack(*(pd.read_csv((relative_path + "\\atk.csv"), sep=';', skiprows=lambda x: x != player2[k].moves[j] - 1, nrows=1, header=None)).values[0])
        k += 1
    
    return player1, player2

def trocar_pokemon(player):
    i = 1
    print("Escolha o primeiro pokemon para trocar:\n")
    for pokemon in player:
        if pokemon == player[0]: print(f"    [{i}] - ", pokemon.name, " -> Pokemon a ser trocado")
        else: print(f"    [{i}] - ", pokemon.name)
        i += 1
    while True:
        escolha = int(input("\n:")) - 1
        if player[escolha].name == "morto": print("esse pokemon já esta morto")
        elif player[escolha] == player[0]: print("esse pokemon ja esta na batalha")
        else: break    
    
    temp = player[escolha]
    player[escolha] = player[0]
    player[0] = temp

def realizar_ataque(player1, player2, i):
    if player1[0].name == "morto": return
    print(player1[0].name, " usou ", player1[0].moves[i].name)
    player2[0].hp -= dano.calcular_dano(player1[0], player2[0], player1[0].moves[i])
    if player2[0].hp <= 0:
        print(player2[0].name, "morreu, voce precisa substituilo")
        player2[0] = cs.Morto()
        return player2


def simular_batalha():
    player1, player2 = carregar_time()
    print("############### Batalha Iniciada ################")
    batalha_fim = False

    while not batalha_fim:
        print(player1[0], "\n",player2[0])
        escolha = input("\nOque o player1 deseja fazer?\n [1] - Atacar\n [2] - Trocar pokemon\n:")
        player1_prioridade = False
        player2_prioridade = False
        match escolha:
            case "1":
                print("\n\nAtacar:")
                i = 1
                for moves in player1[0].moves:
                    print(f"   [{i}]", moves.name)
                    i += 1
                ataque1 = input("\n:")
                acao_1 = lambda: realizar_ataque(player1, player2, int(ataque1) - 1)
            case "2":
                acao_1 = lambda: trocar_pokemon(player1)
                player1_prioridade = True

        escolha = input("\nOque o player 2 deseja fazer?\n [1] - Atacar\n [2] - Trocar pokemon\n:")
        match escolha:
            case "1":
                print("\n\nAtacar:")
                i = 1
                for moves in player2[0].moves:
                    print(f"   [{i}]", moves.name)
                    i += 1
                ataque = input("\n:")
                acao_2 = lambda: realizar_ataque(player2, player1, int(ataque) - 1)
            case "2":
                acao_2 = lambda: trocar_pokemon(player2)
                player2_prioridade = True
            

        pkm_morto = None
        if (player2[0].speed > player1[0].speed and not player1_prioridade) or player2_prioridade:
            n = acao_2()
            if n != None: pkm_morto = n
            n = acao_1()
            if n != None: pkm_morto = n
            if pkm_morto != None:
                trocar_pokemon(pkm_morto)
        else:
            n = acao_1()
            if n != None: pkm_morto = n
            n = acao_2()
            if n != None: pkm_morto = n
            if pkm_morto != None:
                trocar_pokemon(pkm_morto)

simular_batalha()