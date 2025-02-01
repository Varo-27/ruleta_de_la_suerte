import random

class Weel:

    def __init__(self):
        self.section = (
                        0, 0, 
                        200, 200, 
                        500, 500, 500, 
                        750, 750, 750, 
                        1000, 1000, 
                        1500, 
                        2000, 
                        'broke', 'broke', 
                        'lose_turn', 'lose_turn', 
                        'all_vowels', 
                        'x2', 
                        '1/2'
                        )

    def tirada(self)  -> int | str:
        return random.choice(self.section)



if __name__ == "__main__":
    well = Weel()
    print(well.tirada())