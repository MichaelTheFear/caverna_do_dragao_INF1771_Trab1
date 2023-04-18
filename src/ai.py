import itertools
from random import randint, random
from math import exp

class AlgoritimosAI():
    ANNEALING_FATOR_PARADA = 75 # em porcentagem
    ANNEALING_EARLY_STOP = 25 # em porcentagem

    personagens = {
        
        'Hank': [1.5, 0],
        'Diana': [1.4, 0],
        'Sheila': [1.3, 0],
        'Presto': [1.2, 0],
        'Bob': [1.1, 0],
        'Eric': [1.0, 0]
    }
    
    dificuldade = {
        '0': 1,
        '1': 10,
        '2': 20,
        '3': 30,
        '4': 60,
        '5': 65,
        '6': 70,
        '7': 75,
        '8': 80,
        '9': 85,
        'B': 90,
        'C': 95,
        'E': 100,
        'G': 110,
        'H': 120,
        'I': 130,
        'J': 140,
        'K': 150,
        'L': 160,
        'N': 170,
        'O': 180,
        'P': 190,
        'Q': 200,
        'S': 210,
        'T': 220,
        'U': 230,
        'W': 240,
        'Y': 250,
        'Z': 260
    }


    def calcula_tempo(self, personagens:list[str], fase: str) -> int:
        tempo = 0
        for personagem in personagens:
            tempo += self.personagens[personagem][0]
        return self.dificuldade[fase] // tempo


    def calcula_tempo_fase(self,personagens,dificulade):
        somatorio = 0
        for personagem in personagens:
            somatorio += personagem[0]
        return dificulade / somatorio

    def permutacao(self,personagens:list[str]) -> list[list[str]]:
        return list(itertools.permutations(personagens))

    def resolve_por_anneling(self,personagens:list[str] , fases:list[str]) -> dict[str,list[str]]:
        solucao = {}
        for fase in fases:
            solucao[fase] = self.annealing(self.permutacao(personagens),self.dificuldade[fase])
        return solucao

    def escolhe_estado(self, estados:list[list[float]]) -> list[float]:
        return estados.pop(randint(0,len(estados)-1))

    def boltzman(self, delta:int, tempo:int) -> float:
        return exp(-delta/tempo)

    def annealing(self, estados:list[list[float]], coeficiente_fase:int) -> int:
        melhor_estado = estados[0]
        total_max_de_iteracoes = len(estados) * 100/ self.ANNEALING_FATOR_PARADA
        i = 0
        melhor_estado_mudado = 0
        while i < total_max_de_iteracoes:
            estado = self.escolhe_estado(estados)
            t_melhor_estado = self.calcula_tempo_fase(melhor_estado,coeficiente_fase)
            t_estado_atual = self.calcula_tempo_fase(estado,coeficiente_fase)
            delta_estado = t_estado_atual - t_melhor_estado
            if t_estado_atual < t_melhor_estado or random() > self.prob(delta_estado,0):
                melhor_estado = estado
                melhor_estado_mudado = 0
            else:
                melhor_estado_mudado += 1
                if melhor_estado_mudado > total_max_de_iteracoes * self.ANNEALING_EARLY_STOP / 100:
                    return melhor_estado

            i += 1
        
        return melhor_estado

        
