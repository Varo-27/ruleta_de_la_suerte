from textwrap import wrap
# from pathlib import Path
#import pyfiglet

class Panel:
    __frase: str
    __pista: str
    letras_acertadas: list[str]
    letras_falladas: list[str]
    resuelto: bool

    def __init__(self,panel: tuple[str, str]):
        self.__frase = panel[0]
        self.__pista = Panel.decorar_pista(panel[1])
        self.letras_acertadas = [" ", ","]
        self.letras_falladas = []
        self.resuelto = False

    @property
    def frase(self):
        return self.__frase
    
    @staticmethod
    def decorar_pista(pista: str) -> str:
        pista =pista.upper().center(111, " ")
        linea = "="*111

        # root_dir = Path(__file__).resolve().parent.parent
        # font_path = root_dir / "font" / "calvinss"
        # figlet = pyfiglet.Figlet(font= f"{font_path}", justify="center")
        # figlet.width = 111
        # pista = figlet.renderText(pista)

        return linea + "\n" + pista + "\n" + linea


    def check_letter(self, letra: str) -> int:
        if letra in self.__frase:
            if letra.upper() not in self.letras_acertadas:
                self.letras_acertadas.append(letra.upper())
                self.letras_acertadas.sort()
                return self.__frase.count(letra)
            else:
                return -1
        else:
            self.letras_falladas.append(letra)
            self.letras_falladas.sort()
            return 0

    def comprobar_resolucion(self, resolucion: str)  -> bool:
        if resolucion.lower() == self.__frase.lower():
            self.resuelto = True
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
                "| ▀▀▀ |",
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

    def decorar_frase(self):
        if self.resuelto is False:
            frase = "".join([letra if letra.upper() in self.letras_acertadas else "_" for letra in self.frase])
        else:
            frase = self.frase

        MAXLENGHT = 14

        #Separa la frase en lineas de 14 caracteres como maximo
        divided_lines = wrap(frase.upper(), MAXLENGHT)

        centered_lines = [linea.center(MAXLENGHT, " ") for linea in divided_lines]
        lines = [["", "", "", "", ""] for _ in range(len(centered_lines))]

        for index, line in enumerate(centered_lines):                       #Cada linea de la frase
            decorada = [self.decorar_letra(letter) for letter in line]      #Decorar cada letra de la linea
            for letter in decorada:                                         #Cada letra de la linea ya decorada
                for i in range(5):                                          #5 filas por letra
                    lines[index][i] += letter[i] + " "                      #Añade la fila de la letra a la fila de la linea

        return "\n".join("\n".join(line) for line in lines) #Junta las filas de cada linea, y todas las lineas

    def __str__(self) -> str:
        frase_oculta = self.decorar_frase()
        frase_fallos = f"Letras ya probadas: {", ".join(self.letras_falladas).upper()}"
        return frase_oculta + "\n" + self.__pista + "\n" + frase_fallos + "\n"














if __name__ == "__main__":
    import os

    os.system("cls" if os.name == "nt" else "clear")
    pregunta1 = {
        "frase" : "en un lugar de la mancha de cuyo nombre",
        "pista" : "es una pedazo de pista de prueba"
    }

    pregunta = (pregunta1["frase"], pregunta1["pista"])
    frase_prueba = Panel(pregunta)

    letras = "aafberdkwmlopst"
    for caracter in letras:
        frase_prueba.check_letter(caracter)
    print(frase_prueba)
    while True:
        pass