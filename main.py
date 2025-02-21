from controller.game import Game
from models import Register, Wheel, Scoreboard
from view.vista import View

if __name__ == "__main__":
    view = View()
    wheel = Wheel()
    register = Register()
    scoreboard = Scoreboard()

    game = Game(view, wheel, register, scoreboard)
    game.run()