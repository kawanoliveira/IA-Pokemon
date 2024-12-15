import json
import os

# Definindo o caminho relativo
relative_path = os.path.join(os.path.dirname(__file__))

def multiplicador(atk, pokemon):
    """
    Calcula o multiplicador de dano de um ataque com base no tipo do Pokémon alvo.
    
    :param atk: O ataque que está sendo usado (instância da classe Attack).
    :param pokemon: O Pokémon alvo do ataque (instância da classe Pokemon).
    :return: O multiplicador de dano baseado nos tipos do ataque e do Pokémon.
    """
    # Carrega os tipos dos ataques a partir de um arquivo JSON
    with open(os.path.join(relative_path, "tipos.json"), 'r') as f:
        tipos = json.load(f)
        multiplicador = 1

        # Obtém o tipo do ataque
        tipo = tipos[atk.attack_type]

        # Verifica a compatibilidade do tipo do Pokémon com o tipo do ataque
        if pokemon.tipo1 in tipo[0]:
            multiplicador = 0  # Nenhum efeito
        elif pokemon.tipo1 in tipo[1]:
            multiplicador *= 0.5  # Efeito reduzido
        elif pokemon.tipo1 in tipo[2]:
            multiplicador *= 2  # Efeito dobrado

        if pokemon.tipo2 in tipo[0]:
            multiplicador = 0  # Nenhum efeito
        elif pokemon.tipo2 in tipo[1]:
            multiplicador *= 0.5  # Efeito reduzido
        elif pokemon.tipo2 in tipo[2]:
            multiplicador *= 2  # Efeito dobrado

    return multiplicador
