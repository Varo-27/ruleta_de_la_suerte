import pygame
import sys
from textwrap import wrap

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 1100, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Cada Letra en un Cuadro con Borde")

# Definir colores
colores = {
    'rojo': (255, 179, 186),
    'verde': (186, 255, 201),
    'azul': (179, 212, 255),
    'amarillo': (255, 255, 179),
    'cyan': (179, 255, 255),
    'magenta': (255, 179, 255),
    'negro' : (0, 0, 0),
    'blanco' : (255, 255, 255)
}


# Definir la fuente
fuente = pygame.font.Font("Gordita-Black.otf", 70)

# Función para dibujar cada letra en un cuadrado con borde
def dibujar_letras_enmarcadas(self, texto:str, x_inicial, y_inicial):
    x = x_inicial  # Posición inicial en x
    aumento_x = 70
    for letra in texto.upper():
        if letra.isspace():
            rectangulo = pygame.Rect(x, y_inicial, 70, 80)
            pygame.draw.rect(ventana, colores['azul'], rectangulo)
        else:
            if letra == "_":
                letra = " "
            letra_surface = fuente.render(letra, True, colores['negro'])
            letra_rect = letra_surface.get_rect(center=(x + aumento_x//2 , y_inicial + 45))

            # Dibujar el borde del rectángulo
            rectangulo = pygame.Rect(x, y_inicial, 70, 80)
            pygame.draw.rect(ventana, colores['amarillo'], rectangulo)
            pygame.draw.rect(ventana, colores['negro'], rectangulo, 2)

            # Dibujar la letra centrada dentro del cuadrado
            ventana.blit(letra_surface, letra_rect)

        x += aumento_x  # Espacio entre cuadros


# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar la ventana con el color de fondo
    ventana.fill(colores['blanco'])

    # Dibujar letras enmarcadas
    letras = "est_ es _n _je_plo _ara la _un_ion _e _ibujar "
    lineas = wrap(letras, 14)
    for i in range(len(lineas)):
        lineas[i] = lineas[i].center(14)
        dibujar_letras_enmarcadas(lineas[i], 50, i*100 + 50)




    # Actualizar la pantalla
    pygame.display.flip()