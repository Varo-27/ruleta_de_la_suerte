import random
import json
from pathlib import Path
from models import Jugador, Panel, Wheel, Register, Scoreboard
from view.vista import Vista

class Juego:
    turno: int
    num_panel: int
    num_rounds: int
    player_round: bool
    players: list[Jugador]
    __panel_list: list[Panel]
    wheel: Wheel
    register: Register
    scoreboard: Scoreboard
    view: Vista

    def __init__(self, vista: Vista, wheel: Wheel, register: Register, scoreboard: Scoreboard):
        self.turno = 0
        self.num_panel = 0
        self.player_round = True
        self.players = []
        self.__panel_list = []
        self.view = vista
        self.wheel = wheel
        self.register = register
        self.scoreboard = scoreboard


    def menu(self) -> None:
        """
        Menu de inicio, se eligen los jugadores y se cargan los paneles
        """
        players_ok = False
        while players_ok is False:
            self.view.welcome()
            selection = self.view.start_menu()
            match selection:
                case 1:
                    self.add_players()
                    if len(self.players) > 0:
                        players_ok = True

                case 2:
                    self.view.print_scoreboard(self.scoreboard)

                case 3:
                    self.phrase_register()

                case 4:
                    if self.view.double_check():
                        exit()
                case _:
                    self.view.error("Valor incorrecto")

    def phrase_register(self) -> None:
        self.view.phrase_register()
        phrase = self.view.phrase_entry("Introduce la frase", True)
        if self.register.format_phrase(phrase) is None:
            self.view.error("Frase demasiado larga o corta")
        else:
            hint = self.view.phrase_entry("Introduce la pista", True)
            if self.register.format_hint(hint) is None:
                self.view.error("Pista demasiado larga o corta")
            try:
                self.register.entry_generator(phrase, hint)
            except FileNotFoundError:
                self.view.error("Archivo no encontrado")
            except json.JSONDecodeError:
                self.view.error("Error en el archivo JSON")
            except ValueError as e:
                self.view.error(f"{e}")

    def phrase(self) -> tuple[str, str]:
        root_dir = Path(__file__).resolve().parent.parent
        paneles_path = root_dir / "data" / "paneles.json"
        with open(paneles_path, "r", encoding="utf-8") as f:
            paneles = json.load(f)
        clave = random.choice(list(paneles.keys()))
        return (paneles[clave]["phrase"], paneles[clave]["hint"])

    def add_players(self) -> None:
        num_players = 0
        check = False
        while check is False:
            try:
                num_players = self.view.num_players()
                check = True
            except ValueError:
                self.view.error("Valor incorrecto")
        while len(self.players) < num_players:
                self.players.append(Jugador(self.view.player_name(len(self.players)+1)))
        self.view.starting_game()

    def siguiente_turno(self) -> None:
        self.player_round = False
        self.turno += 1
        if self.turno == len(self.players):
            self.turno = 0

    def control_points(self) -> None:
        self.players[self.turno].win_panel()
        for jugador in self.players:
            jugador.puntos_ronda = 0

    def wheel_throw(self) -> None:
        selection = self.wheel.tirada()
        match selection:
            case 'broke':
                self.players[self.turno].puntos_ronda = 0
                self.view.wheel_bankrupt()
                self.siguiente_turno()
            case 'lose_turn':
                self.view.wheel_lose_turn()
                self.siguiente_turno()
            case 'all_vowels':
                self.view.wheel_allvowels()
                letter = self.view.prove_letter("consonante")
                num_letters = self.__panel_list[self.num_panel].check_letter(letter)
                if num_letters > 0:
                    self.__panel_list[self.num_panel].check_letter("a")
                    self.__panel_list[self.num_panel].check_letter("e")
                    self.__panel_list[self.num_panel].check_letter("i")
                    self.__panel_list[self.num_panel].check_letter("o")
                    self.__panel_list[self.num_panel].check_letter("u")
                elif num_letters == -1:
                    self.view.error("letter ya introducida")
                    self.siguiente_turno()
                else:
                    self.siguiente_turno()
            case 'x2':
                self.view.wheel_x2()
                letter = self.view.prove_letter("consonante")
                num_letters = self.__panel_list[self.num_panel].check_letter(letter)
                if num_letters > 0:
                    self.players[self.turno].puntos_ronda *= 2
                elif num_letters == -1:
                    self.view.error("letter ya introducida")
                    self.siguiente_turno()
                else:
                    self.siguiente_turno()
            case '1/2':
                self.view.wheel_1_2()
                letter = self.view.prove_letter("consonante")
                num_letters = self.__panel_list[self.num_panel].check_letter(letter)
                if num_letters > 0:
                    self.players[self.turno].puntos_ronda //= 2
                elif num_letters == -1:
                    self.view.error("letter ya introducida")
                    self.siguiente_turno()
                else:
                    self.siguiente_turno()
            case _:     #Cualquier opcion de puntos normal
                try:
                    selection = int(selection)
                    self.view.wheel_points(selection)
                    letter = self.view.prove_letter("consonante")
                    num_letters = self.__panel_list[self.num_panel].check_letter(letter)
                    if num_letters > 0:
                        puntos = num_letters * selection
                        self.players[self.turno].puntos_ronda += puntos
                    elif num_letters == -1:
                        self.view.error("letra ya introducida")
                        self.siguiente_turno()
                    else:
                        self.siguiente_turno()
                except ValueError:
                    self.view.error("Error en la tirada, valor 'selection' no previsto")

    def run(self) -> None:
        self.menu() #Menu de inicio - Elegir participantes
        if len(self.players) == 1:
            self.num_rounds = 3
        else:
            self.num_rounds = self.view.num_rounds()

        while len(self.__panel_list) < self.num_rounds:
            panel = Panel(self.phrase())                                            #Crear paneles con una frase aleatoria
            if panel.frase not in [panel.frase for panel in self.__panel_list]:     #Asegurarse de no repetir la frase
                self.__panel_list.append(panel)

        while self.num_panel < self.num_rounds:
            resuelto = False

            while resuelto is False:
                first_throw = False
                self.player_round = True

                while self.player_round is True:
                    self.view.print_panel(self.__panel_list[self.num_panel])
                    self.view.print_players(self.players[self.turno])
                    opcion_juego = self.view.game_menu(self.players[self.turno].nombre)
                    match opcion_juego:
                        case 1: #Tirar ruleta
                            first_throw = True
                            self.wheel_throw()

                        case 2: #Comprar vocal
                            if first_throw is False:
                                self.view.error("Tienes que hacer una tirada primero")
                            elif self.players[self.turno].puntos_ronda <= 500:
                                self.view.error("No tienes suficientes puntos")
                            else:
                                self.view.print_panel(self.__panel_list[self.num_panel])
                                self.players[self.turno].compra_vocal()
                                vowel = self.view.prove_letter("vocal")
                                if self.__panel_list[self.num_panel].check_letter(vowel) == 0:
                                    self.siguiente_turno()

                        case 4: #Salir
                            if self.view.double_check():
                                self.siguiente_turno()

                        case 3: #Resolver panel
                            if first_throw is False:
                                self.view.error("Tienes que hacer una tirada primero")
                            elif self.players[self.turno].puntos_ronda <= 0:
                                self.view.error("No tienes puntos para guardar")
                            else:
                                self.view.print_panel(self.__panel_list[self.num_panel])
                                solucion = self.view.phrase_entry("Introduce la solución", True)
                                if self.__panel_list[self.num_panel].comprobar_resolucion(solucion):
                                    resuelto = True
                                    self.control_points()
                                    self.view.print_panel(self.__panel_list[self.num_panel])
                                    self.view.end_points(self.players)
                                self.siguiente_turno()
                        case _:
                            raise ValueError("Valor incorrecto en mach case")

            self.num_panel += 1
        self.view.end_points(self.players)

        for player in self.players:
            try:
                self.scoreboard.add_score(player.nombre, player.puntos_totales)
            except FileNotFoundError:
                self.view.error("Archivo no encontrado")
            except json.JSONDecodeError:
                self.view.error("Error en el archivo JSON")
            except ValueError as e:
                self.view.error(f"{e}")

        self.view.print_scoreboard(self.scoreboard)
