import pandas as pd
import os
import classes as cs
import dano
import copy

def carregar_time():
    relative_path = os.path.join(os.path.dirname(__file__))

    player1 = [142, 65]
    player2 = [6, 103]

    atk1 = [[109, 169, 39, 47], [99, 44, 14, 69]]
    atk2 = [[169, 14, 47, 109], [167, 168, 99, 134]]

    k = 0
    for i in player1:
        linha_desejada = pd.read_csv((relative_path + "\\pkm.csv"), sep=';', skiprows=lambda x: x != i, nrows=1, header=None)
        player1[k]  = cs.Pokemon(*linha_desejada.values[0], moves=atk1[k])
        k += 1
    k = 0
    for i in player2:
        linha_desejada = pd.read_csv((relative_path + "\\pkm.csv"), sep=';', skiprows=lambda x: x != i, nrows=1, header=None)
        player2[k]  = cs.Pokemon(*linha_desejada.values[0], moves=atk2[k])
        k += 1
    
    return player1, player2

def trocar_pokemon(player, escolha):
    if player[escolha].name == "morto": 
        return 0

    temp = player[escolha]
    player[escolha] = player[0]
    player[0] = temp
    return 0

def realizar_ataque(player1, player2, i):
    if player1[0].name == "morto": return 0
    dano_dado = dano.calcular_dano(player1[0], player2[0], player1[0].moves[i])
    player2[0].hp -= dano_dado
    if player2[0].hp <= 0:
        dano_dado += player2[0].hp
        player2[0] = cs.Morto()
        troca =  False
        for k in range(len(player2)):
            if player2[k].name != "morto":
                var = player2[0]
                player2[0] = player2[k]
                player2[k] = var
                troca = True
                return "matou"
        if troca == False: 
            return "sem pokemons"
    return dano_dado

def simular_batalha2(player1, player2, escolha1, escolha2):
    player1_novo = copy.deepcopy(player1)
    player2_novo = copy.deepcopy(player2)
    match escolha1:
        case "1":
            acao_1 = lambda: realizar_ataque(player1_novo, player2_novo, int(escolha2) - 1)
        case "2":
            acao_1 = lambda: trocar_pokemon(player1_novo, int(escolha2)-1)
    dano = acao_1()
    return player1_novo, player2_novo, dano