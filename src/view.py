import sys
import pygame
from busca import MAPA, AEstrela
"""

TAMANHO_DO_BLOCO = 8
NUMERO_DE_LINHAS = 105
NUMERO_DE_COLUNAS = 200
LARGURA_DA_TELA = NUMERO_DE_COLUNAS * TAMANHO_DO_BLOCO
ALTURA_DA_TELA = NUMERO_DE_LINHAS * TAMANHO_DO_BLOCO
LINHAS_DE_APOIO = False


def getCor(value: str) -> tuple:
    if value == '.':
        return (222, 219, 133)
    elif value == 'F':

        return (50, 168, 82)
    elif value == 'R':

        return (200, 200, 200)
    elif value == 'D':

        return (255, 0, 0)
    elif value == 'A':

        return (0, 0, 255)
    elif value == 'M':

        return (139, 69, 19)
    elif value == '0':
        return (255, 100, 20)
    elif value == '1':
        return (255, 100, 20)
    else:
        return (0, 0, 0)


i = 0
j = 1
eventos = MAPA.eventos
busca = AEstrela().solve(eventos["0"], eventos["1"])

print(eventos)
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((0, 0, 0))

    for linha in range(MAPA.height):
        for coluna in range(MAPA.width):
            pygame.draw.rect(SCREEN, getCor(MAPA.mapa[linha][coluna]), (coluna * TAMANHO_DO_BLOCO, linha * TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO))
            if LINHAS_DE_APOIO:
                pygame.draw.rect(SCREEN, (0, 0, 0), (coluna * TAMANHO_DO_BLOCO, linha * TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO), 1)

    

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
            

                if evento.key == pygame.K_SPACE:
                    no = next(busca)
                    while no["estado"] != "fim":
                        no = next(busca)
                        if no["estado"] == "buscando...":
                            for i in no["vizinhos"]:
                                pygame.draw.rect(SCREEN, (255, 0, 255), (i[1] * TAMANHO_DO_BLOCO, i[0] * TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO))
                                pygame.display.update()
                                CLOCK.tick(500)
                        elif no["estado"] == "fim":
                            for i in no["caminho"]:
                                
                                pygame.draw.rect(SCREEN, (255, 215, 0), (i[1] * TAMANHO_DO_BLOCO, i[0] * TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO))
                                pygame.display.update()
                                CLOCK.tick(500)



                   
                        
                        

        pygame.display.update()

        
main()
"""

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
    TAMANHO_DO_BLOCO = 8
    NUMERO_DE_LINHAS = 105
    NUMERO_DE_COLUNAS = 200
    LARGURA_DA_TELA = NUMERO_DE_COLUNAS * TAMANHO_DO_BLOCO
    ALTURA_DA_TELA = NUMERO_DE_LINHAS * TAMANHO_DO_BLOCO
    LINHAS_DE_APOIO = False
    EVENTOS = dictToList(MAPA.eventos)
    PROXIMO_EVENTO = 0
    EVENTO_ATUAL = -1
    AESTRELA = AEstrela()
    

    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.LARGURA_DA_TELA, self.ALTURA_DA_TELA))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill((0, 0, 0))
        self.limpa_mapa()


        
    def get_cor(self, value: str) -> tuple:
        if value == '.':
            return (222, 219, 133)
        elif value == 'F':
            return (50, 168, 82)
        elif value == 'R':
            return (200, 200, 200)
        elif value == 'D':
            return (255, 0, 0)
        elif value == 'A':
            return (0, 0, 255)
        elif value == 'M':
            return (139, 69, 19)
        else:
            return (0, 0, 0)
    
    def desenha_quadrado(self, linha:int, coluna:int) -> None:
        pygame.draw.rect(self.SCREEN, self.get_cor(MAPA.mapa[linha][coluna]), (coluna * self.TAMANHO_DO_BLOCO, linha * self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO))
        if self.LINHAS_DE_APOIO:
            pygame.draw.rect(self.SCREEN, (0, 0, 0), (coluna * self.TAMANHO_DO_BLOCO, linha * self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO), 1)

    def limpa_mapa(self)  -> None:
        for linha in range(MAPA.height):
            for coluna in range(MAPA.width):
                self.desenha_quadrado(linha, coluna)

    def proximo_caminho(self) -> None:
        self.EVENTO_ATUAL += 1
        self.PROXIMO_EVENTO += 1
        yield AEstrela().solve(self.EVENTOS[self.EVENTO_ATUAL], self.EVENTOS[self.PROXIMO_EVENTO])
    
    def game_start(self) -> None:
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    self.limpa_mapa()
                    caminho = self.proximo_caminho()
                    busca = next(caminho)
                    if evento.key == pygame.K_SPACE:
                        no = next(busca)
                        while no["estado"] != "fim":
                            no = next(busca)
                            if no["estado"] == "buscando...":
                                for i in no["vizinhos"]:
                                    pygame.draw.rect(self.SCREEN, (255, 0, 255), (i[1] * self.TAMANHO_DO_BLOCO, i[0] * self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO))
                                    pygame.display.update()
                                    self.CLOCK.tick(500)
                            elif no["estado"] == "fim":
                                for i in no["caminho"]:
                                    
                                    pygame.draw.rect(self.SCREEN, (255, 215, 0), (i[1] * self.TAMANHO_DO_BLOCO, i[0] * self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO, self.TAMANHO_DO_BLOCO))
                                    pygame.display.update()
                                    self.CLOCK.tick(500)



                    
                            
                            

            pygame.display.update()




Caverna_Do_Dragao().game_start()