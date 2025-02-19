from models import Jugador, Panel, Wheel, Register, Scoreboard
from view.vista import Vista
import random
import json
from pathlib import Path

class Juego:
    turno: int
    players: list[Jugador]
    __panel_list: list[Panel]
    num_panel: int
    wheel: Wheel
    view: Vista
    player_round: bool

    def __init__(self, vista: Vista, wheel: Wheel, register: Register, scoreboard: Scoreboard):
        self.turno = 0
        self.players = []
        self.__panel_list = []
        self.num_panel = 0
        self.view = vista
        self.wheel = wheel
        self.register = register
        self.scoreboard = scoreboard
        self.player_round = True


    def menu(self):
        players_ok = False
        while players_ok == False:
            self.view.welcome()
            selection = self.view.start_menu()
            match selection:
                case 1:
                    self.add_players()
                    if len(self.players) > 0:
                        players_ok = True

                case 2:
                    print(self.scoreboard)
                    input()

                case 3:
                    phrase = self.view.phrase_entry("Introduce la frase", True)
                    if self.register.format_phrase(phrase) == None:
                        self.view.error("Frase demasiado larga o corta")
                    else:
                        hint = self.view.phrase_entry("Introduce la pista", True)
                        if self.register.format_hint(hint) == None:
                            self.view.error("Pista demasiado larga o corta")
                        try:
                            self.register.entry_generator(phrase, hint)
                        except FileNotFoundError:
                            self.view.error("Archivo no encontrado")
                        except json.JSONDecodeError:
                            self.view.error("Error en el archivo JSON")
                        except ValueError as e:
                            self.view.error(f"{e}")
                        except Exception as e:
                            self.view.error(f"Error desconocido: {e}")

                case 4:
                    if self.view.double_check():
                        exit()
                case _:
                    self.view.error("Valor incorrecto")

    def phrase(self) -> tuple[str, str]:
        root_dir = Path(__file__).resolve().parent.parent
        paneles_path = root_dir / "data" / "paneles.json"
        with open(paneles_path, "r") as f:
            paneles = json.load(f)
        clave = random.choice(list(paneles.keys()))
        return (paneles[clave]["phrase"], paneles[clave]["hint"])

    def add_players(self):
        num_players = 0
        check = False
        while check == False:
            try:
                num_players = self.view.num_players()
                check = True
            except ValueError:
                self.view.error("Valor incorrecto")
        while len(self.players) < num_players:
            name = ""
            if num_players == 1:
                name = self.login()
                if name != "exit":
                    self.players.append(Jugador(name))
                else:
                    return
            else:
                self.players.append(Jugador(self.view.player_name(len(self.players)+1)))
        self.view.starting_game()
    
    def login(self):
        valid_answer = False
        while valid_answer == False:
            username = self.view.phrase_entry("Introduce tu nombre de usuario")
            passw = self.view.get_password("Introduce tu contraseña")
            
            if username == "exit" or passw == "exit":
                return "exit"

            root_dir = Path(__file__).resolve().parent.parent
            usuarios_path = root_dir / "data" / "usuarios.json"
            with open(usuarios_path, "r") as f:
                usuarios = json.load(f)
            if username in usuarios:
                if usuarios[username]["password"] == passw:
                    self.view.login_success()
                    valid_answer = True
                else:
                    self.view.error("Contraseña incorrecta\n(exit)para salir")
            else:
                self.view.error("Usuario no encontrado\n(exit)para salir")
        return username


    def siguiente_turno(self):
        self.player_round = False
        self.turno += 1
        if self.turno == len(self.players):
            self.turno = 0

    def control_points(self):
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
                self.view.prove_letter("consonant")
                letra = self.view.prove_letter("consonant")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.__panel_list[self.num_panel].comprobar_letra("a")
                    self.__panel_list[self.num_panel].comprobar_letra("e")
                    self.__panel_list[self.num_panel].comprobar_letra("i")
                    self.__panel_list[self.num_panel].comprobar_letra("o")
                    self.__panel_list[self.num_panel].comprobar_letra("u")
                else:
                    self.siguiente_turno()
            case 'x2':
                self.view.wheel_x2()
                self.view.prove_letter("consonant")
                letra = self.view.prove_letter("consonant")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.players[self.turno].puntos_ronda *= 2
                else:
                    self.siguiente_turno()
            case '1/2':
                self.view.wheel_1_2()
                self.view.prove_letter("consonant")
                letra = self.view.prove_letter("consonant")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.players[self.turno].puntos_ronda //= 2
                else:
                    self.siguiente_turno()
            case _:     #Cualquier opcion de puntos normal
                try:
                    selection = int(selection)
                    self.view.wheel_points(selection)
                    letra = self.view.prove_letter("consonant")
                    if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                        self.players[self.turno].puntos_ronda += self.__panel_list[self.num_panel].comprobar_letra(letra) * selection
                    else:
                        self.siguiente_turno()
                except ValueError:
                    self.view.error("Error en la tirada, valor 'selection' no previsto")

    def run(self):
        self.menu() #Menu de inicio - Elegir participantes

        while len(self.__panel_list) < 3:
            panel = Panel(self.phrase())                                            #Crear paneles con una frase aleatoria
            if panel.frase not in [panel.frase for panel in self.__panel_list]:     #Asegurarse de no repetir la frase
                self.__panel_list.append(panel)

        while self.num_panel < 3:
            resuelto = False

            while resuelto == False:
                first_throw = False
                self.player_round = True

                while self.player_round == True:
                    self.view.correct_letters =  self.__panel_list[self.num_panel].letras_acertadas
                    self.view.print_panel(self.__panel_list[self.num_panel])
                    self.view.print_players(self.players[self.turno])
                    opcion_juego = self.view.game_menu(self.players[self.turno].nombre)
                    match opcion_juego:
                        case 1: #Tirar ruleta
                            first_throw = True
                            self.wheel_throw()

                        case 2: #Comprar vocal
                            if first_throw == False:
                                self.view.error("Tienes que hacer una tirada primero")
                            elif self.players[self.turno].puntos_ronda <= 500:
                                self.view.error("No tienes suficientes puntos")
                            else:
                                self.view.print_panel(self.__panel_list[self.num_panel])
                                self.players[self.turno].compra_vocal()
                                vowel = self.view.prove_letter("vowel")
                                if self.__panel_list[self.num_panel].comprobar_letra(vowel) == 0:
                                    self.siguiente_turno()

                        case 4: #Salir
                            if self.view.double_check():
                                self.siguiente_turno()

                        case 3: #Resolver panel
                            if first_throw == False:
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