import pandas as pd
import os
import classes as cs
import dano


relative_path = os.path.join(os.path.dirname(__file__))

player1 = [128, 65, 143, 121, 103, 76]
player2 = [135, 131, 113, 94, 112, 149]

atk1 = [(14, 65, 39, 12), (99, 105, 115, 153), (14, 65, 39, 116), (142, 154, 105, 13), (99, 123, 42, 137), (39, 109, 139, 42)]
atk2 = [(154, 93, 32, 153), (13, 14, 21, 154), (115, 153, 127, 68), (67, 42, 14, 89), (14, 39, 109, 139), (13, 154, 65, 166)]

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

print("############### Batalha Iniciada ################")

batalha_fim = False

while not batalha_fim:
    print(player1[0], "\n", player2[0])
    escolha = input("\nOque deseja fazer?\n [1] - Atacar\n [2] - Trocar pokemon\n:")
    match escolha:
        case "1":
            print("\n\nAtacar:")
            i = 1
            for moves in player1[0].moves:
                linha_desejada = pd.read_csv((relative_path + "\\atk.csv"), sep=';', skiprows=lambda x: x != moves-1, nrows=1, header=None)
                move  = cs.Attack(*linha_desejada.values[0])
                print(f"   [{i}]", move.name)
                i += 1
            
            ataque = input("\n:")
            match ataque:
                case "1":
                    player2[0].hp -= dano.calcular_dano(player1[0], player2[0], )