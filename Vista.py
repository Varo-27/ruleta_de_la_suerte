import os

class Vista():

    def inicio():
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido a la Ruleta de la suerte")
        print("===================================")

    def menu_opciones():
        print("1.Añadir jugadores \n2.Scoreboard")
