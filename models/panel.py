from textwrap import wrap
class Panel:
    __phrase: str
    __hint: str
    correct_letters: list[str]
    incorrect_letters: list[str]
    __solved: bool

    def __init__(self,panel: tuple[str, str]):
        self.__phrase = panel[0]
        self.__hint = Panel.decorate_hint(panel[1])
        self.correct_letters = [" ", ","]
        self.incorrect_letters = []
        self.__solved = False

    @property
    def phrase(self):
        return self.__phrase


    @staticmethod
    def decorate_hint(hint: str) -> str:
        hint =hint.upper().center(111, " ")
        line = "="*111
        return line + "\n" + hint + "\n" + line


    def check_letter(self, letter: str) -> int:
        if letter in self.__phrase:
            if letter.upper() not in self.correct_letters:
                self.correct_letters.append(letter.upper())
                self.correct_letters.sort()
                return self.__phrase.count(letter)
            else:
                return -1
        else:
            self.incorrect_letters.append(letter)
            self.incorrect_letters.sort()
            return 0

    def check_solution(self, solution: str)  -> bool:
        if solution.lower() == self.__phrase.lower():
            self.__solved = True
            return True
        else:
            return False

    def decorate_letter(self, letra: str) -> list[str]:
        if letra == " ":
            return [
                " _____ ",
                "│█████│",
                "│█████│",
                "│█████│",
                " ‾‾‾‾‾ "
            ]
        elif letra == "_":
            return [
                " _____ ",
                "│     │",
                "│     │",
                "│ ▀▀▀ │",
                " ‾‾‾‾‾ "
            ]
        else:
            return [
                " _____ ",
                "│     │",
                "│  {}  │".format(letra),
                "│     │",
                " ‾‾‾‾‾ "
            ]

    def decorate_phrase(self):
        phrase = self.__phrase

        if self.__solved is False:
            phrase = "".join([letra if letra.upper() in self.correct_letters else "_" for letra in self.__phrase])

        MAXLENGHT = 14

        #Separa la frase en lineas de 14 caracteres como maximo
        divided_lines = wrap(phrase.upper(), MAXLENGHT)

        centered_lines = [linea.center(MAXLENGHT, " ") for linea in divided_lines]
        lines = [["", "", "", "", ""] for _ in range(len(centered_lines))]

        for index, line in enumerate(centered_lines):                       #Cada linea de la frase
            decorated = [self.decorate_letter(letter) for letter in line]      #Decorar cada letra de la linea
            for letter in decorated:                                         #Cada letra de la linea ya decorada
                for i in range(5):                                          #5 filas por letra
                    lines[index][i] += letter[i] + " "                      #Añade la fila de la letra a la fila de la linea

        return "\n".join("\n".join(line) for line in lines) #Junta las filas de cada linea, y todas las lineas

    def __str__(self) -> str:
        hidden_phrase = self.decorate_phrase()
        failed_letters = f"Letras ya probadas: {", ".join(set(sorted(self.incorrect_letters))).upper()}"
        return hidden_phrase + "\n" + self.__hint + "\n" + failed_letters + "\n"



#TEST
if __name__ == "__main__":
    import os

    os.system("cls" if os.name == "nt" else "clear")
    pregunta1 = {
        "frase" : "en un lugar de la mancha de cuyo nombre",
        "pista" : "es una pedazo de pista de prueba"
    }

    pregunta = (pregunta1["frase"], pregunta1["pista"])
    frase_prueba = Panel(pregunta)

    letras = "aafffffffberdkwmlopst"
    for caracter in letras:
        frase_prueba.check_letter(caracter)
    print(frase_prueba)
    while True:
        pass