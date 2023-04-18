from itertools import combinations
from random import randint, random
from math import exp
from json import dumps

class AlgoritimosAI():
    ANNEALING_FATOR_PARADA = 5 # em porcentagem
    ANNEALING_EARLY_STOP = 1 # em porcentagem
    FASES = "123456789BCEGHIJKLNOPQSTUWYZ"

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
    MIN_COEFICIENTE = min(dificuldade.values())
    MAX_COEFICIENTE = max(dificuldade.values())



    def calcula_tempo(self, personagens:list[str], fase: str) -> int:
        tempo = 0
        for personagem in personagens:
            tempo += self.personagens[personagem][0]
        return self.dificuldade[fase] // tempo


    def calcula_tempo_fase(self,personagens:list[str],dificulade:int):
        somatorio = 0
        for personagem in personagens:
            somatorio += self.personagens[personagem][0]
        return dificulade / somatorio

    def combincacao(self,personagens:list[str]) -> list[list[str]]:
        personagens_validos = []
        res = []
        for personagem in personagens:
            if self.personagens[personagem][1] != 11:
                personagens_validos.append(personagem)

        for i in range(1, len(personagens_validos)+1):
            for comb in combinations(personagens_validos, i):
                res.append(list(comb))
        
        return res
        

    def resolve_por_anneling(self,personagens:list[str] , fases:list[str]) -> dict[str,list[str]]:
        solucao = {}
        for fase in fases:
            solucao[fase] = self.annealing(self.combincacao(personagens),self.dificuldade[fase])
            for personagem in solucao[fase][0]:
                self.personagens[personagem][1] += 1
        return solucao

    def escolhe_estado(self, estados:list[list[float]],coeficente_fase:int) -> list[float]:
        #heuristica de estados aumentar a probabilidade de escolher um estado com indice menor se o coeficiente for menor
        coeficiente = coeficente_fase / self.MAX_COEFICIENTE
        index = int(len(estados)*coeficiente*random()) + 1 
        return estados.pop(index)

    def boltzman(self, delta:int, tempo:int) -> float:
        return exp(-delta/tempo)

    def annealing(self, estados:list[list[float]], coeficiente_fase:int) -> int:
        melhor_estado = estados[0]
        t_melhor_estado = self.calcula_tempo_fase(melhor_estado,coeficiente_fase)
        total_max_de_iteracoes = len(estados) * self.ANNEALING_FATOR_PARADA // 100
        total_max_de_iteracoes_sem_mudanca = len(estados) * self.ANNEALING_EARLY_STOP // 100
        i = 0
        melhor_estado_mudado = 0
        while i < total_max_de_iteracoes:
            i += 1
            estado = self.escolhe_estado(estados, coeficiente_fase)
            t_estado_atual = self.calcula_tempo_fase(estado,coeficiente_fase)
            delta_estado = t_estado_atual - t_melhor_estado
            if t_estado_atual < t_melhor_estado or random() > self.boltzman(delta_estado,i):
                t_melhor_estado = t_estado_atual
                melhor_estado = estado
                melhor_estado_mudado = 0
            else:
                melhor_estado_mudado += 1
                if i >= total_max_de_iteracoes  or melhor_estado_mudado >= total_max_de_iteracoes_sem_mudanca:
                    return melhor_estado , t_melhor_estado

        
        return melhor_estado, t_melhor_estado
        
    def test(self):
        resultado = self.resolve_por_anneling(self.personagens.keys(),self.FASES)
        print(dumps(resultado,indent=4))
        print(dumps(self.personagens,indent=4))
        total = 0
        for fase in resultado:
            total += resultado[fase][1]
        print(f"total ecnontrado {total}")

AlgoritimosAI().test()
