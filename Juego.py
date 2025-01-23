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
            self.vista.welcome()
            seleccion = self.vista.start_menu()
            match seleccion:
                case 1:
                    self.add_players()
                    jugadores_ok = True
                case 2:
                    print("Aun no implementado")
                    input()
                case 3:
                    exit()
                case _:
                    self.vista.error("Valor incorrecto")

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
        self.jugadores[self.turno].win_panel()
        for jugador in self.jugadores:
            jugador.puntos_ronda = 0


    def run(self):
        self.menu() #Menu de inicio - Elegir participantes
        self.panel = Panel(self.frase())    #Crear panel con una frase aleatoria

        while self.resuelto == False:
            first_throw = False
            round_game = True
            while round_game == True:
                self.vista.pintar_panel(self.panel)
                self.vista.pintar_jugadores(self.jugadores[self.turno])
                opcion_juego = self.vista.game_menu(self.jugadores[self.turno].nombre)
                match opcion_juego:
                    case 1:
                        first_throw = True
                        selection = self.weel.tirada()
                        match selection:
                            case 'broke':
                                self.jugadores[self.turno].puntos_ronda = 0
                                self.vista.bankrupt()
                                self.siguiente_turno()
                                round_game = False
                            case 'lose_turn':
                                self.vista.lose_turn()
                                self.siguiente_turno()
                                round_game = False
                            case _:
                                letra = self.vista.consonant()
                                if self.panel.comprobar_letra(letra) > 0:
                                    self.jugadores[self.turno].puntos_ronda += self.panel.comprobar_letra(letra) * selection
                                else:
                                    self.siguiente_turno()
                                    round_game = False
                    case 2:
                        if first_throw == False:
                            self.vista.error("Tienes que hacer una tirada primero")
                        elif self.jugadores[self.turno].puntos_ronda <= 50:
                            self.vista.error("No tienes suficientes puntos")
                        else:
                            self.vista.pintar_panel(self.panel)
                            self.jugadores[self.turno].compra_vocal()
                            vowel = self.vista.vowel()
                            if self.panel.comprobar_letra(vowel) == 0:
                                self.siguiente_turno()
                                round_game = False
                    case 3:
                        print(self.panel)
                        solucion = self.vista.solve()
                        if self.panel.comprobar_resolucion(solucion):
                            self.resuelto = True
                            round_game = False
                            self.control_puntos()
                            self.vista.pintar_panel(self.panel)
                            self.vista.end_points(self.jugadores)
                        else:
                            self.siguiente_turno()
                            round_game = False
                    case 4:
                        exit()
                    case _:
                        raise ValueError("Valor incorrecto en mach case")














#Tests
if __name__ == "__main__":
    juego = Juego()
    print(juego.frase())
