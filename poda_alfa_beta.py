import json
import classes as cs
import simulador as sm
import copy

def par(numero):
    return numero % 2 == 0

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

def pcnt(num, index, lista=None):
    if num == "matou": return lista[index]
    return ((num / hps1[index]) * 100)
def calc_apr(list):
    return ((list[0]+list[1]))-(list[2]+list[3])

def min_max(no, hps):
    if isinstance(no, cs.Node_final):
        novo_hps = copy.deepcopy(hps)
        novo_hps[nome.index(no.pai.pkm1)] -= pcnt("matou", nome.index(no.pai.pkm1), hps)
        no.filhos = float(calc_apr(novo_hps))
        if no.filhos == 0:
            i = 0
    elif no.filhos == []:
        novo_hps = copy.deepcopy(hps)
        novo_hps[nome.index(no.pkm2)] -= pcnt(no.dano, nome.index(no.pkm2), hps)
        no.filhos = float(calc_apr(novo_hps))
        if no.filhos == 0:
            i = 0
    elif no != raiz and isinstance(no, cs.Node):
        novo_hps = copy.deepcopy(hps)
        novo_hps[nome.index(no.pkm2)] -= pcnt(no.dano, nome.index(no.pkm2), hps)
        for filho in no.filhos:
            min_max(filho, novo_hps)

    else:
        for filho in no.filhos:
            min_max(filho, hps)

def verificar_ancestral(num, no, epar):
    if epar:
        while no != None:
            if not par(no.profundidade):
                if no.visitado and no.visitado < num:
                    return True
            no = no.pai
    else:
        while no != None:
            if par(no.profundidade):
                if no.visitado and no.visitado > num:
                    return True
    return False

def busca_alfa_beta(no, alfa=-float('inf'), beta=float('inf')): 
    lista = []
    
    # Se o nó tem filhos, percorre e aplica a busca recursivamente.
    if isinstance(no.filhos, list):  # Verifica se há filhos (e não é um valor final)
        for filho in no.filhos:
            if isinstance(filho.visitado, float):  # Se já for um valor numérico, apenas adiciona
                lista.append(filho.visitado)
            else:
                # Caso contrário, aplica a função recursivamente, passando alfa e beta
                filho.visitado = busca_alfa_beta(filho, alfa, beta)  
                lista.append(filho.visitado)

            # Após processar um filho, verificar a poda
            if par(no.profundidade):  # Maximizar
                alfa = max(alfa, filho.visitado)
                if beta <= alfa:  # Poda
                    break
            else:  # Minimizar
                beta = min(beta, filho.visitado)
                if beta <= alfa:  # Poda
                    break

        # Se a profundidade é par (maximiza), caso contrário, minimiza
        if par(no.profundidade):
            return max(lista)  # Maximiza
        else:
            return min(lista)  # Minimiza
    else:
        return no.filhos  # Caso contrário, retorna o valor da folha (que deve ser um número)

def buscar_origem(no):
    if isinstance(no.filhos, float): return no
    else:
        for filho in no.filhos:
            if filho.visitado == no.visitado:
                return buscar_origem(filho)
    

with open("arvore.json", "r") as arquivo:
    dados = json.load(arquivo)

# Cria a árvore a partir dos dados
raiz = carregar_arvore(dados)
player1, player2 = sm.carregar_time()
nome = [player1[0].name, player1[1].name, player2[0].name, player2[1].name]
hps1 = [player1[0].hp, player1[1].hp, player2[0].hp, player2[1].hp]
del dados, sm, json, player1, player2
hps = [pcnt(hps1[0], 0), pcnt(hps1[1], 1), pcnt(hps1[2], 2), pcnt(hps1[3], 3)]

min_max(raiz, hps)
raiz.visitado = busca_alfa_beta(raiz)
resultado = buscar_origem(raiz)
caminho = []
while resultado != None:
    caminho.insert(0, (int(resultado.acao), int(resultado.escolha)))
    resultado = resultado.pai
print(caminho)