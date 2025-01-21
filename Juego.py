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
        self.weel = Weel()
        self.turno = 0
        self.jugadores = []
        self.resuelto = False


    def menu(self):
        jugadores_ok = False
        while jugadores_ok == False:
            try:
                self.vista.welcome()
                seleccion = self.vista.start_menu()
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
            self.jugadores.append(Jugador.Jugador(self.vista.player_name(len(self.jugadores)+1)))

        self.vista.starting_game()

    def siguiente_turno(self):
        self.turno += 1
        if self.turno == len(self.jugadores):
            self.turno = 0

    def control_puntos(self):
        self.jugadores[self.turno].puntos += 100
        pass


    def run(self):
        self.menu()
        self.panel = Panel(self.frase())
        while self.resuelto ==False:
            opcion_juego = self.vista.game_menu(self.jugadores[self.turno].nombre)
            match opcion_juego:
                case 1:
                    selection = self.weel.tirada()

                    match selection:
                        case 'broke':
                            self.jugadores[self.turno].puntos = 0
                            self.vista.bankrupt()
                            self.siguiente_turno()
                        case 'lose_turn':
                            self.vista.lose_turn()
                            self.siguiente_turno()
                        case _:
                            letra = self.vista.consonant()
                            if self.panel.comprobar_letra(letra) > 0:
                                self.jugadores[self.turno].puntos += self.panel.comprobar_letra(letra) * selection
                            else:
                                self.siguiente_turno() 
                case 2:
                    self.vista.pintar_panel(self.panel)
                    self.jugadores[self.turno].compra_vocal()
                    vowel = self.vista.vowel()
                    if self.panel.comprobar_letra(vowel) == 0:
                        self.siguiente_turno()
                case 3:
                    solucion = self.vista.solve()
                    if self.panel.comprobar_resolucion(solucion):
                        self.resuelto = True
                        self.control_puntos()
                    else:
                        self.siguiente_turno()
                case 4:
                    exit()
                case _:
                    raise ValueError("Valor incorrecto en mach case")














#Tests
if __name__ == "__main__":
    juego = Juego()
    print(juego.frase())
