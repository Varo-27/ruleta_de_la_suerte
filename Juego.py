import Ruleta
import Jugador

class Juego:

    def __init__(self, numero_jugadores: int):
        self.numero_jugadores = numero_jugadores
        self.turno = 0
        self.jugadores = []

    def añadir_jugadores(self, nombre):
        self.jugadores.append(Jugador.Jugador(nombre))

    def siguiente_turno(self):
        pass

    def control_puntos(self):
        pass

    def __str__(self):
        return "1.Añadir jugadores \n2.Empezar partida"




if __name__ == "__main__":
    check = False
    while check == False:
        try:
            num_players = int(input("Introduce el numero de participantes: "))
            check = True
        except ValueError:
            print("Introduce un numero de jugadores")
        
    game = Juego(num_players)

    print(game)

    while True:
        try:
            seleccion = int(input())
            if seleccion == 1:
                game.añadir_jugadores(input("Nombre del Jugador"))
                break
        except:
            print("numero invalido")
    
    game.siguiente_turno()