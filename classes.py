class Pokemon:
    def __init__(self,id, name, tipo1, tipo2, att_total, hp, atk, defs, sp_atk, sp_defs, speed, nivel = 50, moves = None):
        """
        Inicializa um Pokémon com atributos mais detalhados.
        :param id: id do Pokémon correspondente a pokedex.
        :param nome: Nome do Pokémon.
        :param tipo1: Primeiro tipo do Pokémon (ex: 'Fogo', 'Água').
        :param tipo2: Segundo tipo do Pokémon (ex: 'Voador', 'Terrestre'). Pode ser None.
        :param att_total: Atributo total de ataque do Pokémon.
        :param hp: Pontos de vida (HP) do Pokémon.
        :param atk: Valor de ataque físico do Pokémon.
        :param defs: Valor de defesa do Pokémon.
        :param sp_atk: Valor de ataque especial do Pokémon.
        :param sp_defs: Valor de defesa especial do Pokémon.
        :param speed: Velocidade do Pokémon.
        """
        self.id = id
        self.name = name
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.att_total = att_total
        self.hp = ((((hp + 15)*2)*nivel)/100)+nivel+10
        self.atk = ((((atk + 15)*2)*nivel)/100)+5
        self.defs = ((((defs + 15)*2)*nivel)/100)+5
        self.sp_atk = ((((sp_atk + 15)*2)*nivel)/100)+5
        self.sp_defs = ((((sp_defs + 15)*2)*nivel)/100)+5
        self.speed = ((((speed + 15)*2)*nivel)/100)+5
        self.nivel = nivel
        self.moves = moves

    def __str__(self):
        """
        Retorna uma string representando as informações do Pokémon.
        """
        return (f"{self.name} (Tipo: {self.tipo1}/{self.tipo2 if self.tipo2 else 'Nenhum'}, "
                f"HP: {self.hp}, Ataque: {self.atk}, Defesa: {self.defs}, "
                f"Sp. Ataque: {self.sp_atk}, Sp. Defesa: {self.sp_defs}, Velocidade: {self.speed})")


class Attack:
    def __init__(self, name, attack_type, category, power, accuracy, pp, effect):
        """
        Inicializa um Ataque com atributos detalhados.
        :param name: Nome do ataque (ex: 'Flamethrower', 'Thunderbolt').
        :param attack_type: Tipo do ataque (ex: 'Fire', 'Electric').
        :param category: Categoria do ataque (ex: 'Physical', 'Special', 'Status').
        :param power: Poder do ataque (valor numérico, ex: 90).
        :param accuracy: Precisão do ataque (valor numérico, ex: 100).
        :param pp: Número de PP (Power Points) do ataque.
        :param effect: Efeito do ataque (ex: 'Queima o alvo', 'Paralisa o alvo').
        """
        self.name = name
        self.attack_type = attack_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect

    def __str__(self):
        """
        Retorna uma string representando as informações do ataque.
        """
        return (f"Ataque: {self.name} (Tipo: {self.attack_type}, Categoria: {self.category}, "
                f"Poder: {self.power}, Precisão: {self.accuracy}%, PP: {self.pp}, Efeito: {self.effect})")

class Morto:
    def __init__(self):
        self.name = "morto"