from panel import Panel
from vista import Vista
from weel import Weel
from jugador import Jugador
import random
import json

class Juego:
    turno: int
    jugadores: list[Jugador]
    lista_paneles: list[Panel]
    paneles_completados: int
    weel: Weel
    vista: Vista

    def __init__(self):
        self.turno = 0
        self.jugadores = []
        self.paneles = []
        self.paneles_completados = 0
        self.vista = Vista()
        self.weel = Weel()


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
                    self.vista.end_game()
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
            self.jugadores.append(Jugador(self.vista.player_name(len(self.jugadores)+1)))

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

        while len(self.paneles) < 3:
            self.panel = Panel(self.frase())    #Crear paneles con una frase aleatoria
            if self.panel.frase not in [panel.frase for panel in self.paneles]:
                self.paneles.append(self.panel)
        
        while self.paneles_completados < 3:

            self.panel.resuelto = False

            while self.panel.resuelto == False:
                first_throw = False
                player_round = True

                while player_round == True:
                    self.vista.pintar_panel(self.panel)
                    self.vista.pintar_jugadores(self.jugadores[self.turno])
                    opcion_juego = self.vista.game_menu(self.jugadores[self.turno].nombre)
                    match opcion_juego:
                        case 1: #Tirar ruleta
                            first_throw = True
                            selection = self.weel.tirada()
                            match selection:
                                case 'broke':
                                    self.jugadores[self.turno].puntos_ronda = 0
                                    self.vista.weel_bankrupt()
                                    self.siguiente_turno()
                                    player_round = False
                                case 'lose_turn':
                                    self.vista.weel_lose_turn()
                                    self.siguiente_turno()
                                    player_round = False
                                case _:
                                    try:
                                        selection = int(selection)
                                        self.vista.weel_points(selection)
                                        letra = self.vista.consonant()
                                        if self.panel.comprobar_letra(letra) > 0:
                                            self.jugadores[self.turno].puntos_ronda += self.panel.comprobar_letra(letra) * selection
                                        else:
                                            self.siguiente_turno()
                                            player_round = False
                                    except ValueError:
                                        self.vista.error("Error en la tirada, 'selection' no previsto")

                        case 2: #Comprar vocal
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
                                    player_round = False

                        case 3: #Resolver panel
                            self.vista.pintar_panel(self.panel)
                            solucion = self.vista.solve()
                            if self.panel.comprobar_resolucion(solucion):
                                self.panel.resuelto = True
                                player_round = False
                                self.control_puntos()
                                self.vista.pintar_panel(self.panel)
                                self.vista.end_points(self.jugadores)
                            else:
                                self.siguiente_turno()
                                player_round = False

                        case 4: #Salir
                            self.vista.end_game()

                        case _:
                            raise ValueError("Valor incorrecto en mach case")

                self.paneles_completados += 1
        self.vista.end_points(self.jugadores)












#Tests
if __name__ == "__main__":
    juego = Juego()
    print(juego.run())
