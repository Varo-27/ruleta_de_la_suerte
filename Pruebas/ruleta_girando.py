import pygame

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Rotar una imagen en Pygame")

# Carga la imagen
imagen = pygame.image.load('imgs/LaRuletadelaSuerte.png')

# Ángulo de rotación
angulo = 0  # Puedes cambiar este valor para rotar la imagen al ángulo deseado

# Configuración de FPS (frames per second)
clock = pygame.time.Clock()
fps = 60

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if angulo >= 360:
        angulo = 0
    angulo += 1
    # Rellena la pantalla con el color blanco
    screen.fill((255, 255, 255))
    
    # Rota la imagen
    imagen_rotada = pygame.transform.rotate(imagen, angulo)
    
    # Obtén el rectángulo de la imagen rotada para centrarla
    rect_imagen = imagen_rotada.get_rect(center=(500, 500))
    
    # Dibuja la imagen rotada en la posición (500, 500) centrada
    screen.blit(imagen_rotada, rect_imagen.topleft)
    
    # Actualiza la pantalla
    pygame.display.flip()
    
    # Limita los FPS
    clock.tick(fps)

pygame.quit()
