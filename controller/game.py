import random
import json
from pathlib import Path
from models import Player, Panel, Wheel, Register, Scoreboard
from view.vista import View

class Game:
    __turn: int = 0
    __num_panel: int = 0
    __num_rounds: int = 0
    __player_round: bool = True
    __players: list[Player] = []
    __panel_list: list[Panel] = []
    __wheel: Wheel
    __register: Register
    __scoreboard: Scoreboard
    __view: View

    def __init__(self, view: View, wheel: Wheel, register: Register, scoreboard: Scoreboard):
        self.__view = view
        self.__wheel = wheel
        self.__register = register
        self.__scoreboard = scoreboard


    def menu(self) -> None:
        """
        Menu de inicio, se eligen los jugadores y se cargan los paneles
        """
        players_ok = False
        while players_ok is False:
            self.__view.welcome()
            selection = self.__view.start_menu()
            match selection:
                case 1:
                    self.add_players()
                    if len(self.__players) > 0:
                        players_ok = True

                case 2:
                    self.__view.print_scoreboard(self.__scoreboard)

                case 3:
                    self.phrase_register()

                case 4:
                    if self.__view.double_check():
                        exit()
                case _:
                    self.__view.error("Valor incorrecto")

    def phrase_register(self) -> None:
        self.__view.phrase_register()
        phrase = self.__view.phrase_entry("Introduce la frase", True)
        if self.__register.format_phrase(phrase) is None:
            self.__view.error("Frase demasiado larga o corta")
        else:
            hint = self.__view.phrase_entry("Introduce la pista", True)
            if self.__register.format_hint(hint) is None:
                self.__view.error("Pista demasiado larga o corta")
            try:
                self.__register.entry_generator(phrase, hint)
            except FileNotFoundError:
                self.__view.error("Archivo no encontrado")
            except json.JSONDecodeError:
                self.__view.error("Error en el archivo JSON")
            except ValueError as e:
                self.__view.error(f"{e}")

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
                num_players = self.__view.num_players()
                check = True
            except ValueError:
                self.__view.error("Valor incorrecto")
        while len(self.__players) < num_players:
                self.__players.append(Player(self.__view.player_name(len(self.__players)+1)))

    def next_turn(self) -> None:
        self.__player_round = False
        self.__turn += 1
        if self.__turn == len(self.__players):
            self.__turn = 0

    def control_points(self) -> None:
        self.__players[self.__turn].win_panel()
        for player in self.__players:
            player.round_points = 0

    def wheel_throw(self) -> None:
        selection = self.__wheel.throw()
        match selection:
            case 'broke':
                self.__players[self.__turn].round_points = 0
                self.__view.wheel_bankrupt()
                self.next_turn()
            case 'lose_turn':
                self.__view.wheel_lose_turn()
                self.next_turn()
            case 'all_vowels':
                self.__view.wheel_allvowels()
                letter = self.__view.prove_letter("consonante")
                num_letters = self.__panel_list[self.__num_panel].check_letter(letter)
                if num_letters > 0:
                    self.__panel_list[self.__num_panel].check_letter("a")
                    self.__panel_list[self.__num_panel].check_letter("e")
                    self.__panel_list[self.__num_panel].check_letter("i")
                    self.__panel_list[self.__num_panel].check_letter("o")
                    self.__panel_list[self.__num_panel].check_letter("u")
                elif num_letters == -1:
                    self.__view.error("letter ya introducida")
                    self.next_turn()
                else:
                    self.next_turn()
            case 'x2':
                self.__view.wheel_x2()
                letter = self.__view.prove_letter("consonante")
                num_letters = self.__panel_list[self.__num_panel].check_letter(letter)
                if num_letters > 0:
                    self.__players[self.__turn].round_points *= 2
                elif num_letters == -1:
                    self.__view.error("letter ya introducida")
                    self.next_turn()
                else:
                    self.next_turn()
            case '1/2':
                self.__view.wheel_1_2()
                letter = self.__view.prove_letter("consonante")
                num_letters = self.__panel_list[self.__num_panel].check_letter(letter)
                if num_letters > 0:
                    self.__players[self.__turn].round_points //= 2
                elif num_letters == -1:
                    self.__view.error("letter ya introducida")
                    self.next_turn()
                else:
                    self.next_turn()
            case _:     #Cualquier opcion de puntos normal
                try:
                    selection = int(selection)
                    self.__view.wheel_points(selection)
                    letter = self.__view.prove_letter("consonante")
                    num_letters = self.__panel_list[self.__num_panel].check_letter(letter)
                    if num_letters > 0:
                        puntos = num_letters * selection
                        self.__players[self.__turn].round_points += puntos
                    elif num_letters == -1:
                        self.__view.error("letra ya introducida")
                        self.next_turn()
                    else:
                        self.next_turn()
                except ValueError:
                    self.__view.error("Error en la tirada, valor 'selection' no previsto")

    def run(self) -> None:
        self.menu() #Menu de inicio - Elegir participantes
        if len(self.__players) == 1:
            self.__num_rounds = 3
        else:
            self.__num_rounds = self.__view.num_rounds()

        self.__view.starting_game()

        while len(self.__panel_list) < self.__num_rounds:
            panel = Panel(self.phrase())                                            #Crear paneles con una frase aleatoria
            if panel.phrase not in [panel.phrase for panel in self.__panel_list]:     #Asegurarse de no repetir la frase
                self.__panel_list.append(panel)

        while self.__num_panel < self.__num_rounds:
            resuelto = False

            while resuelto is False:
                first_throw = False
                self.__player_round = True

                while self.__player_round is True:
                    self.__view.print_panel(self.__panel_list[self.__num_panel])
                    self.__view.print_players(self.__players[self.__turn])
                    opcion_game = self.__view.game_menu(self.__players[self.__turn].name)
                    match opcion_game:
                        case 1: #Tirar ruleta
                            first_throw = True
                            self.wheel_throw()

                        case 2: #Comprar vocal
                            if first_throw is False:
                                self.__view.error("Tienes que hacer una tirada primero")
                            elif self.__players[self.__turn].round_points <= 500:
                                self.__view.error("No tienes suficientes puntos")
                            else:
                                self.__view.print_panel(self.__panel_list[self.__num_panel])
                                self.__players[self.__turn].buy_vowel()
                                vowel = self.__view.prove_letter("vocal")
                                if self.__panel_list[self.__num_panel].check_letter(vowel) == 0:
                                    self.next_turn()

                        case 4: #Salir
                            if self.__view.double_check():
                                self.next_turn()

                        case 3: #Resolver panel
                            if first_throw is False:
                                self.__view.error("Tienes que hacer una tirada primero")
                            elif self.__players[self.__turn].round_points <= 0:
                                self.__view.error("No tienes puntos para guardar")
                            else:
                                self.__view.print_panel(self.__panel_list[self.__num_panel])
                                solucion = self.__view.phrase_entry("Introduce la solución", True)
                                if self.__panel_list[self.__num_panel].comprobar_resolucion(solucion):
                                    resuelto = True
                                    self.control_points()
                                    self.__view.print_panel(self.__panel_list[self.__num_panel])
                                    self.__view.endround_points(self.__players)
                                    self.__view.total_points(self.__players)
                                self.next_turn()
                        case _:
                            raise ValueError("Valor incorrecto en mach case")

            self.__num_panel += 1
        self.__view.total_points(self.__players)

        for player in self.__players:
            try:
                self.__scoreboard.add_score(player.name, player.total_points)
            except FileNotFoundError:
                self.__view.error("Archivo no encontrado")
            except json.JSONDecodeError:
                self.__view.error("Error en el archivo JSON")
            except ValueError as e:
                self.__view.error(f"{e}")

        self.__view.print_scoreboard(self.__scoreboard)
