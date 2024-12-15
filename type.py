import json
import os

relative_path = os.path.join(os.path.dirname(__file__))

def multiplicador(atk, pokemon):
    with open(relative_path + "\\tipos.json", 'r') as f:
        tipos = json.load(f)
        multiplicador = 1
        tipo = tipos[atk.attack_type]
        if pokemon.tipo1 in tipo[0]:
            multiplicador = 0
        elif pokemon.tipo1 in tipo[1]:
            multiplicador = multiplicador*0.5
        elif pokemon.tipo1 in tipo[2]:
            multiplicador = multiplicador*2
        if pokemon.tipo2 in tipo[0]:
            multiplicador = 0
        elif pokemon.tipo2 in tipo[1]:
            multiplicador = multiplicador*0.5
        elif pokemon.tipo2 in tipo[2]:
            multiplicador = multiplicador*2
        
        #if multiplicador >= 2:
        #    print("Ataque super efetivo")
        #elif multiplicador == 0:
        #    print("Ataque não afeta o oponente")
        #elif multiplicador <= 0.5:
        #    print("Ataque não muito efetivo")
    return multiplicador