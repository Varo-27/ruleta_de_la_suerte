import os
import time

class Vista():

    def inicio(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido a la Ruleta de la suerte")
        print("===================================")

    def menu_opciones(self):
        print("1.Añadir jugadores \n2.Scoreboard")
    
    def elegir(self):
        print("Elige una opción: ", end="")

    def num_participantes(self):
        print("Introduce el número de participantes: ", end="")

    def error(self):
        print("Error al introducir los datos")

    def nombre_jugador(self, num_jugador):
        print(f"Nombre del Jugador {num_jugador}: ", end="")

    def empezando_partida(self):
        print("Jugadores listos, empezando partida...")
        time.sleep(2)
        print("\033[F\033[K", end="")

    def pintar_panel(self):
        print()