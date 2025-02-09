from controller.juego import Juego
from models import Register, Wheel
from view.vista import Vista

if __name__ == "__main__": 
    vista = Vista()
    wheel = Wheel()
    register = Register()

    game = Juego(vista, wheel, register)
    game.run()