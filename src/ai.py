from copy import deepcopy
from itertools import combinations
from random import choice, randint, random, seed
from math import exp
from json import dumps
from time import sleep

seed()

"""

personagens = {
        'Hank': [1.5, 11],
        'Diana': [1.4, 11],
        'Sheila': [1.3, 11],
        'Presto': [1.2, 11],
        'Bob': [1.1, 11],
        'Eric': [1.0, 11]
    }
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
        
        index_pesonagem_em_fase_1 = randint(0,len(solucao[self.FASES[index_1]])-1) #A:["Hank","Eric"]
        index_pesonagem_em_fase_2 = randint(0,len(solucao[self.FASES[index_2]])-1)
        
        personagem_1 = solucao[self.FASES[index_1]][index_pesonagem_em_fase_1]
        personagem_2 = solucao[self.FASES[index_2]][index_pesonagem_em_fase_2]

        while personagem_1 == personagem_2:
            index_pesonagem_em_fase_1 = randint(0,len(solucao[self.FASES[index_1]])-1) #A:["Hank","Eric"]
            index_pesonagem_em_fase_2 = randint(0,len(solucao[self.FASES[index_2]])-1)
        
            personagem_1 = solucao[self.FASES[index_1]][index_pesonagem_em_fase_1]
            personagem_2 = solucao[self.FASES[index_2]][index_pesonagem_em_fase_2]

            if personagem_2 in solucao[self.FASES[index_1]] or personagem_1 in solucao[self.FASES[index_2]]:
                return self.gera_vizinhanca(solucao)

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
"""

