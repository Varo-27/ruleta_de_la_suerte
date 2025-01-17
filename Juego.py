from Vista import Vista
import Ruleta
import Jugador

class Juego:

    def __init__(self):
        self.vista = Vista()
        self.turno = 0
        self.jugadores = []

    def añadir_jugadores(self, nombre):
        self.jugadores.append(Jugador.Jugador(nombre))

    def siguiente_turno(self):
        self.jugadores[self.turno].tirar()

    def control_puntos(self):
        pass

    def run(self):
        jugadores_ok = False
        while jugadores_ok == False:
            try:
                self.vista.inicio()
                self.vista.menu_opciones()
                seleccion = int(input("Elige una opción"))
                if seleccion == 1:
                    check = False
                    while check == False:
                        try:
                            num_players = int(input("Introduce el numero de participantes: "))
                            check = True
                        except ValueError:
                            print("Introduce un numero de jugadores")

                    while len(game.jugadores) < num_players:
                        game.añadir_jugadores(input(f"Nombre del Jugador {len(game.jugadores)+1}: "))
                    print("Jugadores listos")
                    jugadores_ok = True
                elif seleccion == 2:
                    print("Aun no implementado")
                    input()
                else:
                    print("Selecciona una opcion válida")

            except:
                print("numero invalido")



if __name__ == "__main__":
    game = Juego()
    game.run()