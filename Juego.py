from Vista import Vista
import Ruleta
import Jugador
from time import sleep

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
                self.vista.elegir()
                seleccion = int(input())
                if seleccion == 1:
                    check = False
                    while check == False:
                        try:
                            self.vista.num_participantes()
                            num_players = int(input())
                            check = True
                        except ValueError:
                            self.vista.error()

                    while len(game.jugadores) < num_players:
                        self.vista.nombre_jugador(len(game.jugadores)+1)
                        game.añadir_jugadores(input())
                    self.vista.empezando_partida()
                    jugadores_ok = True
                elif seleccion == 2:
                    print("Aun no implementado")
                    input()
                else:
                    print("Selecciona una opcion válida")

            except:
                print("numero invalido")
                sleep(1)



if __name__ == "__main__":
    game = Juego()
    game.run()