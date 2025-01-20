import os
import time

class Vista():

    def inicio(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido a la Ruleta de la suerte")
        print("===================================")

    def menu_inicio(self):
        print("1.Añadir jugadores")
        print("2.Scoreboard")

    def menu_juego(self):
        print("1. Tirar")
        print("2. Comprar vocal")
        print("3. Resolver")
    
    def elegir(self):
        print("Elige una opción: ", end="")

    def num_participantes(self) -> int:
        print("Introduce el número de participantes: ", end="")
        return int(input())

    def error(self, menssaje):
        print(f"Error introduciendo datos: {menssaje}")

    def nombre_jugador(self, num_jugador: int) -> str:
        print(f"Nombre del Jugador {num_jugador}: ", end="")
        return input()

    def empezando_partida(self):
        print("Jugadores listos, empezando partida...")
        time.sleep(2)
        print("\033[F\033[K", end="")

    def pintar_panel(self):
        print()