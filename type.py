import json

def multiplicador(atk, pokemon):
    with open('tipos.json', 'r') as f:
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
        
    print(multiplicador)

    return multiplicador