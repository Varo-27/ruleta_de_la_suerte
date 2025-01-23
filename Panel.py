class Panel:

    def __init__(self,panel: tuple):
        self.frase = panel[0]
        self.pista = panel[1]
        self.letras_acertadas = [" "]
        self.letras_falladas = []

    def comprobar_letra(self, letra: str) -> int:
        if letra in self.frase:
            self.letras_acertadas.append(letra)
            self.letras_acertadas.sort()
            return self.frase.count(letra)
        else:
            self.letras_falladas.append(letra)
            self.letras_falladas.sort()
            return 0

    def comprobar_resolucion(self, resolucion: str)  -> bool:
        if resolucion.lower() == self.frase.lower():
            return True
        else:
            return False

    def decorar_letra(self, letra: str) -> list[str]:
        if letra == " ":
            return [
                " _____ ",
                "|█████|",
                "|█████|",
                "|█████|",
                " ‾‾‾‾‾ "
            ]
        elif letra == "_":
            return [
                " _____ ",
                "|     |",
                "|  ░  |",
                "|     |",
                " ‾‾‾‾‾ "
            ]       
        else:
            return [
                " _____ ",
                "|     |",
                "|  {}  |".format(letra),
                "|     |",
                " ‾‾‾‾‾ "
            ]

    def decorar_frase(self, frase: str) -> str:
        # Buscar el espacio más cercano a la mitad de la frase
        mitad = len(frase) // 2
        mejor_corte = len(frase)
        for i in range(mitad + 10, mitad - 3, -1):
            if frase[i] == ' ':
                mejor_corte = i

        #Ocultar las letras no acertadas
        print(frase)
        frase_oculta = "".join([letra.upper() if letra in self.letras_acertadas else "_" for letra in frase])

        # Dividir la frase en dos líneas
        linea1 = frase_oculta[:mejor_corte].strip()
        decorada1 = [self.decorar_letra(letra) for letra in linea1]

        linea2 = frase_oculta[mejor_corte:].strip()
        decorada2 = [self.decorar_letra(letra) for letra in linea2]

        # Unir las partes de cada línea en filas horizontales
        filas1 = ["", "", "", "", ""]
        for letra in decorada1:
            for i in range(5):
                filas1[i] += letra[i] + "  "

        filas2 = ["", "", "", "", ""]
        for letra in decorada2:
            for i in range(5):
                filas2[i] += letra[i] + "  "

        # Combinar las lineas del panel
        return "\n".join(filas1) + "\n" + "\n".join(filas2)

    def __str__(self) -> str:
        frase_oculta = self.decorar_frase(self.frase)
        pista = self.pista
        frase_fallos = f"Letras ya probadas: {", ".join(self.letras_falladas).upper()}"
        return frase_oculta + "\n"*2 + frase_fallos + "\n"*2 + pista + "\n"














if __name__ == "__main__":
    import animation
    import os

    os.system("cls" if os.name == "nt" else "clear")
    pregunta1 = {
        "frase" : "la mejor frase de prueba posible",
        "pista" : "Pista de prueba"
    }
    pregunta2 = {
        "frase" : "es una frase de prueba dos",
        "pista" : "Pista de prueba dos"
    }

    pregunta = (pregunta1["frase"], pregunta1["pista"])

    frase_prueba = Panel(pregunta)
    frase_prueba.comprobar_letra("a")
    frase_prueba.comprobar_letra("f")
    frase_prueba.comprobar_letra("b")
    frase_prueba.comprobar_letra("e")
    frase_prueba.comprobar_letra("r")
    frase_prueba.comprobar_letra("d")
    frase_prueba.comprobar_letra("k")
    frase_prueba.comprobar_letra("w")
    frase_prueba.comprobar_letra("m")
    frase_prueba.comprobar_letra("l")
    print(frase_prueba)
    #animation.animation()
    while True:
        pass
