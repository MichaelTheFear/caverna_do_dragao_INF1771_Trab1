from copy import deepcopy
from itertools import combinations
from random import choice, randint, random, seed
from math import exp
from json import dumps

seed()

class AlgoritimosAI():
    TOTAL_DE_ITERACOES_ANNEALING = 1e6
    ANNEALING_FATOR_PARADA = TOTAL_DE_ITERACOES_ANNEALING 
    ANNEALING_EARLY_STOP = TOTAL_DE_ITERACOES_ANNEALING // 50
    FASES = "123456789BCEGHIJKLNOPQSTUWYZ" # tamanho fases
    PERSONAGENS = ['Hank', 'Diana', 'Sheila', 'Presto', 'Bob', 'Eric']
    TAMANHO_FASES = len(FASES)
    min_fitness = 2000.00
    min_solucao = {}

    personagens = {
        'Hank': [1.5, 11],
        'Diana': [1.4, 11],
        'Sheila': [1.3, 11],
        'Presto': [1.2, 11],
        'Bob': [1.1, 11],
        'Eric': [1.0, 11]
    }
    
    dificuldade = {
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


    def print_dict(self, d:dict):
        print(dumps(d,indent=4))

    def reset_personagens(self):
        for personagem in self.personagens:
            self.personagens[personagem][1] = 11
        

    def boltzman(self, delta:float, tempo:float) -> float:
        return exp(-delta/tempo)


    def pega_personagen_aleatorio(self):
        if not self.sem_personagem_valido():
            raise Exception("Não tem personagem valido")
        todos_os_persoangem = list(self.personagens.keys())
        indice = randint(0,len(todos_os_persoangem)-1)
        if self.personagens[todos_os_persoangem[indice]][1] == 0:
            return self.pega_personagen_aleatorio()
        else:
            self.personagens[todos_os_persoangem[indice]][1] -= 1
        return todos_os_persoangem[indice]

    def sem_personagem_valido(self):
        soma = 0
        for vezes_uso in self.personagens.values():
            soma += vezes_uso[1]

        if soma > 0:
            return True
        return False
    
    def pega_fase_aleatoria(self):
        indice = randint(0,len(self.FASES)-1)
        return self.FASES[indice]
    

    def gera_solucao_aleatoria_valida_2(self):
        solucao = {}
        for fase in self.FASES:
            solucao[fase] = [self.pega_personagen_aleatorio()]
        

        while self.sem_personagem_valido():
            fase = self.pega_fase_aleatoria()
            try:
                solucao[fase].append(self.pega_personagen_aleatorio())
            except:
                break
            
        self.reset_personagens()
        return solucao

    def gera_composicao_valida_aleatoria(self, personagens: list[str]) -> list[str]:
        composicao = []
        for personagem in personagens:
            if self.personagens[personagem][1] != 0 and random() < 0.5:
                composicao.append(personagem)
                self.personagens[personagem][1] -= 1
        return composicao

    def gera_solucao_valida_aleatoria(self) -> dict[str,list[str]]:
        solucao = {}
        comeco = len(self.FASES)
        while comeco != 0:
            fase = self.FASES[comeco-1]
            solucao[fase] = self.gera_composicao_valida_aleatoria(self.personagens.keys())
            if len(solucao[fase]) == 0:
                self.reset_personagens()
                raise Exception("Nao foi possivel gerar uma solucao valida")
            comeco -= 1
        
        soma = 0
        for vezes_uso in self.personagens.values():
            soma += vezes_uso[1]
        
        self.reset_personagens()

        if soma < 1:
            raise Exception("Nao foi possivel gerar uma solucao valida")
        
        return solucao
    
    def gera_vizinhanca(self, solucao: dict[str,list[str]]) -> list[dict[str,list[str]]]:
        index_1 = randint(0,len(self.FASES)-1)
        index_2 = randint(0,len(self.FASES)-1)
        while index_1 != index_2: # arrumar para conseguir mexer em fases com uma so pessoa
            index_2 = randint(0,len(self.FASES)-1)
        
        index_pesonagem_em_fase_1 = randint(0,len(solucao[self.FASES[index_1]])-1)
        index_pesonagem_em_fase_2 = randint(0,len(solucao[self.FASES[index_2]])-1)
        personagem_1 = solucao[self.FASES[index_1]][index_pesonagem_em_fase_1]
        personagem_2 = solucao[self.FASES[index_2]][index_pesonagem_em_fase_2]

        solucao[self.FASES[index_1]][index_pesonagem_em_fase_1] = personagem_2
        solucao[self.FASES[index_2]][index_pesonagem_em_fase_2] = personagem_1
        return solucao
    
    def gera_vizinhanca_2(self,solucao):
        index_1 = randint(0,len(self.FASES)-1)
        index_2 = randint(0,len(self.FASES)-1)
        while index_1 != index_2:
            index_2 = randint(0,len(self.FASES)-1)
        
        key_1 = self.FASES[index_1]
        key_2 = self.FASES[index_2]
        solucao[key_1],solucao[key_2] = solucao[key_2],solucao[key_1]

        return solucao


    def calcula_tempo(self, envolvidos: list[str], fase: str) -> int:
        return self.dificuldade[fase] / sum([self.personagens[env][0] for env in envolvidos])

    #calcula tempo de uma solucao
    def calcula_tempo_solucao(self, solucao: dict[str,list[str]]) -> int:
        tempo = 0
        for fase in solucao:
            tempo += self.calcula_tempo(solucao[fase], fase)
        return tempo
    
    def fitness(self, solucao: dict[str,list[str]]) -> int:
        #mudar
        return self.calcula_tempo_solucao(solucao)

    def resolve_por_anneling(self) -> dict[str,list[str]]:
        while True:
            try:
                atual = self.gera_solucao_aleatoria_valida_2()
                break
            except Exception:
                continue
        
        atual_fitness = self.fitness(atual)

        total_max_de_iteracoes = self.ANNEALING_FATOR_PARADA 
        total_max_de_iteracoes_sem_mudanca = self.ANNEALING_EARLY_STOP 
        
        i = 0
        estado_mudado = 0
        temperatura = 10
        T = temperatura / 1
        delta_estado = 0

        while i < total_max_de_iteracoes:
            try:
                if random() < 0.5:
                    candidata = self.gera_solucao_aleatoria_valida_2()
                    flag = "Boltz"
                else:
                    if random() > 0.7:
                        candidata = self.gera_vizinhanca(atual if self.min_solucao == {} else self.min_solucao)
                        flag = "Vizinhança"
                    else:
                        candidata = self.gera_vizinhanca_2(atual if self.min_solucao == {} else self.min_solucao)
                        flag = "Vizinhança_2"
            except Exception:
                continue
            i += 1
            candidata_fitness = self.fitness(candidata)
            if candidata_fitness < self.min_fitness:
                self.min_solucao = candidata
                self.min_fitness = candidata_fitness
                #self.print_dict(self.min_solucao)
                print(f"Tempo: {self.min_fitness} {flag}")

            delta_estado = candidata_fitness - atual_fitness
            T = 1000 / self.min_fitness

            #print(f"i = {i} BTZ {self.boltzman(delta_estado,T)}")
            if delta_estado < 0 or random() < self.boltzman(delta_estado,T):
                atual = candidata
                atual_fitness = candidata_fitness
                estado_mudado = 0
            else:
                estado_mudado += 1
                if i >= total_max_de_iteracoes  or estado_mudado >= total_max_de_iteracoes_sem_mudanca:
                    return self.min_solucao

        return self.min_solucao
    
    def test(self):
        solucao = self.resolve_por_anneling()
        tempo = self.calcula_tempo_solucao(solucao)
        self.print_dict(solucao)
        print(f"Tempo: {tempo}")

        
        
            

AlgoritimosAI().test()
