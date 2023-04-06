MAPA = []

# [Agilidade, Quantidade de vezes usado]
PERSONAGENS = {
    "Hank": [1.5 , 0],
    "Diana": [1.4, 0],
    "Sheila": [1.3, 0],
    "Presto": [1.2,0],
    "Bob": [1.1,0],
    "Eric": [1.0,0]
}


def loadMapa() -> None:
    with open('mapa.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            MAPA.append([])
            for j in range(len(lines[i]) - 1):
                MAPA[i].append(lines[i][j])
                # botar pra atualizar o numero de linhas e colunas e a largura e altura da tela


def getDificuldade(evento: str) -> int:
    if evento == '1':
        return 10
    elif evento == '2':
        return 20
    elif evento == '3':
        return 30
    elif evento == '4':
        return 60
    elif evento == '5':
        return 65
    elif evento == '6':
        return 70
    elif evento == '7':
        return 75
    elif evento == '8':
        return 80
    elif evento == '9':
        return 85
    elif evento == 'B':
        return 90
    elif evento == 'C':
        return 95
    elif evento == 'E':
        return 100
    elif evento == 'G':
        return 110
    elif evento == 'H':
        return 120
    elif evento == 'I':
        return 130
    elif evento == 'J':
        return 140
    elif evento == 'K':
        return 150
    elif evento == 'L':
        return 160
    elif evento == 'N':
        return 170
    elif evento == 'O':
        return 180
    elif evento == 'P':
        return 190
    elif evento == 'Q':
        return 200
    elif evento == 'S':
        return 210
    elif evento == 'T':
        return 220
    elif evento == 'U':
        return 230
    elif evento == 'W':
        return 240
    elif evento == 'Y':
        return 250
    elif evento == 'Z':
        return 260

def getValor(quadrado: str) -> int:
    if quadrado == '.':
        return 1
    elif quadrado == 'R':
        return 5
    elif quadrado == 'D':
        return 10
    elif quadrado == 'F':
        return 15
    elif quadrado == 'A':
        return 20
    elif quadrado == 'M':
        return 100
    else:
        return 1

loadMapa()

class AEstrela:
    def neighbors(self, coord:tuple[int,int]) -> list[tuple[str, tuple[int, int]]]:
        row, col = coord
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result