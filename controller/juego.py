from models import Jugador, Panel, Weel, Register
from view.vista import Vista
import random
import json

class Juego:
    turno: int
    jugadores: list[Jugador]
    __panel_list: list[Panel]
    num_panel: int
    weel: Weel
    vista: Vista

    def __init__(self, vista: Vista, weel: Weel, register: Register):
        self.turno = 0
        self.jugadores = []
        self.__panel_list = []
        self.num_panel = 0
        self.vista = vista
        self.weel = weel
        self.register = register


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
                    valid_answer = False
                    while valid_answer == False:
                        self.phrase = self.vista.phrase_entry("Introduce la frase")
                        self.hint = self.vista.phrase_entry("Introduce la pista")
                case 4:
                    self.vista.double_check()
                case _:
                    self.vista.error("Valor incorrecto")

    def frase(self) -> tuple[str, str]:
        with open("paneles.json", "r") as f:
            paneles = json.load(f)
        clave = random.choice(list(paneles.keys()))
        return (paneles[clave]['frase'], paneles[clave]['pista'])


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
        self.turno += 1
        if self.turno == len(self.jugadores):
            self.turno = 0

    def control_puntos(self):
        self.jugadores[self.turno].win_panel()
        for jugador in self.jugadores:
            jugador.puntos_ronda = 0

    def weel_throw(self) -> bool:
        selection = self.weel.tirada()
        match selection:
            case 'broke':
                self.jugadores[self.turno].puntos_ronda = 0
                self.vista.weel_bankrupt()
                self.siguiente_turno()
                return False
            case 'lose_turn':
                self.vista.weel_lose_turn()
                self.siguiente_turno()
                return False
            case 'all_vowels':
                self.vista.weel_allvowels()
                self.vista.prove_letter("consonante")
                letra = self.vista.prove_letter("consonante")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.__panel_list[self.num_panel].comprobar_letra("a")
                    self.__panel_list[self.num_panel].comprobar_letra("e")
                    self.__panel_list[self.num_panel].comprobar_letra("i")
                    self.__panel_list[self.num_panel].comprobar_letra("o")
                    self.__panel_list[self.num_panel].comprobar_letra("u")
                    return True
                else:
                    self.siguiente_turno()
                    return False
            case 'x2':
                self.vista.weel_x2()
                self.vista.prove_letter("consonante")
                letra = self.vista.prove_letter("consonante")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.jugadores[self.turno].puntos_ronda *= 2
                    return True
                else:
                    self.siguiente_turno()
                    return False
            case '1/2':
                self.vista.prove_letter("consonante")
                letra = self.vista.prove_letter("consonante")
                if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                    self.jugadores[self.turno].puntos_ronda //= 2
                    return True
                else:
                    self.siguiente_turno()
                    return False
            case _: #cualquier opcion de puntos normal
                try:
                    selection = int(selection)
                    self.vista.weel_points(selection)
                    letra = self.vista.prove_letter("consonante")
                    if self.__panel_list[self.num_panel].comprobar_letra(letra) > 0:
                        self.jugadores[self.turno].puntos_ronda += self.__panel_list[self.num_panel].comprobar_letra(letra) * selection
                        return True
                    else:
                        self.siguiente_turno()
                        return False
                except ValueError:
                    self.vista.error("Error en la tirada, valor 'selection' no previsto")
                    return True

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
                player_round = True

                while player_round == True:
                    self.vista.pintar_panel(self.__panel_list[self.num_panel])
                    self.vista.pintar_jugadores(self.jugadores[self.turno])
                    opcion_juego = self.vista.game_menu(self.jugadores[self.turno].nombre)
                    match opcion_juego:
                        case 1: #Tirar ruleta
                            first_throw = True
                            player_round = self.weel_throw()

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
                                    player_round = False

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
                                    player_round = False
                                    self.control_puntos()
                                    self.vista.pintar_panel(self.__panel_list[self.num_panel])
                                    self.vista.end_points(self.jugadores)
                                else:
                                    self.siguiente_turno()
                                    player_round = False

                        case 4: #Salir
                            answer = self.vista.double_check()
                            if answer:
                                exit()
                        case _:
                            raise ValueError("Valor incorrecto en mach case")

                self.num_panel += 1
        self.vista.end_points(self.jugadores)









#Tests
if __name__ == "__main__":
    juego = Juego()
    juego.run()
