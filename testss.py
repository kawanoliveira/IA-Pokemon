import psutil
import os
import sys

def checar_memoria():
    processo = psutil.Process(os.getpid())
    memoria_usada = processo.memory_info().rss / (1024 ** 3)  # Converte para GB
    print(f"{memoria_usada:.2f} GB.")

def simular_batalha():
    player1, player2 = carregar_time()
    print("############### Batalha Iniciada ################")
    batalha_fim = False

    while not batalha_fim:
        print(player1[0], "\n",player2[0])
        escolha = input("aaaa\nOque o player1 deseja fazer?\n [1] - Atacar\n [2] - Trocar pokemon\n:")
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
            if isinstance(n, tuple): 
                pkm_morto = n[1]
                n = n[0]
            if player1[0].name != "morto": player1[0].hp -= n
            n = acao_1()
            if isinstance(n, tuple): 
                pkm_morto = n[1]
                n = n[0]
            if player2[0].name != "morto": player2[0].hp -= n
            if pkm_morto != None:
                trocar_pokemon(pkm_morto)
            
        else:
            n = acao_1()
            if isinstance(n, tuple): 
                pkm_morto = n[1]
                n = n[0]
            if player2[0].name != "morto": player2[0].hp -= n
            n = acao_2()
            if isinstance(n, tuple): 
                pkm_morto = n[1]
                n = n[0]
            if player1[0].name != "morto": player1[0].hp -= n
            if pkm_morto != None:
                trocar_pokemon(pkm_morto)

import json

def copiar_primeiras_linhas_json(input_filename, output_filename, max_linhas=1000):
    """Copia as primeiras 1000 linhas de um arquivo JSON para outro arquivo."""
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                # Começa o arquivo de saída com o início de um array JSON
                
                linha_atual = 0
                for line in file:
                    # Verifica se atingiu o limite de linhas
                    if linha_atual >= max_linhas:
                        break
                    
                    if line:  # Se a linha não estiver vazia
                        output_file.write(line)
                        linha_atual += 1
                
                # Fecha o array no arquivo de saída

            print(f"Primeiras {linha_atual} linhas copiadas para '{output_filename}'.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
# Suponha que o arquivo grande seja 'arvore_grande.json'
# E você deseja salvar as primeiras 1000 linhas em 'primeiras_1000.json'
copiar_primeiras_linhas_json('arvore.json', 'primeiras_1000.json')
