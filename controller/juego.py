from models import Jugador, Panel, Wheel, Register
from view.vista import Vista
import random
import json

class Juego:
    turno: int
    jugadores: list[Jugador]
    __panel_list: list[Panel]
    num_panel: int
    wheel: Wheel
    vista: Vista
    player_round: bool

    def __init__(self, vista: Vista, wheel: Wheel, register: Register):
        self.turno = 0
        self.jugadores = []
        self.__panel_list = []
        self.num_panel = 0
        self.vista = vista
        self.wheel = wheel
        self.register = register
        self.player_round = True


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
                    phrase = self.vista.phrase_entry("Introduce la frase")
                    if self.register.format_phrase(phrase) == None:
                        self.vista.error("Frase demasiado larga o corta")
                    else:
                        hint = self.vista.phrase_entry("Introduce la pista")
                        if self.register.format_hint(hint) == None:
                            self.vista.error("Pista demasiado larga o corta")
                        try:
                            self.register.entry_generator(phrase, hint)
                        except FileNotFoundError:
                            self.vista.error("Archivo no encontrado")
                        except json.JSONDecodeError:
                            self.vista.error("Error en el archivo JSON")
                        except ValueError as e:
                            self.vista.error(f"{e}")
                        except Exception as e:
                            self.vista.error(f"Error desconocido: {e}")

                case 4:
                    if self.vista.double_check():
                        exit()
                case _:
                    self.vista.error("Valor incorrecto")

    def frase(self) -> tuple[str, str]:
        with open("paneles.json", "r") as f:
            paneles = json.load(f)
        clave = random.choice(list(paneles.keys()))
        return (paneles[clave]["phrase"], paneles[clave]["hint"])


    def add_players(self):
        num_players = 0
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
        self.player_round = False
        self.turno += 1
        if self.turno == len(self.jugadores):
            self.turno = 0

    def control_puntos(self):
        self.jugadores[self.turno].win_panel()
        for jugador in self.jugadores:
            jugador.puntos_ronda = 0

    def wheel_throw(self) -> None:
        selection = self.wheel.tirada()
        match selection:
            case 'broke':
                self.jugadores[self.turno].puntos_ronda = 0
                self.vista.wheel_bankrupt()
                self.siguiente_turno()
            case 'lose_turn':
                self.vista.wheel_lose_turn()
                self.siguiente_turno()
            case 'all_vowels':
                self.vista.wheel_allvowels()
                self.vista.prove_letter("consonante")
                letra = self.vista.prove_letter("consonante")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.__panel_list[self.num_panel].comprobar_letra("a")
                    self.__panel_list[self.num_panel].comprobar_letra("e")
                    self.__panel_list[self.num_panel].comprobar_letra("i")
                    self.__panel_list[self.num_panel].comprobar_letra("o")
                    self.__panel_list[self.num_panel].comprobar_letra("u")
                else:
                    self.siguiente_turno()
            case 'x2':
                self.vista.wheel_x2()
                self.vista.prove_letter("consonante")
                letra = self.vista.prove_letter("consonante")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.jugadores[self.turno].puntos_ronda *= 2
                else:
                    self.siguiente_turno()
            case '1/2':
                self.vista.prove_letter("consonante")
                letra = self.vista.prove_letter("consonante")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.jugadores[self.turno].puntos_ronda //= 2
                else:
                    self.siguiente_turno()
            case _: #cualquier opcion de puntos normal
                try:
                    selection = int(selection)
                    self.vista.wheel_points(selection)
                    letra = self.vista.prove_letter("consonante")
                    if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                        self.jugadores[self.turno].puntos_ronda += self.__panel_list[self.num_panel].comprobar_letra(letra) * selection
                    else:
                        self.siguiente_turno()
                except ValueError:
                    self.vista.error("Error en la tirada, valor 'selection' no previsto")

    def run(self):
        self.menu() #Menu de inicio - Elegir participantes

        while len(self.__panel_list) < 3:
            panel = Panel(self.frase())                                             #Crear paneles con una frase aleatoria
            if panel.frase not in [panel.frase for panel in self.__panel_list]:     #Asegurarse de no repetir la frase
                self.__panel_list.append(panel)

        while self.num_panel < 3:
            resuelto = False

            while resuelto == False:
                first_throw = False
                self.player_round = True

                while self.player_round == True:
                    self.vista.pintar_panel(self.__panel_list[self.num_panel])
                    self.vista.pintar_jugadores(self.jugadores[self.turno])
                    opcion_juego = self.vista.game_menu(self.jugadores[self.turno].nombre)
                    match opcion_juego:
                        case 1: #Tirar ruleta
                            first_throw = True
                            self.wheel_throw()

                        case 2: #Comprar vocal
                            if first_throw == False:
                                self.vista.error("Tienes que hacer una tirada primero")
                            elif self.jugadores[self.turno].puntos_ronda <= 500:
                                self.vista.error("No tienes suficientes puntos")
                            else:
                                self.vista.pintar_panel(self.__panel_list[self.num_panel])
                                self.jugadores[self.turno].compra_vocal()
                                vowel = self.vista.prove_letter("vocal")
                                if self.__panel_list[self.num_panel].comprobar_letra(vowel) == 0:
                                    self.siguiente_turno()

                        case 4: #Salir
                            if self.vista.double_check():
                                self.siguiente_turno()

                        case 3: #Resolver panel
                            if first_throw == False:
                                self.vista.error("Tienes que hacer una tirada primero")
                            elif self.jugadores[self.turno].puntos_ronda <= 0:
                                self.vista.error("No tienes puntos para guardar")
                            else:
                                self.vista.pintar_panel(self.__panel_list[self.num_panel])
                                solucion = self.vista.phrase_entry("Introduce la solución")
                                if self.__panel_list[self.num_panel].comprobar_resolucion(solucion):
                                    resuelto = True
                                    self.control_puntos()
                                    self.vista.pintar_panel(self.__panel_list[self.num_panel])
                                    self.vista.end_points(self.jugadores)
                                self.siguiente_turno()
                        case _:
                            raise ValueError("Valor incorrecto en mach case")

            self.num_panel += 1
        self.vista.end_points(self.jugadores)
