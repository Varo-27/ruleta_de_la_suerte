
class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos_ronda = 0
        self.puntos_totales = 0

    def compra_vocal(self):
        self.puntos_ronda -=50

    def win_panel(self):
        self.puntos_totales += self.puntos_ronda
    
    def pintar_total(self):
        return f"{self.nombre} - {self.puntos_totales} puntos"

    def __str__(self) -> str:
        return f"{self.nombre} - {self.puntos_ronda} puntos"