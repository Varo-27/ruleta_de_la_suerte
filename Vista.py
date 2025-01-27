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

    def pintar_panel(self, panel: Panel) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(panel)

    def choice(self) -> None:
        print("Elige una opción: ", end="")

    def bankrupt(self) -> None:
        print("Has caido en la quiebra")
        time.sleep(2)

    def lose_turn(self) -> None:
        print("Pierdes el turno")
        time.sleep(2)

    def end_points(self, jugadores: list[Jugador]) -> None:
        for jugador in jugadores:
            print(jugador.pintar_total())
        input("Pulsa enter para continuar...")

    def pintar_jugadores(self, jugador: Jugador) -> None:
        print(jugador)



    #Funciones con input
    #===================

    def start_menu(self) -> int:
        print("1.Añadir jugadores")
        print("2.Scoreboard")
        print("3.Salir")
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
        print("2. Comprar vocal")
        print("3. Resolver")
        print("4. Salir")
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

    def solve(self) -> str:
        print("Respuesta final: ")
        valid_answer = False
        while valid_answer == False:
            try:
                answer = input()
            except: 
                self.error("Tipo de dato incorrecto")
        return answer

    def consonant(self) -> str:
        print("Introduce consonante: ")
        valid_answer = False
        while valid_answer == False:
            try:
                answer = input()
                if len(answer) == 1 and answer.lower() in "bcdfghjklmnñpqrstvwxyz":
                    valid_answer = True
                else:
                    self.error("Valor incorrecto")
            except:
                self.error("Tipo de dato incorrecto")
        return answer

    def vowel(self) -> str:
        print("Introduce vocal: ")
        valid_answer = False
        while valid_answer == False:
            try:
                answer = input()
                if len(answer) == 1 and answer.lower() in "aeiou":
                    valid_answer = True
                else:
                    self.error("Valor incorrecto")
            except:
                self.error("Tipo de dato incorrecto")
        return answer


    def player_name(self, num_jugador: int) -> str:
        print(f"Nombre del Jugador {num_jugador}: ", end="")
        valid_answer = False
        while valid_answer == False:
            player_name = input()
            respuesta = "s" #input(f"El nombre del jugador {num_jugador} es {nombre}, ¿es correcto? (s/n): ")
            if respuesta.lower() == "s":
                valid_answer = True
            else:
                print("Introducelo de nuevo: ", end="")
        return player_name

    def num_participantes(self) -> int:
        print("Introduce el número de participantes (2 o 3): ", end="")
        valid_answer = False
        while valid_answer == False:
            try:
                answer = int(input())
                if 1 < answer < 4:
                    valid_answer = True
            except:
                self.error("Tipo de dato incorrecto")
        return answer

    def end_game(self) -> None:
        print("Seguro que quieres salir? (s/N): ", end="")
        answer = input()
        if answer.lower() == "s":
            exit()
        else:
            return
