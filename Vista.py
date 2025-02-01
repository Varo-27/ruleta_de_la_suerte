import os
import time
from panel import Panel         #Solo para type hints
from jugador import Jugador     #Solo para type hints

class Vista():

    #Funciones solo de impresión
    #===========================

    def welcome(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido a la Ruleta de la suerte")
        print("===================================")

    def starting_game(self) -> None:
        print("Jugadores listos, empezando partida...")
        time.sleep(2)

    def error(self, menssaje: str) -> None:
        print(f"Error introduciendo datos: {menssaje}")
        input("Pulsa enter para continuar...")

    def choice(self) -> None:
        print("Elige una opción: ", end="")

    def weel_bankrupt(self) -> None:
        print("Has caido en la quiebra")
        time.sleep(2)

    def weel_allvowels(self) -> None:
        print("Acierta la consonante y desbloquea todas las vocales")

    def weel_x2(self) -> None:
        print("Acierta la consonante y duplica tus puntos esta ronda")

    def weel_lose_turn(self) -> None:
        print("Pierdes el turno")
        time.sleep(2)

    def weel_points(self, section: int) -> None:
        print(f"Has caido en {section} puntos")

    def end_points(self, jugadores: list[Jugador]) -> None:
        for jugador in jugadores:
            print(jugador.pintar_total())
        input("Pulsa enter para continuar...")

    def pintar_panel(self, panel: Panel) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(panel)

    def pintar_jugadores(self, jugador: Jugador) -> None:
        print(jugador)

    def phrase_register(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("REGISTRANDO NUEVA ENTRADA EN EL JUEGO")
        print("=====================================")


    #Funciones con input
    #===================

    def start_menu(self) -> int:
        print("1.Añadir jugadores")
        print("2.Scoreboard")
        print("3.Añadir nuevo panel")
        print("4.Salir")
        answer = 0
        valid_answer = False
        while valid_answer == False:
            try:
                self.choice()
                answer = int(input())
                if answer in [1, 2, 3]:
                    valid_answer = True
                else:
                    self.error("Valor incorrecto")
            except:
                self.error("Tipo de dato incorrecto")
        return answer

    def game_menu(self, player_name: str) -> int:
        print(f"Turno de {player_name}")
        print("1. Tirar")
        print("2. Comprar vocal (50 puntos)")
        print("3. Resolver")
        print("4. Salir")
        answer = 0
        valid_answer = False
        while valid_answer == False:
            try:
                self.choice()
                answer = int(input())
                if answer in [1, 2, 3, 4]:
                    valid_answer = True
                else:
                    print("\033[F\033[K", end="")
                    self.error("Valor incorrecto")
            except:
                print("\033[F\033[K", end="")
                self.error("Tipo de dato incorrecto")
        return answer

    def phrase_entry(self,msg: str) -> str:
        print(f"{msg}: ", end="")
        answer = ""
        valid_answer = False
        while valid_answer == False:
            try:
                answer = input().lower()
                valid_answer = True
            except: 
                self.error("Tipo de dato incorrecto")
        return answer

    def prove_letter(self, letter_type: str) -> str:
        consonants = "bcdfghjklmnñpqrstvwxyz"
        vowels = "aeiou"
        answer = ""
        valid_answer = False
        while valid_answer == False:
            try:
                print(f"Introduce una {letter_type}: ", end="")
                answer = input().lower()
                if len(answer) == 1:
                    if letter_type == "consonante" and answer in consonants:
                        valid_answer = True
                    elif letter_type == "vocal" and answer in vowels:
                        valid_answer = True
                    else:
                        self.error("Letra no reconocida")
                else:
                    self.error("Solo una letra")
            except:
                self.error("Tipo de dato incorrecto")
        return answer

    def player_name(self, num_jugador: int) -> str:
        print(f"Nombre del Jugador {num_jugador}: ", end="")
        player_name = ""
        valid_answer = False
        while valid_answer == False:
            player_name = input()
            if len(player_name) > 0:
                valid_answer = self.double_check()
            else:
                print("Introducelo de nuevo: ", end="")
        return player_name

    def num_participantes(self) -> int:
        print("Introduce el número de participantes (2 o 3): ", end="")
        answer = 0
        valid_answer = False
        while valid_answer == False:
            try:
                answer = int(input())
                if 1 < answer < 4:
                    valid_answer = True
            except:
                self.error("Tipo de dato incorrecto")
        return answer

    def double_check(self) -> bool:
        print("Seguro? (s/N): ", end="")
        answer = input()
        if answer.lower() == "s":
            return True
        else:
            return False








if __name__ == "__main__":
    v = Vista()
    v.prove_letter("consonante")