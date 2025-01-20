from Panel import Panel
from Vista import Vista
from Weel import Weel
import Jugador
from time import sleep
import random
import json

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
                
                self.vista.elegir()
                seleccion = self.vista.menu_inicio()
                if seleccion == 1:
                    self.add_players()
                    jugadores_ok = True
                elif seleccion == 2:
                    print("Aun no implementado")
                    input()
                elif seleccion == 3:
                    exit()
                else:
                    self.vista.error("Valor incorrecto")
            except:
                self.vista.error("Tipo de dato incorrecto")
                sleep(1)

    def frase(self) -> tuple:
        with open("paneles.json", "r") as f:
            paneles = json.load(f)
        clave = random.choice(list(paneles.keys()))
        return (paneles[clave]['frase'], paneles[clave]['pista'])


    def add_players(self):
        check = False
        while check == False:
            try:
                num_players = self.vista.num_participantes()
                check = True
            except ValueError:
                self.vista.error("Valor incorrecto")

        while len(self.jugadores) < num_players:
            self.jugadores.append(Jugador.Jugador(self.vista.nombre_jugador(len(self.jugadores)+1)))

        self.vista.empezando_partida()



    def siguiente_turno(self):
        self.turno += 1

    def control_puntos(self):
        pass


    def run(self):
        self.menu()
        self.panel = Panel(self.frase())
        while self.resuelto ==False:
            self.jugadores[self.turno].jugar()


if __name__ == "__main__":
    juego = Juego()
    print(juego.frase())
