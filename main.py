import pygame
from controller.juego import Juego
from models import Register, Weel
from view.vista import Vista

if __name__ == "__main__": 
    pygame.init()

    screen = pygame.display.set_mode((1100, 1100))
    pygame.display.set_caption("La Ruleta de la Suerte")
    
    vista = Vista(screen)
    weel = Weel()
    register = Register()

    game = Juego(vista, weel, register)
    game.run()