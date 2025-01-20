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
        print("3.Salir")
        while True:
            try:
                answer = int(input())
                if answer in [1, 2, 3]:
                    return answer
                else:
                    self.error("Valor incorrecto")
            except:
                self.error("Tipo de dato incorrecto")

    def menu_juego(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("1. Tirar")
        print("2. Comprar vocal")
        print("3. Resolver")
        print("4. Salir")
        while True:
            try:
                answer = int(input())
                if answer in [1, 2, 3, 4]:
                    return answer
                else:
                    self.error("Valor incorrecto")
            except:
                self.error("Tipo de dato incorrecto")
    
    def elegir(self):
        print("Elige una opción: ", end="")

    def num_participantes(self) -> int:
        print("Introduce el número de participantes: ", end="")
        while True:
            try:
                answer = int(input())
                return answer
            except:
                self.error("Tipo de dato incorrecto")

    def error(self, menssaje):
        print(f"Error introduciendo datos: {menssaje}")

    def nombre_jugador(self, num_jugador: int) -> str:
        print(f"Nombre del Jugador {num_jugador}: ", end="")
        while True:
            nombre = input()
            respuesta = input(f"El nombre del jugador {num_jugador} es {nombre}, ¿es correcto? (s/n): ")
            if respuesta.lower() == "s":
                return nombre
            else:
                print("Introducelo de nuevo: ", end="")

    def empezando_partida(self):
        print("Jugadores listos, empezando partida...")
        time.sleep(2)
        print("\033[F\033[K", end="")

    def pintar_panel(self):
        print()