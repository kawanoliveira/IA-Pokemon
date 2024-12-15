import simulador as sm

def busca_profundidade_limitada_simulador(no, limite, player1, player2, profundidade=0, contador_nos=0):
    """
    Realiza uma busca em profundidade limitada, aplicando o dano diretamente nos objetos Pokémon,
    e conta o número de nós visitados.

    Args:
        no (dict): O nó atual da árvore (representado como um dicionário).
        limite (int): Profundidade máxima para a busca.
        player1 (list): Lista dos Pokémon do jogador 1.
        player2 (list): Lista dos Pokémon do jogador 2.
        profundidade (int): Profundidade atual na árvore (default é 0).
        contador_nos (int): Contador de nós visitados (default é 0).

    Returns:
        int: O número total de nós visitados.
    """
    if profundidade > limite:
        return contador_nos

    # Aplica o dano ao Pokémon correspondente
    if isinstance(no, dict) and "dano" in no and "pkm2" in no:
        pkm2_nome = no["pkm2"]
        dano = no["dano"]

        # Busca o Pokémon pelo nome nos times e aplica o dano
        for pkm in player1 + player2:
            if pkm.name == pkm2_nome:  # Supondo que os objetos Pokémon têm um atributo 'name'
                if dano == "matou":
                    print(f"{pkm.name} foi derrotado! HP restante: 0")
                    pkm.hp = 0  # Define HP como 0
                else:
                    dano = float(dano)  # Converte dano para float
                    pkm.hp -= dano  # Subtrai o dano do HP
                    pkm.hp = max(pkm.hp, 0)  # Garante que o HP não seja menor que 0
                    print(f"{pkm.name} recebeu {dano:.2f} de dano. HP restante: {pkm.hp:.2f}")
                break

        # Incrementa o contador de nós visitados
        contador_nos += 1

    # Recursão para os filhos
    for filho in no.get("filhos", []):
        contador_nos = busca_profundidade_limitada_simulador(filho, limite, player1, player2, profundidade + 1, contador_nos)

    return contador_nos


# Carrega a árvore a partir do JSON
import json
with open("arvore.json", "r") as arquivo:
    arvore = json.load(arquivo)

# Carrega os times do simulador
player1, player2 = sm.carregar_time()
aerodactyl, alakazam, charizard, exeggutor = player1[0], player1[1], player2[0], player2[1]

# Mostra os Pokémon antes da busca
print(f"Times antes da busca:")
for pkm in player1 + player2:
    print(f"{pkm.name}: HP = {pkm.hp:.2f}")

# Configurações da busca
limite = 4  # Profundidade máxima

# Realiza a busca em profundidade limitada e conta o número de nós visitados
nos_visitados = busca_profundidade_limitada_simulador(arvore, limite, player1, player2)

# Mostra o número de nós visitados
print(f"\nNúmero de nós visitados: {nos_visitados}")

# Mostra os Pokémon após a busca
print(f"\nTimes após a busca:")
for pkm in player1 + player2:
    print(f"{pkm.name}: HP = {pkm.hp:.2f}")
