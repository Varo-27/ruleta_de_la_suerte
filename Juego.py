from Vista import Vista
from Weel import Weel
import Jugador
from time import sleep

class Juego:

    def __init__(self):
        self.vista = Vista()
        self.turno = 0
        self.jugadores = []
        self.resuelto = False


    def menu(self):
        jugadores_ok = False
        while jugadores_ok == False:
            try:
                self.vista.inicio()
                self.vista.menu_opciones()
                self.vista.elegir()
                seleccion = int(input())
                if seleccion == 1:
                    self.add_players()
                    jugadores_ok = True
                elif seleccion == 2:
                    print("Aun no implementado")
                    input()
                else:
                    self.vista.error()
            except:
                print("numero invalido")
                sleep(1)



    def add_players(self):
        check = False
        while check == False:
            try:
                self.vista.num_participantes()
                num_players = int(input())
                check = True
            except ValueError:
                self.vista.error()

        while len(self.jugadores) < num_players:
            self.vista.nombre_jugador(len(self.jugadores)+1)
            
            self.jugadores.append(Jugador.Jugador(input()))

        self.vista.empezando_partida()



    def siguiente_turno(self):
        self.turno += 1

    def control_puntos(self):
        pass


    def run(self):
        self.menu()

        while self.resuelto ==False:
            self.jugadores[self.turno].jugar()
