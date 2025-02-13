import os
import time
from models import Jugador, Panel
import pygame
from textwrap import wrap

class Vista():

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
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
                        'blanco' : (255, 255, 255),
                        'gris' : (200, 200, 200)
                        }
        self.pista_rect = pygame.Rect(50, 20, 560, 50)




    def dibujar_letras_enmarcadas(self, texto:str, x, y_inicial):
        aumento_x = 40
        alto = 50
        rad = 5
        for letra in texto.upper():
            rectangulo = pygame.Rect(x, y_inicial, aumento_x, alto)
            if letra.isspace():
                color_actual = self.colores['azul']
            else:
                color_actual = self.colores['amarillo']
                if letra == "_":
                    letra = " "
                letra_surface = self.fuente.render(letra, True, self.colores['negro'])
                letra_rect = letra_surface.get_rect(center=(x + aumento_x//2 , y_inicial + alto//2))

            pygame.draw.rect(self.screen, color_actual, rectangulo, border_radius=rad)
            pygame.draw.rect(self.screen, self.colores['negro'], rectangulo, 2, border_radius=rad)

            # Dibujar la letra centrada dentro del cuadrado
            if not letra.isspace():
                self.screen.blit(letra_surface, letra_rect)

            x += aumento_x  # Espacio entre cuadros




    def dibujar_consonantes(self, consonantes, x, y_inicial, mouse_pos, click_pos):
        alto = 50
        ancho = 40
        aumento_x = 50
        rad = 5
        for letra in consonantes.upper():
            rectangulo = pygame.Rect(x, y_inicial, ancho, alto)
            
            if rectangulo.collidepoint(mouse_pos):
                color_actual = self.colores['rojo']  # Color hover
                sombra = pygame.Rect(x-5, y_inicial-5, ancho+10, alto+10)
                pygame.draw.rect(self.screen, self.colores['gris'], sombra, border_radius=rad)
            else:
                color_actual = self.colores['amarillo']

            if rectangulo.collidepoint(click_pos):
                print(f"Se ha pulsado {letra}")

            if letra == "_":
                letra = " "
            letra_surface = self.fuente.render(letra, True, self.colores['negro'])
            letra_rect = letra_surface.get_rect(center=(x + ancho//2 , y_inicial + alto//2))

            pygame.draw.rect(self.screen, color_actual, rectangulo, border_radius=rad)
            pygame.draw.rect(self.screen, self.colores['negro'], rectangulo, 2, border_radius=rad)

            # Dibujar la letra centrada dentro del cuadrado
            if not letra.isspace():
                self.screen.blit(letra_surface, letra_rect)

            x += aumento_x  # Espacio entre cuadros

    def rotar_ruleta(self, angulo):
        image = pygame.image.load('pyview\imgs\LaRuletadelaSuerte.png')
        
        imagen_rotada = pygame.transform.rotate(image, angulo)
        imagen_escalada = pygame.transform.scale(imagen_rotada, (300,300))

        rect_imagen = imagen_escalada.get_rect(center=(200, 300))
        self.screen.blit(imagen_escalada, rect_imagen.topleft)
        pass



    def controller(self):
        angulo = 0
        while True:
            click_pos = (0,0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os._exit(0)
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_pos = event.pos

            # Rellenar la ventana con el color de fondo
            self.screen.fill(self.colores['blanco'])
            pygame.draw.rect(self.screen, self.colores['verde'], self.pista_rect)

            # Dibujar letras enmarcadas
            letras = "est_ es _n _jem_lo _wra la _un_ion _e _ibujar _e "
            lineas = wrap(letras, 14)
            consonantes = 'bcdfghjklmnñpqrstvwxyz'
            consonantes = wrap(consonantes,6)
            for i in range(len(lineas)):
                lineas[i] = lineas[i].center(14)
                
                mouse_pos = pygame.mouse.get_pos()


                self.dibujar_letras_enmarcadas(lineas[i], 50, i*50 + 75)
                self.dibujar_consonantes(consonantes[i], 50, i*70+ 350, mouse_pos, click_pos)
            
            if angulo >= 360:
                angulo = 0
            angulo += 1

            self.rotar_ruleta(angulo)
            # Actualizar la pantalla
            pygame.display.flip()
            self.clock.tick(self.fps)
