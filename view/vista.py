"""
Vista
===== 
Archivo que contiene la clase Vista, que se encarga de la interacción con el usuario.
Contiene funciones para imprimir mensajes y solicitar datos al usuario.
"""

import os
import time
import getpass
from models import Jugador, Panel

class Vista():


#Funciones solo de impresión
#===========================

    def welcome(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido a la Ruleta de la suerte")
        print("===================================")

    def starting_game(self) -> None:
        print("Jugadores listos, empezando partida...")
        time.sleep(1)

    def error(self, menssaje: str) -> None:
        print(f"Error introduciendo datos: {menssaje}")
        input("Pulsa enter para continuar...")

    def choice(self) -> None:
        print("Elige una opción: ", end="")

    def phrase_register(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Menú de registro de frases")
        print("==========================")

    def login_success(self) -> None:
        print("Login correcto")


    # Tiradas ruleta

    def wheel_bankrupt(self) -> None:
        print("Has caido en la quiebra")
        input("Pulsa enter para continuar...")

    def wheel_lose_turn(self) -> None:
        print("Pierdes el turno")
        input("Pulsa enter para continuar...")

    def wheel_allvowels(self) -> None:
        print("Acierta la consonante y desbloquea todas las vocales")

    def wheel_x2(self) -> None:
        print("Acierta la consonante y duplica tus puntos esta ronda")

    def wheel_1_2(self) -> None:
        print("Acierta la consonante y reduce tus puntos a la mitad pero puedes seguir jugando")

    def wheel_points(self, section: int) -> None:
        print(f"Has caido en {section} puntos")


    # Paneles y puntuaciones

    def end_points(self, jugadores: list[Jugador]) -> None:
        for jugador in jugadores:
            print(jugador.pintar_total())
        input("Pulsa enter para continuar...")

    def print_panel(self, panel: Panel) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(panel)

    def print_players(self, jugador: Jugador) -> None:
        print(jugador)


#Funciones con input
#===================

    def start_menu(self) -> int:
        print("1.Añadir jugadores")
        print("2.Scoreboard")
        print("3.Registro")
        print("4.Salir")
        answer = 0
        valid_answer = False
        while valid_answer is False:
            try:
                self.choice()
                answer = int(input())
                if answer in [1, 2, 3, 4]:
                    valid_answer = True
                else:
                    self.error("Valor incorrecto")
            except ValueError:
                self.error("Tipo de dato incorrecto")
        return answer

    def game_menu(self, player_name: str) -> int:
        print(f"Turno de {player_name}")
        print("1. Tirar")
        print("2. Comprar vocal (50 puntos)")
        print("3. Resolver")
        print("4. Pasar turno")
        answer = 0
        valid_answer = False
        while valid_answer is False:
            try:
                self.choice()
                answer = int(input())
                if answer in [1, 2, 3, 4]:
                    valid_answer = True
                else:
                    print("\033[F\033[K", end="")
                    self.error("Valor incorrecto")
            except ValueError:
                print("\033[F\033[K", end="")
                self.error("Tipo de dato incorrecto")
        return answer

    def num_rounds(self) -> int:
        print("Elige el numero de rondas (1-6): ", end="")
        answer = 0
        valid_answer = False
        while valid_answer is False:
            try:
                self.choice()
                answer = int(input())
                if answer in [1, 2, 3, 4, 5, 6]:
                    valid_answer = True
                else:
                    print("\033[F\033[K", end="")
                    self.error("Valor incorrecto")
            except ValueError:
                print("\033[F\033[K", end="")
                self.error("Tipo de dato incorrecto")
        return answer

    def get_password(self, msg :str) -> str:
        return getpass.getpass(f"{msg}: ")

    def phrase_entry(self,msg: str, double_check: bool = False) -> str:
        """
        Introduce una frase y comprueba que no esté vacía

        Args:
            msg (str): Descripción de la frase a introducir
            double_check (bool, optional): Pregunta por confirmacion. Defaults to False.

        Returns:
            str: _description_
        """
        print(f"{msg}: ", end="")
        answer = ""
        valid_answer = False
        while valid_answer is False:
            try:
                answer = input().lower()
                if len(answer) > 0:
                    if double_check is True:
                        valid_answer = self.double_check()
                    else:
                        valid_answer = True
                else:
                    self.error("Este campo no puede estar vacío")
            except (EOFError, KeyboardInterrupt) as e:
                self.error(f"Error inesperado: {e}")
        return answer

    def prove_letter(self, letter_type: str) -> str:
        """
        Introduce una letra y comprueba que sea válida

        Args:
            letter_type (str):  Tipo de letra a introducir
                - consonant
                - vowel

        Returns:
            str: Una letra válida
        """
        consonants = "bcdfghjklmnñpqrstvwxyz"
        vowels = "aeiou"
        answer = ""
        valid_answer = False
        while valid_answer is False:
            try:
                print(f"Introduce una {letter_type}: ", end="")
                answer = input().lower()
                if len(answer) == 1:
                    #Consonante
                    if letter_type == "consonante" and answer in consonants:
                        valid_answer = True
                    #Vocal
                    elif letter_type == "vocal" and answer in vowels:
                        valid_answer = True
                    else:
                        self.error("Letra no reconocida")
                else:
                    self.error("Solo una letra")
            except (EOFError, KeyboardInterrupt) as e:
                self.error(f"Error inesperado: {e}")
        return answer

    def player_name(self, num_jugador: int) -> str:
        player_name = ""
        valid_answer = False
        while valid_answer is False:
            print(f"Nombre del Jugador {num_jugador}: ", end="")
            player_name = input()
            if len(player_name) > 0:
                valid_answer = self.double_check()
            else:
                print("Introducelo de nuevo: ", end="")
        return player_name

    def num_players(self) -> int:
        print("Introduce el número de participantes (3 max): ", end="")
        answer = 0
        valid_answer = False
        while valid_answer is False:
            try:
                answer = int(input())
                if 1 <= answer < 4:
                    valid_answer = True
            except ValueError:
                self.error("Tipo de dato incorrecto")
            except (EOFError, KeyboardInterrupt) as e:
                self.error(f"Error inesperado: {e}")
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