class AlgoritimosAI():
    TOTAL_DE_ITERACOES_ANNEALING = 1e5
    ANNEALING_FATOR_PARADA = TOTAL_DE_ITERACOES_ANNEALING 
    ANNEALING_EARLY_STOP = TOTAL_DE_ITERACOES_ANNEALING // 10
    MULTIPLICADOR_TEMPERATURA = TOTAL_DE_ITERACOES_ANNEALING // 100
    FASES = "123456789BCEGHIJKLNOPQSTUWYZ" # tamanho fases
    PERSONAGENS = ['Hank', 'Diana', 'Sheila', 'Presto', 'Bob', 'Eric']
    VALOR_PERSONAGEM = [1.5, 1.4, 1.3, 1.2, 1.1, 1.0]
    TAMANHO_FASES = len(FASES)
    min_fitness = 2000.00
    min_solucao = {}

    
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

    def print_solucao(self, solucao:dict):
        solucao_f = {}
        for fase in solucao:
            solucao_f[fase] = []
            for per_index in range(len(solucao[fase])):
                if solucao[fase][per_index]:
                    solucao_f[fase].append(self.PERSONAGENS[per_index])

        self.print_dict(solucao_f)

    def reset_personagens(self):
        for personagem in self.personagens:
            self.personagens[personagem][1] = 11
        

    def boltzman(self, delta:float, tempo:float) -> float:
        return exp(-abs(delta)/tempo)

    def sobre_somente_um(self, personagens: list[int]) -> bool:
        return sum(personagens) == 1
    

    def gera_solucao_aleatoria(self):
        solucao = {}
        for fase in self.FASES:
            solucao[fase] = [False for i in range(6)]
            
        personagens_uso = [11,11,11,11,11,10] # HANK,DIANA,SHEILA,PRESTO,BOB,ERIC
        index_validos = [0,1,2,3,4,5] #retirar do index valido a quando o uso do personagem chegar em 0

        for fase in self.FASES:
            random_personagem_index = index_validos[randint(0,len(index_validos)-1)] 
            solucao[fase][random_personagem_index] = True
            personagens_uso[random_personagem_index] -= 1
            if personagens_uso[random_personagem_index] == 0:
                index_validos.remove(random_personagem_index)
        
        
        
        i = len(index_validos)
        for index in range(i):
            index_personagem = index_validos[index]
            for p in range(personagens_uso[index_personagem]):
                while True:
                    fase = self.FASES[randint(0,len(self.FASES)-1)]
                    if solucao[fase][index_personagem] == False:
                        solucao[fase][index_personagem] = True
                        break


        return solucao
    

    def personagem_aleatorio(self, personagens: list[bool]) -> int:
        personagens_index_validos = []
        for i in range(len(personagens)):
            if personagens[i]:
                personagens_index_validos.append(i)
        return personagens_index_validos[randint(0,len(personagens_index_validos)-1)]
    
    def heuristica_vizinhanca(self, nfase:int)-> int:
        return 2.5 * ((nfase - 1 )/ len(self.FASES))

    def gera_vizinhanca(self, solucao: dict[str,list[bool]]) -> dict[str,list[bool]]:
        # a media de personagens por fase é 2.5
        # pega uma fase aleatoria cuja a media seja maior que 2.5
        # pega um personagem aleatorio dessa fase e troca de fase
        #while self.calcula_tempo_solucao(solucao) < self.min_fitness:
        fases25 = []
        todas_as_fases_indexes = [i for i in range(len(self.FASES))]
        for index in range(len(self.FASES)):
            fase = self.FASES[index]
            if self.calcula_tempo_composicao(solucao[fase]) > self.heuristica_vizinhanca(index) and solucao[fase].count(True) > 1:
                fases25.append(fase)
        fase = fases25[randint(0,len(fases25)-1)]
        todas_as_fases_indexes.remove(self.FASES.index(fase))
        #pega personagem valido dessa fase
        personagem_index = self.personagem_aleatorio(solucao[fase])
        #pega uma fase aleatoria que nao seja a fase atual e que nao tenha esse personagem
        while True:
            i = randint(0,len(todas_as_fases_indexes)-1)
            fase_key = self.FASES[todas_as_fases_indexes[i]]
            if not solucao[fase_key][personagem_index]:
                solucao[fase][personagem_index] = False
                solucao[fase_key][personagem_index] = True
                break

        return solucao

    
    def calcula_tempo_composicao(self, envolvidos: list[bool]) -> int:
        soma = 0 
        for i in range(len(envolvidos)):
            if envolvidos[i]:
                soma += self.VALOR_PERSONAGEM[i]

        return soma
    
    def calcula_tempo_solucao(self, solucao: dict[str,list[bool]]) -> int:
        tempo = 0
        for fase in solucao:
            tempo += self.dificuldade[fase]/self.calcula_tempo_composicao(solucao[fase])
        return tempo

    
    def fitness(self, solucao: dict[str,list[str]]) -> int:
        return self.calcula_tempo_solucao(solucao)
    
    def escalonador(self, iteracoes_anneling:int) -> float:
        return self.MULTIPLICADOR_TEMPERATURA / (self.min_fitness) * iteracoes_anneling

    def resolve_por_anneling(self) -> dict[str,list[str]]:
        while True:
            try:
                atual = self.gera_solucao_aleatoria()
                break
            except Exception:
                continue
        

        total_max_de_iteracoes = self.ANNEALING_FATOR_PARADA 
        total_max_de_iteracoes_sem_mudanca = self.ANNEALING_EARLY_STOP 
        
        i = 0
        estado_mudado = 1
        temperatura = 10
        T = self.escalonador(1)
        candidata_fitness = 2000

        while i < total_max_de_iteracoes:
            if random() > self.boltzman(self.min_fitness - candidata_fitness, T):
                candidata = self.gera_solucao_aleatoria()
                flag = "Boltz"
            else:
                candidata = self.gera_vizinhanca(deepcopy(self.min_solucao) if self.min_solucao != {} else self.gera_solucao_aleatoria())
                flag = "Vizinhança"

            
           
            i += 1
            candidata_fitness = self.fitness(candidata)
            T = self.escalonador(i)

            if candidata_fitness < self.min_fitness:
                self.min_solucao = deepcopy(candidata)
                self.min_fitness = candidata_fitness
                print(f"Tempo: {self.min_fitness} {flag}")
                sleep(0.1)
                estado_mudado = 0
            else:
                estado_mudado += 1
                if i >= total_max_de_iteracoes  or estado_mudado >= total_max_de_iteracoes_sem_mudanca:
                    return self.min_solucao

        return self.min_solucao
    
    def test(self):
        solucao = self.resolve_por_anneling()
        tempo = self.fitness(solucao)
        self.print_solucao(solucao)
        print(f"Tempo: {self.min_fitness}")

        
        
            

AlgoritimosAI().test()
