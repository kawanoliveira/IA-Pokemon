import os
import classes as cs
import pandas as pd

# Definindo o caminho relativo
relative_path = os.path.join(os.path.dirname(__file__))

class Pokemon:
    """
    Classe que representa um Pokémon com atributos detalhados e seus movimentos.
    """
    def __init__(self, id, name, tipo1, tipo2, att_total, hp, atk, defs, sp_atk, sp_defs, speed, nivel=50, moves=None):
        """
        Inicializa um Pokémon com atributos detalhados.
        :param id: id do Pokémon correspondente à Pokédex.
        :param name: Nome do Pokémon.
        :param tipo1: Primeiro tipo do Pokémon (ex: 'Fogo', 'Água').
        :param tipo2: Segundo tipo do Pokémon (ex: 'Voador', 'Terrestre'). Pode ser None.
        :param att_total: Atributo total de ataque do Pokémon.
        :param hp: Pontos de vida (HP) do Pokémon.
        :param atk: Valor de ataque físico do Pokémon.
        :param defs: Valor de defesa do Pokémon.
        :param sp_atk: Valor de ataque especial do Pokémon.
        :param sp_defs: Valor de defesa especial do Pokémon.
        :param speed: Velocidade do Pokémon.
        :param nivel: Nível do Pokémon (default é 50).
        :param moves: Lista de movimentos do Pokémon.
        """
        self.id = id
        self.name = name
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.att_total = att_total
        self.hp = ((((hp + 15)*2)*nivel)/100) + nivel + 10
        self.atk = ((((atk + 15)*2)*nivel)/100) + 5
        self.defs = ((((defs + 15)*2)*nivel)/100) + 5
        self.sp_atk = ((((sp_atk + 15)*2)*nivel)/100) + 5
        self.sp_defs = ((((sp_defs + 15)*2)*nivel)/100) + 5
        self.speed = ((((speed + 15)*2)*nivel)/100) + 5
        self.nivel = nivel
        self.moves = moves

        # Carrega os movimentos a partir de um arquivo CSV
        for i in range(len(moves)):
            self.moves[i] = cs.Attack(
                *(pd.read_csv(
                    os.path.join(relative_path, "atk.csv"),
                    sep=';',
                    skiprows=lambda x: x != moves[i] - 1,
                    nrows=1,
                    header=None
                ).values[0])
            )

    def __str__(self):
        """
        Retorna uma string representando as informações do Pokémon.
        """
        return (f"{self.name} (Tipo: {self.tipo1}/{self.tipo2 if self.tipo2 else 'Nenhum'}, "
                f"HP: {self.hp}, Ataque: {self.atk}, Defesa: {self.defs}, "
                f"Sp. Ataque: {self.sp_atk}, Sp. Defesa: {self.sp_defs}, Velocidade: {self.speed})")


class Attack:
    """
    Classe que representa um ataque com atributos detalhados.
    """
    def __init__(self, name, attack_type, category, power, accuracy, pp, effect):
        """
        Inicializa um ataque com atributos detalhados.
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
    """
    Classe que representa um Pokémon morto.
    """
    def __init__(self):
        self.name = "morto"


class Node:
    """
    Classe que representa um nó na árvore de decisão.
    """
    def __init__(self, pai, acao, escolha, dano, pkm1=None, pkm2=None, profundidade=None):
        """
        Inicializa um nó da árvore de decisão.
        :param pai: Nó pai (anterior na árvore).
        :param acao: Ação associada ao nó.
        :param escolha: Escolha associada ao nó.
        :param dano: Dano ou resultado da ação.
        :param pkm1: Pokémon 1 (opcional).
        :param pkm2: Pokémon 2 (opcional).
        :param profundidade: Profundidade do nó na árvore.
        """
        self.pai = pai
        self.profundidade = profundidade if profundidade is not None else pai.profundidade + 1
        self.visitado = False
        self.filhos = []
        self.acao = acao
        self.escolha = escolha
        self.dano = dano
        self.pkm1 = pkm1
        self.pkm2 = pkm2

class Node_final:
    """
    Classe que representa um nó final na árvore de decisão.
    """
    def __init__(self, pai, dado, acao, escolha):
        """
        Inicializa um nó final da árvore de decisão.
        :param pai: Nó pai (anterior na árvore).
        :param acao: Ação associada ao nó.
        :param escolha: Escolha associada ao nó.
        :param dado: Dano ou resultado da ação.
        :param profundidade: Profundidade do nó na árvore.
        """
        self.pai = pai
        self.profundidade = pai.profundidade+1
        self.visitado = False
        self.dado = dado
        self.acao = acao
        self.escolha = escolha
        self.filhos = []

class Candidato:
    def __init__(self, valor, no, hps):
        self.valor = valor
        self.no = no
        self.hps = hps