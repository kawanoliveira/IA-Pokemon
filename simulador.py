import pandas as pd
import os
import classes as cs
import dano
import copy

def carregar_time():
    """
    Carrega os times dos jogadores a partir de um arquivo CSV.
    
    :return: Uma tupla contendo duas listas, uma para cada time de Pokémon (player1 e player2).
    """
    relative_path = os.path.join(os.path.dirname(__file__))

    # IDs dos Pokémons de cada jogador
    player1 = [142, 65]
    player2 = [6, 103]

    # Ataques de cada Pokémon dos jogadores
    atk1 = [[109, 169, 39, 47], [99, 44, 14, 69]]
    atk2 = [[169, 14, 47, 109], [167, 168, 99, 134]]

    # Carregando os Pokémons do player1
    k = 0
    for i in player1:
        linha_desejada = pd.read_csv(
            os.path.join(relative_path, "pkm.csv"), sep=';', skiprows=lambda x: x != i, nrows=1, header=None
        )
        player1[k] = cs.Pokemon(*linha_desejada.values[0], moves=atk1[k])
        k += 1
    
    # Carregando os Pokémons do player2
    k = 0
    for i in player2:
        linha_desejada = pd.read_csv(
            os.path.join(relative_path, "pkm.csv"), sep=';', skiprows=lambda x: x != i, nrows=1, header=None
        )
        player2[k] = cs.Pokemon(*linha_desejada.values[0], moves=atk2[k])
        k += 1
    
    return player1, player2

def trocar_pokemon(player, escolha):
    """
    Troca o Pokémon atual do jogador pelo escolhido.
    
    :param player: Lista de Pokémons do jogador.
    :param escolha: Índice do Pokémon a ser escolhido para troca.
    :return: 0 (não retorna nada de relevante).
    """
    if player[escolha].name == "morto": 
        return 0

    # Realiza a troca do Pokémon
    temp = player[escolha]
    player[escolha] = player[0]
    player[0] = temp
    return 0

def realizar_ataque(player1, player2, i):
    """
    Realiza o ataque de um Pokémon do player1 no Pokémon do player2.
    
    :param player1: Lista de Pokémons do jogador 1, que vai atacar.
    :param player2: Lista de Pokémons do jogador 2, que vai receber o ataque.
    :param i: Índice do ataque a ser utilizado.
    :return: O dano causado no Pokémon adversário ou uma mensagem indicando o estado da batalha.
    """
    if player1[0].name == "morto": 
        return 0

    # Calcula o dano do ataque
    dano_dado = dano.calcular_dano(player1[0], player2[0], player1[0].moves[i])
    player2[0].hp -= dano_dado

    # Verifica se o Pokémon do player2 foi derrotado
    if player2[0].hp <= 0:
        dano_dado += player2[0].hp
        player2[0] = cs.Morto()

        # Verifica se o player2 ainda possui outros Pokémons
        if player2[1].name != "morto":
            var = player2[0]
            player2[0] = player2[1]
            player2[1] = var
            return "matou"
        else: 
            return "sem pokemons"
    return dano_dado

def simular_batalha2(player1, player2, escolha1, escolha2):
    """
    Simula uma batalha entre dois jogadores, considerando as escolhas de ação dos jogadores.
    
    :param player1: Lista de Pokémons do jogador 1.
    :param player2: Lista de Pokémons do jogador 2.
    :param escolha1: Ação escolhida pelo jogador 1 (ataque ou troca).
    :param escolha2: O ataque ou Pokémon escolhido para a ação.
    :return: O estado final dos dois times e o dano causado.
    """
    # Faz uma cópia dos times para não alterar os originais
    player1_novo = copy.deepcopy(player1)
    player2_novo = copy.deepcopy(player2)

    # Define a ação do jogador 1
    match escolha1:
        case "1":  # Ataque
            acao_1 = lambda: realizar_ataque(player1_novo, player2_novo, int(escolha2) - 1)
        case "2":  # Troca de Pokémon
            acao_1 = lambda: trocar_pokemon(player1_novo, int(escolha2)-1)

    # Executa a ação
    dano = acao_1()

    return player1_novo, player2_novo, dano
