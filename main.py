from controller.juego import Juego
from models import Register, Wheel, Scoreboard
from view.vista import Vista

if __name__ == "__main__":
    vista = Vista()
    wheel = Wheel()
    register = Register()
    scoreboard = Scoreboard()

    game = Juego(vista, wheel, register, scoreboard)
    game.run()