class Jugador:
    nombre: str
    puntos_ronda: int
    __puntos_totales: int

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.puntos_ronda = 0
        self.__puntos_totales = 0

    @property
    def puntos_totales(self) -> int:
        return self.__puntos_totales


    def compra_vocal(self):
        self.puntos_ronda -=500

    def win_panel(self):
        self.__puntos_totales += self.puntos_ronda
    
    def pintar_total(self) -> str:
        return f"{self.nombre} - {self.__puntos_totales} puntos"

    def __str__(self) -> str:
        return f"{self.nombre} - {self.puntos_ronda} puntos"