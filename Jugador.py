
class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def compra_vocal(self):
        if self.puntos < 50:
            return False
        else:
            self.puntos -=50
            return True

    def jugar(self):
        



    def resolver(self):
        #resolver el panel
        pass

    def __str__(self) -> str:
        return self.nombre