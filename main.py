from controller.juego import Juego
from models import Register, Weel
from view.vista import Vista

if __name__ == "__main__": 
    vista = Vista()
    weel = Weel()
    register = Register()

    game = Juego(vista, weel, register)
    game.run()