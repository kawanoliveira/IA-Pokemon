import classes as cs
import simulador as sm

acoes = ["1", "1", "1", "1", "2"]
escolhas = ["1", "2", "3", "4", "2"]

acoes2 = ["2", "2"]
escolhas2 = ["2", "3"]

arvore_inicio = cs.Node(None, 0, 0, 0, profundidade= 0)
numero_nos = 1
nos_finais = 0
nos_nao_finais = 0

player1, player2 = sm.carregar_time()

def gerar_nos(player1, player2, no_atual, player_verdadeiro, morto = False):
    global nos_finais
    global nos_nao_finais
    global numero_nos
    if no_atual.profundidade < 8:
        if player1[0].speed > player2[0].speed or player_verdadeiro == False:
            for i in range(len(acoes)):
                if morto:
                    no_atual.filhos.append(cs.Node(no_atual, "0", "0", 0, player1[0].name, player2[0].name))
                    gerar_nos(player2, player1, no_atual.filhos[i], not player_verdadeiro)
                    break
                player1_novo, player2_novo, dano = sm.simular_batalha2(player1, player2, acoes[i], escolhas[i])
                if dano == "sem pokemons":
                    nos_finais += 1
                    no_atual.filhos.append(("fim da batalha", acoes[i], escolhas[i]))
                    continue
                no_atual.filhos.append(cs.Node(no_atual, acoes[i], escolhas[i], dano, player1[0].name, player2[0].name))
                if dano == "matou" and player_verdadeiro:
                    gerar_nos(player2_novo, player1_novo, no_atual.filhos[i], not player_verdadeiro, morto=True)
                    numero_nos += 1
                    print(numero_nos, end='\r')
                    continue
                gerar_nos(player2_novo, player1_novo, no_atual.filhos[i], not player_verdadeiro)
                numero_nos += 1
                print(numero_nos, end='\r')
        else:
            for i in range(len(acoes2)):
                player1_novo, player2_novo, dano = sm.simular_batalha2(player1, player2, acoes2[i], escolhas2[i])
                if dano == "sem pokemons": return 0
                no_atual.filhos.append(cs.Node(no_atual, acoes[i], escolhas[i], dano, player1_novo[0].name, player2_novo[0].name))
                gerar_nos(player2_novo, player1_novo, no_atual.filhos[i], not player_verdadeiro)
                numero_nos += 1
                print(numero_nos, end='\r')
    else:
        numero_nos += 1
        nos_nao_finais += 1
        return 0
    
import json

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


gerar_nos(player1, player2, arvore_inicio, True)
salvar_arvore_json(arvore_inicio, 'arvore.json')
print("Total de nos: ",numero_nos)
print("Nos limitados pela profundidade: ",nos_nao_finais)
print("Nos de batalhas finalizadas: ",nos_finais)


#for i in player1:
#    print(i)
#    for k in i.moves:
#        print(k)
#for i in player2:
#    print(i)
#    for k in i.moves:
#        print(k)