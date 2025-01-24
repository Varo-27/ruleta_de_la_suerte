from textwrap import wrap

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
                "|     |",
                "| *** |",
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

    def decorar_frase(self, frase: str):
        hidden_phrase = "".join([letra.upper() if letra in self.letras_acertadas else "_" for letra in frase])

        MAXLENGHT = 14
        divided_lines = wrap(hidden_phrase, MAXLENGHT)

        max_length = max([len(linea) for linea in divided_lines])
        centered_lines = [linea.center(max_length, " ") for linea in divided_lines]
        print(centered_lines)
        lines = [["", "", "", "", ""] for _ in range(len(centered_lines))]

        for index, line in enumerate(centered_lines):
            decorada = [self.decorar_letra(letter) for letter in line]
            for letter in decorada:
                for i in range(5):
                    lines[index][i] += letter[i] + " "


        return "\n\n".join("\n".join(line) for line in lines)


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
        "frase" : "en un lugar de la mancha de cuyo nombre",
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
    frase_prueba.comprobar_letra("o")
    frase_prueba.comprobar_letra("p")
    frase_prueba.comprobar_letra("s")
    frase_prueba.comprobar_letra("t")
    print(frase_prueba)
    animation.animation()
    while True:
        pass
