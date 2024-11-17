import classes as cs
from graphviz import Digraph
import testss

acoes = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
escolhas = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6]

arvore_inicio = cs.Node(None, 0, "-", 1)
numero_nos = 1

for i in range(len(acoes)):
    arvore_inicio.filhos.append(cs.Node(arvore_inicio, arvore_inicio.profundidade + 1, (str(acoes[i]) + " - " + str(escolhas[i])), acoes[i]))
    numero_nos +=1
    filho = arvore_inicio.filhos[i]
    testss.checar_memoria()
    for j in range(len(acoes)):
        if filho.a == 2: continue
        filho.filhos.append(cs.Node(arvore_inicio, filho.profundidade + 1, (str(acoes[j]) + " - " + str(escolhas[j])), acoes[j]))
        numero_nos += 1
        filho2 = filho.filhos[j]
        testss.checar_memoria()
        for k in range(len(acoes)):
            if filho2.a == 2: continue
            filho2.filhos.append(cs.Node(arvore_inicio, filho2.profundidade + 1, (str(acoes[k]) + " - " + str(escolhas[k])), acoes[k]))
            numero_nos += 1
            filho3 = filho2.filhos[k]
            testss.checar_memoria()
            for p in range(len(acoes)):
                if filho3.a == 2: continue
                filho3.filhos.append(cs.Node(arvore_inicio, filho3.profundidade + 1, (str(acoes[p]) + " - " + str(escolhas[p])), acoes[p]))
                numero_nos +=1
                testss.checar_memoria()

def desenhar_arvore(raiz):
    grafo = Digraph()
    grafo.render("arvore", format="pdf")  # Gera e visualiza um SVG
    grafo.attr(rankdir='TB')  # Direção da árvore: Topo para Baixo
    
    def adicionar_nodos(no):
        if no is not None:
            grafo.node(str(id(no)), f"Valor: {no.valor}\nProfundidade: {no.profundidade}")
            for filho in no.filhos:
                grafo.edge(str(id(no)), str(id(filho)))  # Conecta pai ao filho
                adicionar_nodos(filho)

    testss.checar_memoria()
    adicionar_nodos(raiz)
    testss.checar_memoria()
    grafo.render("arvore", view=True)  # Salva e abre o arquivo gerado
    testss.checar_memoria()

desenhar_arvore(arvore_inicio)
testss.checar_memoria()
input("k")
print(numero_nos)