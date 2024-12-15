import json
import simulador as sm
import classes as cs
import copy


def carregar_arvore(dado, pai=None):
    """
    Constrói a árvore de objetos Node a partir do JSON.
    :param dado: Dados do nó (normalmente extraído do JSON).
    :param pai: Nó pai (se houver).
    :return: Nó raiz ou um nó filho.
    """
    # Verifica se o nó tem o campo 'status', o que indica que é um nó com ação final
    if "status" in dado:
        # Nó final da batalha, apenas com 'status', 'acao' e 'escolha'
        nodo = cs.Node_final(
            pai=pai,
            acao=dado["acao"],
            escolha=dado["escolha"],
            dado=dado["status"]  # Usamos o status aqui
        )
    else:
        # Nó normal com os atributos esperados
        nodo = cs.Node(
            pai=pai,
            acao=dado.get("acao", ""),
            escolha=dado.get("escolha", ""),
            dano=dado.get("dano", None),
            pkm1=dado.get("pkm1", None),
            pkm2=dado.get("pkm2", None),
            profundidade=dado.get("profundidade", None)
        )
    
    # Para cada filho, recursivamente carrega a árvore
    for filho in dado.get("filhos", []):
        nodo.filhos.append(carregar_arvore(filho, nodo))

    return nodo


def profundidade_limitada(no, hps, contador_nos=0):
    """
    Realiza uma busca em profundidade limitada, aplicando o dano diretamente nos objetos Pokémon,
    e conta o número de nós visitados.

    Args:

    Returns:
        int: O número total de nós visitados.
    """
    global menor_caminho, candidatos
    if no.profundidade > profundidade_max_atual:
        return contador_nos

    if hasattr(no, 'dado'):
        if menor_caminho:
            if menor_caminho.profundidade > no.profundidade:
                menor_caminho = no
        else: menor_caminho = no
        novo_hps = hps
    elif no.dano != 0:
        novo_hps = copy.deepcopy(hps)
        if no.dano == "matou": novo_hps[nome.index(no.pkm2)] = 0
        else: novo_hps[nome.index(no.pkm2)] -= pcnt(no.dano, nome.index(no.pkm2))
        for i in range(5):
            if candidatos[i] != None and candidatos[i].valor < calc_apr(novo_hps):
                candidatos[i] = cs.Candidato(calc_apr(novo_hps),no, novo_hps)
                break
            elif candidatos[i] == None:
                candidatos[i] = cs.Candidato(calc_apr(novo_hps),no, novo_hps)
    else:
        novo_hps = hps

    for filho in no.filhos:
        contador_nos = profundidade_limitada(filho, novo_hps, contador_nos)

    return contador_nos + 1

def pcnt(num, index):
    return ((num / hps1[index]) * 100)
def calc_apr(list):
    return ((list[0]+list[1]))-(list[2]+list[3])


# Carregar a árvore a partir do arquivo JSON
with open("arvore.json", "r") as arquivo:
    dados = json.load(arquivo)

# Cria a árvore a partir dos dados
raiz = carregar_arvore(dados)
player1, player2 = sm.carregar_time()
profundidade_max_atual = 0
nome = player1[0].name, player1[1].name, player2[0].name, player2[1].name
limite_profundidade = 4
profundidade_max_atual = raiz.profundidade + limite_profundidade
candidatos = [None] * 5
hps1 = [player1[0].hp, player1[1].hp, player2[0].hp, player2[1].hp]
menor_caminho = None
del dados
del sm
del json
hps = [pcnt(hps1[0], 0), pcnt(hps1[1], 1), pcnt(hps1[2], 2), pcnt(hps1[3], 3)]
num_nos_visitados = profundidade_limitada(raiz, hps)
if menor_caminho == None:
    while menor_caminho == None:
        for candidato in candidatos:
            if candidato != None:
                candidatos[candidatos.index(candidato)] = None
                for filho in candidato.no.filhos:
                    profundidade_max_atual = filho.profundidade + limite_profundidade
                    num_nos_visitados += profundidade_limitada(filho, candidato.hps)

#print(num_nos_visitados)
del arquivo, candidato, candidatos, copy, cs, filho, hps, hps1, limite_profundidade, nome, num_nos_visitados, player1, player2, profundidade_max_atual, raiz
caminho = []
while menor_caminho != None:
    caminho.insert(0, (int(menor_caminho.acao), int(menor_caminho.escolha)))
    menor_caminho = menor_caminho.pai

print(caminho)