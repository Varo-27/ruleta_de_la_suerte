import os
import time
from models import Jugador, Panel
import pygame
from textwrap import wrap

class Vista():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 800))
        self.fuente = pygame.font.Font("Gordita-Black.otf", 30)
        self.colores = {
                        'rojo': (255, 179, 186),
                        'verde': (186, 255, 201),
                        'azul': (179, 212, 255),
                        'amarillo': (255, 255, 179),
                        'cyan': (179, 255, 255),
                        'magenta': (255, 179, 255),
                        'negro' : (0, 0, 0),
                        'blanco' : (255, 255, 255)
                        }
        self.pista_rect = pygame.Rect(50, 20, 420, 40)




    def dibujar_letras_enmarcadas(self, texto:str, x_inicial, y_inicial):
        x = x_inicial  # Posición inicial en x
        aumento_x = 30
        for letra in texto.upper():
            rectangulo = pygame.Rect(x, y_inicial, 30, 40)
            if letra.isspace():
                pygame.draw.rect(self.screen, self.colores['azul'], rectangulo)
            else:
                if letra == "_":
                    letra = " "
                letra_surface = self.fuente.render(letra, True, self.colores['negro'])
                letra_rect = letra_surface.get_rect(center=(x + aumento_x//2 , y_inicial + 20))

                pygame.draw.rect(self.screen, self.colores['amarillo'], rectangulo)
                pygame.draw.rect(self.screen, self.colores['negro'], rectangulo, 2)

                # Dibujar la letra centrada dentro del cuadrado
                self.screen.blit(letra_surface, letra_rect)

            x += aumento_x  # Espacio entre cuadros


    def whiletrue(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Rellenar la ventana con el color de fondo
            self.screen.fill(self.colores['blanco'])
            pygame.draw.rect(self.screen, self.colores['verde'], self.pista_rect)

            # Dibujar letras enmarcadas
            letras = "est_ es _n _je_plo _ara la _un_ion _e _ibujar ___ "
            lineas = wrap(letras, 14)
            for i in range(len(lineas)):
                lineas[i] = lineas[i].center(14)
                self.dibujar_letras_enmarcadas(lineas[i], 50, i*50 + 75)




            # Actualizar la pantalla
            pygame.display.flip()





