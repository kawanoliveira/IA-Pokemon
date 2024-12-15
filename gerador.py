import classes as cs  # Importando o módulo que contém a classe Node

# Ações e escolhas possíveis para os jogadores
acoes = ["1", "1", "1", "1", "2"]
escolhas = ["1", "2", "3", "4", "2"]
acoes2 = ["2", "2"]
escolhas2 = ["2", "3"]

# Inicializando a árvore de decisão
arvore_inicio = cs.Node(None, 0, 0, 0, profundidade=0)

# Contadores globais
numero_nos = 1  # Número inicial de nós (raiz)
nos_finais = 0  # Contador de nós finais
nos_nao_finais = 0  # Contador de nós não finais
max_profundidade = 8  # Profundidade máxima da árvore
nos_por_profundidade = [0] * (max_profundidade + 1)  # Lista para contar nós por profundidade
nos_por_profundidade[0] = 1  # A raiz está na profundidade 0


def gerar_nos(player1, player2, no_atual, player_verdadeiro, morto=False):
    """
    Função recursiva para gerar nós na árvore de decisão baseada no estado do jogo.
    Para cada estado, são geradas novas possibilidades de ação e seus resultados.

    Args:
        player1: Estado do jogador 1.
        player2: Estado do jogador 2.
        no_atual: Nó atual da árvore.
        player_verdadeiro: Indica qual jogador deve jogar.
        morto: Indica se o pokemon adversario morreu.
    """
    global numero_nos, nos_finais, nos_nao_finais

    # Exibe o número de nós no processo de geração (para fins de acompanhamento)
    print(numero_nos, end='\r')

    # Verifica se a árvore precisa continuar gerando nós
    if numero_nos != sum(nos_por_profundidade):
        # Caso o número de nós não esteja correto, força a continuação
        pl = 1

    # Se a profundidade atual é menor que a máxima, continua gerando nós
    if no_atual.profundidade < max_profundidade:
        # Se o jogador 1 tem maior velocidade ou se não é o turno do jogador verdadeiro
        if player1[0].speed > player2[0].speed or not player_verdadeiro:
            for i in range(len(acoes)):
                # Caso o pokemon tenha morrido, não ataca
                if morto:
                    no_atual.filhos.append(cs.Node(no_atual, "0", "0", 0, player1[0].name, player2[0].name))
                    numero_nos += 1
                    nos_por_profundidade[no_atual.profundidade + 1] += 1
                    gerar_nos(player2, player1, no_atual.filhos[i], not player_verdadeiro)
                    break

                # Simula a batalha e obtém o dano
                player1_novo, player2_novo, dano = sm.simular_batalha2(player1, player2, acoes[i], escolhas[i])

                # Caso a batalha termine sem pokémons, marca o nó como final
                if dano == "sem pokemons":
                    no_atual.filhos.append(("fim da batalha", acoes[i], escolhas[i]))
                    nos_finais += 1
                    numero_nos += 1
                    nos_por_profundidade[no_atual.profundidade + 1] += 1
                    continue

                # Cria um novo nó para o resultado da ação
                no_atual.filhos.append(cs.Node(no_atual, acoes[i], escolhas[i], dano, player1[0].name, player2[0].name))
                numero_nos += 1
                nos_por_profundidade[no_atual.profundidade + 1] += 1

                # Se o dano resultar em morte e for o turno do jogador verdadeiro, continua a recursão
                if dano == "matou" and player_verdadeiro:
                    gerar_nos(player2_novo, player1_novo, no_atual.filhos[i], not player_verdadeiro, morto=True)
                    continue

                # Recursão para o próximo turno de batalha
                gerar_nos(player2_novo, player1_novo, no_atual.filhos[i], not player_verdadeiro)
        else:
            # Se não for o turno do jogador verdadeiro, faz uma simulação com as ações alternativas
            for i in range(len(acoes2)):
                player1_novo, player2_novo, dano = sm.simular_batalha2(player1, player2, acoes2[i], escolhas2[i])

                # Se a batalha terminar sem pokémons, retorna
                if dano == "sem pokemons":
                    return 0

                # Cria um novo nó para o resultado da ação
                no_atual.filhos.append(cs.Node(no_atual, acoes[i], escolhas[i], dano, player1_novo[0].name, player2_novo[0].name))
                nos_por_profundidade[no_atual.profundidade + 1] += 1
                numero_nos += 1

                # Recursão para o próximo turno de batalha
                gerar_nos(player2_novo, player1_novo, no_atual.filhos[i], not player_verdadeiro)
    else:
        # Caso a profundidade máxima seja atingida, conta o nó como não final
        nos_nao_finais += 1
        return 0


    
import json
import simulador as sm


def arvore_para_dict(no):
    if isinstance(no, tuple) and len(no) == 3:
        return {
            "status": no[0],
            "acao": no[1],
            "escolha": no[2]
        }
    return {
        "profundidade": no.profundidade,
        "visitado": no.visitado,
        "acao": no.acao,
        "escolha": no.escolha,
        "dano": no.dano,
        "pkm1": no.pkm1,
        "pkm2": no.pkm2,
        "filhos": [arvore_para_dict(filho) for filho in no.filhos]  # Recursão nos filhos
    }

def salvar_arvore_json(root, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(arvore_para_dict(root), file, ensure_ascii=False, indent=4)



player1, player2 = sm.carregar_time()
gerar_nos(player1, player2, arvore_inicio, True)
salvar_arvore_json(arvore_inicio, 'arvore.json')


print("Total de nos: ",numero_nos)
print("Nos limitados pela profundidade: ",nos_nao_finais)
print("Nos de batalhas finalizadas: ",nos_finais)

print("\n\nNos por profundidade:\n")
for i in range(max_profundidade + 1):
    print(f"{i}:", nos_por_profundidade[i])


#for i in player1:
#    print(i)
#    for k in i.moves:
#        print(k)
#for i in player2:
#    print(i)
#    for k in i.moves:
#        print(k)