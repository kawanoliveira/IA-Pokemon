
import type

def calcular_dano(pkm_ataque, pkm_defesa, atk):
    dano_nivel = 22
    if pkm_ataque.nivel != 50:
        dano_nivel = ((pkm_ataque.nivel*2)/5)+2
    if atk.category == "p": dano = (dano_nivel*atk.power*(pkm_ataque.atk/pkm_defesa.defs))/50 + 2
    elif atk.category == "s": dano = (dano_nivel*atk.power*(pkm_ataque.sp_atk/pkm_defesa.sp_defs))/50 + 2
    elif atk.category == "e": return 0
    if atk.attack_type == pkm_ataque.tipo1 or atk.attack_type == pkm_ataque.tipo2: stab = 1.5
    else: stab = 1
    dano = dano*stab*type.multiplicador(atk, pkm_defesa)

    return dano