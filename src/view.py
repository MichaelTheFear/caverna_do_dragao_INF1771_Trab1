import sys
import pygame
from busca import MAPA, AEstrela

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



