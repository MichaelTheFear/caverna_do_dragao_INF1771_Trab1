class AlgoritimosAI():

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


    """
    Função Simulated-Annealing(Problema, Escalonamento) retorna um estado
    que é o máximo local
        Inicio
        EstadoAtual ← Criar-Nó(Problema[EstadoInicial])
        loop do
        t = t + 1
        T ← Escalonamento[t]
        Se T = 0 então retorna EstadoAtual
        Próximo ← seleciona um sucessor do EstadoAtual aleatoriamente
        ΔE ← Próximo[Valor] – EstadoAtual[Valor]
        se ΔE > 0 então EstadoAtual ← Próximo
        senão EstadoAtual ← Próximo somente com probabilidade e
        ΔE/T
        fim 
    """
    def annealing(self, personagens:list[str], fases: list[str]) -> int:
        estado_atual = 0
        t = 0
        while True:
            T = fases[t]




            t += 1
        