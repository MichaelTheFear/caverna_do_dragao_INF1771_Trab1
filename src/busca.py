# [Agilidade, Quantidade de vezes usado]
PERSONAGENS = {
    "Hank": [1.5 , 0],
    "Diana": [1.4, 0],
    "Sheila": [1.3, 0],
    "Presto": [1.2,0],
    "Bob": [1.1,0],
    "Eric": [1.0,0]
}
'''
MAPA = []

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
'''



class Mapa():
    def __init__(self):
        with open('mapa.txt', 'r') as file:
            lines = file.readlines()
        
        self.height = len(lines)
        self.width = max(len(line) for line in lines)

        self.mapa = []
        self.eventos = {}
        for i in range(self.height):
            row = []
            for j in range(len(lines[i])):
                row.append(lines[i][j])
                if lines[i][j] in '0123456789BCEGHIJKLNOPQSTUWYZ':
                    self.eventos[lines[i][j]] = (i, j)
            self.mapa.append(row)
 
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
        
    def getValor(self, coord: tuple[int, int]) -> int:
        quadrado = self.mapa[coord[0]][coord[1]]
        
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
        

MAPA = Mapa()


class Node():
    def __init__(self, coord, parent):
        self.coord = coord
        self.parent = parent
        
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        if other == None:
            return False

        return self.coord == other.coord


def manhattan(current: Node, goal: Node) -> int:
    return (abs(goal.coord[0] - current.coord[0]) + abs(goal.coord[1] - current.coord[1]))

class CoordList():
    def __init__(self):
        self.coordList = []

    def add(self, node:Node) -> None:
        self.coordList.append(node)
    
    def contains_coord(self, coord) -> bool: #ver os tipos do coord
        return any(node.coord == coord for node in self.coordList)
    
    def empty(self) -> bool:
        return len(self.coordList) == 0
    
    def remove(self) -> Node:
        if self.empty():
            raise Exception("empty OpenList.coordList")
        else:
            node = self.coordList[-1]
            self.coordList = self.coordList[:-1]
            return node


class AEstrela:
    def neighbors(self, node:Node) -> list[Node]:
        row, col = node.coord
        candidates = [
            Node((row - 1, col), node),
            Node((row + 1, col), node),
            Node((row, col - 1), node),
            Node((row, col + 1), node)
        ]

        result = []
        for candNode in candidates:
            r, c = candNode.coord
            if 0 <= r < MAPA.height and 0 <= c < MAPA.width:
                result.append(candNode)
        return result
    
    def solve_todos_os_caminhos(self, nodes:list[tuple[int,int]]) -> list[list[tuple[int,int]]]:
        res = []
        for index in range(len(nodes) - 1):
            current = self.solve(nodes[index], nodes[index+1])
            print(f"current: {current}")
            while True:
                try:
                    current_path = next(current)
                    if current_path["estado"] == "fim":
                        res.extend(current_path["caminho"])
                except:
                    break
    
    def solve(self, start:tuple[int,int], goal:tuple[int,int]) -> list[tuple[int,int]]:
        #Creating start and goal nodes
        startNode = Node(start, None)
        goalNode = Node(goal, None)

        #Creating Open and Closed list
        openList:list[Node] = []
        closedList:list[Node] = []

        #Adding startNode to openList
        openList.append(startNode)

        #Run the algorithm
        while len(openList) > 0:

            #Get the current node
            currentNode = openList[0]
            currentIndex = 0
            for index, node in enumerate(openList):
                if node.f < currentNode.f:
                    currentNode = node
                    currentIndex = index
            
            #Remove node with smaller f from openList and add it to closedList
            openList.pop(currentIndex)
            closedList.append(currentNode)

            #Found the goal
            if currentNode == goalNode:
                path=[]
                node = currentNode
                while node != None:
                    path.append(node.coord)
                    node = node.parent
                yield {
                    "estado": "fim",
                    "caminho":path[::-1]
                    }
                break
            
            neighbors_coords = [node.coord for node in self.neighbors(currentNode)]
            
            yield {
                "estado": "buscando...",
                "vizinhos": neighbors_coords,
                "atual": currentNode.coord
            }
            
            for neighborNode in self.neighbors(currentNode):
                if neighborNode in closedList:
                    continue
                
                tentative_g = currentNode.g + MAPA.getValor(neighborNode.coord)
                if neighborNode not in openList:
                    openList.append(neighborNode)
                else:
                    for node in openList:
                        if node == neighborNode:
                            neighborNode = node
                            break

                    if tentative_g >= neighborNode.g:
                        continue

                neighborNode.parent = currentNode
                neighborNode.g = tentative_g
                neighborNode.h = manhattan(neighborNode, goalNode)
                neighborNode.f = neighborNode.g + neighborNode.h

            
                
                


