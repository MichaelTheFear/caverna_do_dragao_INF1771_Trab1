import sys
import pygame
import time
from busca import MAPA, AEstrela

# convert dict to list in this order 0123456789BCEGHIJKLNOPQSTUWYZ
def dictToList(d)->list:
    lista = []
    for key in "0123456789BCEGHIJKLNOPQSTUWYZ":
        try:
            lista.append(d[key])
        except KeyError:
            pass
    return lista



class Caverna_Do_Dragao:
    VELOCIDADE_ANIMACAO:int = 1e10 # quanto maior mais rapido
    SEM_ANIMACAO:bool = True
    TAMANHO_DO_BLOCO:int = 6
    NUMERO_DE_LINHAS:int = MAPA.height + 2
    NUMERO_DE_COLUNAS:int = MAPA.width +2
    LARGURA_DA_TELA:int = NUMERO_DE_COLUNAS * TAMANHO_DO_BLOCO
    ALTURA_DA_TELA:int = NUMERO_DE_LINHAS * TAMANHO_DO_BLOCO
    LINHAS_DE_APOIO:bool = False
    EVENTOS:list[tuple[int,int]] = dictToList(MAPA.eventos)
    PROXIMO_EVENTO:int = 0
    EVENTO_ATUAL:int = -1
    AESTRELA:AEstrela = AEstrela()
    CAMINHO:list[tuple[int,int]] = []
    NOMES_EVENTOS = "0123456789BCEGHIJKLNOPQSTUWYZ"

    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.LARGURA_DA_TELA, self.ALTURA_DA_TELA))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill((255, 255, 255))
        self.limpa_mapa()
        self.custoAEstrela = 0


        
    def get_cor(self, value: str) -> tuple:
        if value == '.':
            return (186, 178, 127)
        elif value == 'F':
            return (47, 64, 29)
        elif value == 'R':
            return (105, 104, 102)
        elif value == 'D':
            return (82, 32, 32)
        elif value == 'A':
            return (32, 33, 82)
        elif value == 'M':
            return (82, 57, 32)
        else:
            return (0, 0, 0)
    
    def desenha_quadrado(self, linha:int, coluna:int,cor = None) -> None:
            pygame.draw.rect(self.SCREEN, self.get_cor(MAPA.mapa[linha][coluna]) if cor==None else cor, (coluna * self.TAMANHO_DO_BLOCO, linha * self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO))
            if self.LINHAS_DE_APOIO:
                pygame.draw.rect(self.SCREEN, (0, 0, 0), (coluna * self.TAMANHO_DO_BLOCO, linha * self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO), 1)

    def desenha_quadrado_animado(self, linha:int, coluna:int,cor = None) -> None:
        self.desenha_quadrado(linha, coluna, cor=(255, 215, 0))
        pygame.display.update()
        self.CLOCK.tick(self.VELOCIDADE_ANIMACAO)

    def limpa_mapa(self)  -> None:
        for linha in range(MAPA.height):
            for coluna in range(MAPA.width):
                if (linha,coluna) not in self.CAMINHO:
                    self.desenha_quadrado(linha, coluna)
                else:
                    self.desenha_quadrado(linha, coluna, (7, 232, 240))
        
        pygame.display.update()
        self.CLOCK.tick(self.VELOCIDADE_ANIMACAO)
        
        inicio = self.EVENTOS[self.EVENTO_ATUAL]
        try:
            fim = self.EVENTOS[self.PROXIMO_EVENTO]
        except IndexError:
            self.PROXIMO_EVENTO = len(self.EVENTOS)-1
            fim = self.EVENTOS[-1]
        self.desenha_quadrado(inicio[0], inicio[1], (209, 240, 7))
        self.desenha_quadrado(fim[0], fim[1], (240, 170, 7))

    

    def gera_caminho_todo(self) -> None:
        flag = False
        
        while True:
            try:
                caminho = self.proximo_caminho()
                busca = next(caminho) 
            except StopIteration:
                flag = True
            self.limpa_mapa()
            print(f"este evento: {self.NOMES_EVENTOS[self.EVENTO_ATUAL]} proximo evento: {self.NOMES_EVENTOS[self.PROXIMO_EVENTO]}")

            if flag:
                break
            while True:
                no = next(busca)
                if not self.SEM_ANIMACAO:
                    if no["estado"] == "buscando...":
                        for i in no["vizinhos"]:
                            self.desenha_quadrado_animado(i[0], i[1], cor=(255, 215, 0))
                    elif no["estado"] == "fim":
                        for i in no["caminho"]:
                            self.desenha_quadrado_animado(i[0], i[1], cor=(7, 232, 240))
                
                if no["estado"] == "fim":
                    print(no["caminho"])
                    self.CAMINHO.extend(no["caminho"])
                    break
                yield

        self.limpa_mapa()
        



    def gera_caminho_todo_de_uma_vez(self) -> None:
        comeco = time.time()
        caminhos = self.AESTRELA.solve_todos_os_caminhos(nodes=self.EVENTOS)
        for caminho in caminhos:
            self.desenha_quadrado(caminho[0], caminho[1], cor=(209, 240, 7))
        
        pygame.display.update()
        self.CLOCK.tick(self.VELOCIDADE_ANIMACAO)
        fim = time.time()
        print(f"Numero de passos do caminho final: {len(caminhos)} \n Numero de passos do A*: {self.AESTRELA.total_de_passos}")
        print(f"Tempo de execução: {fim - comeco}")
        
    

    def proximo_caminho(self) -> None:
        self.EVENTO_ATUAL += 1
        self.PROXIMO_EVENTO += 1
        if self.PROXIMO_EVENTO != len(self.EVENTOS):
            '''caminho = self.AESTRELA.solve(self.EVENTOS[self.EVENTO_ATUAL], self.EVENTOS[self.PROXIMO_EVENTO])
            for coord in caminho:
                self.custoAEstrela += MAPA.getValor(coord)'''
            yield self.AESTRELA.solve(self.EVENTOS[self.EVENTO_ATUAL], self.EVENTOS[self.PROXIMO_EVENTO])
    
    def game_start(self) -> None:
        caminho_todo:bool = False
        caminho_todo_gerador = self.gera_caminho_todo()
        
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_f:
                        caminho_todo = not caminho_todo
                        comeco = time.time()
                        print(MAPA.aStarCost)
                    
                    if evento.key == pygame.K_x:
                        self.gera_caminho_todo_de_uma_vez()
                    
                    if evento.key == pygame.K_SPACE:
                        self.limpa_mapa()
                        caminho = self.proximo_caminho()
                        busca = next(caminho)
                        no = next(busca)
                        while no["estado"] != "fim":
                            no = next(busca)
                            if no["estado"] == "buscando...":
                                for i in no["vizinhos"]:
                                    self.desenha_quadrado_animado(i[0], i[1], cor=(255, 215, 0))
                            elif no["estado"] == "fim":
                                self.CAMINHO.extend(no["caminho"])
                                for i in no["caminho"]:
                                    self.desenha_quadrado_animado(i[0], i[1], cor=(7, 232, 240))
                        print(MAPA.aStarCost)
            if caminho_todo:
                try:
                    next(caminho_todo_gerador)
                except StopIteration:
                    print(f"Caminho desenhando {time.time() - comeco} segundos")
                    caminho_todo = False
                                    
            pygame.display.update()




Caverna_Do_Dragao().game_start()