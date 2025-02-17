from textwrap import wrap
import pyfiglet

class Panel:
    __frase: str
    __pista: str
    letras_acertadas: list[str]
    letras_falladas: list[str]
    resuelto: bool

    def __init__(self,panel: tuple[str, str]):
        self.__frase = panel[0]
        self.__pista = Panel.decorar_pista(panel[1])
        self.letras_acertadas = [" "]
        self.letras_falladas = []
        self.resuelto = False

    @property
    def frase(self):
        return self.__frase
    
    @staticmethod
    def decorar_pista(pista: str) -> str:
        pista =pista.lower()
        figlet = pyfiglet.Figlet(font= "font/calvinss", justify="center")
        figlet.width = 111
        pista = figlet.renderText(pista)
        linea = "="*111
        linea2 = "="*111
        return linea + "\n" + pista + linea2


    def comprobar_letra(self, letra: str) -> int:
        if letra in self.__frase:
            self.letras_acertadas.append(letra.upper())
            self.letras_acertadas.sort()
            return self.__frase.count(letra)
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
        if self.resuelto == False:
            frase = "".join([letra if letra.upper() in self.letras_acertadas else "_" for letra in self.frase])
        else:
            frase = self.frase
            
        MAXLENGHT = 14
        divided_lines = wrap(frase.upper(), MAXLENGHT)                      #Separa la frase en lineas de 14 caracteres como maximo

        centered_lines = [linea.center(MAXLENGHT, " ") for linea in divided_lines]
        lines = [["", "", "", "", ""] for _ in range(len(centered_lines))]

        for index, line in enumerate(centered_lines):                       #Cada linea de la frase
            decorada = [self.decorar_letra(letter) for letter in line]      #Decorar cada letra de la linea
            for letter in decorada:                                         #Cada letra de la linea ya decorada 
                for i in range(5):                                          #Cada linea son 5 filas de letra                                      
                    lines[index][i] += letter[i] + " "                      #Añade la fila de la letra a la fila de la linea

        return "\n".join("\n".join(line) for line in lines)               #Junta las filas de la frase con un salto de linea y las lineas de la frase con dos saltos de linea

    def __str__(self) -> str:
        frase_oculta = self.decorar_frase()
        frase_fallos = f"Letras ya probadas: {", ".join(self.letras_falladas).upper()}"
        return frase_oculta + "\n" + self.__pista + "\n" + frase_fallos














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
    for letra in letras:
        frase_prueba.comprobar_letra(letra)
    print(frase_prueba)
    # while True:
    #     pass