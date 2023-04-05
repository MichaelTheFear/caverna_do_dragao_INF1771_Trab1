import sys
import pygame
import matplotlib.pyplot as plt


TAMANHO_DO_BLOCO = 8
NUMERO_DE_LINHAS = 105
NUMERO_DE_COLUNAS = 200
LARGURA_DA_TELA = NUMERO_DE_COLUNAS * TAMANHO_DO_BLOCO
ALTURA_DA_TELA = NUMERO_DE_LINHAS * TAMANHO_DO_BLOCO
LINHAS_DE_APOIO = True

MAPA = []


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
    else:
        return (0, 0, 0)


def loadMapa() -> None:
    with open('mapa.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            MAPA.append([])
            for j in range(len(lines[i]) - 1):
                MAPA[i].append(lines[i][j])
                # botar pra atualizar o numero de linhas e colunas e a largura e altura da tela


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((0, 0, 0))
    for linha in range(len(MAPA)):
        for coluna in range(len(MAPA[linha])):
            pygame.draw.rect(SCREEN, getCor(MAPA[linha][coluna]), (coluna * TAMANHO_DO_BLOCO, linha * TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO))
            if LINHAS_DE_APOIO:
                pygame.draw.rect(SCREEN, (0, 0, 0), (coluna * TAMANHO_DO_BLOCO, linha * TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO, TAMANHO_DO_BLOCO), 1)

    

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()



loadMapa()
main()



