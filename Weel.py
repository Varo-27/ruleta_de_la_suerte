import random

class Weel:

    def __init__(self):
        self.section = (0, 25, 25, 50, 50, 75, 75, 100, 200, 'broke', 'broke', 'lose_turn', 'lose_turn')
        self.selection = 0

    def tirada(self)  -> int | str:
        self.selection = random.choice(self.section)
        return self.selection



if __name__ == "__main__":
    well = Weel()
    well.tirada()