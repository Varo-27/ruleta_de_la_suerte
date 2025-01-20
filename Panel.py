class Panel:

    def __init__(self,panel: tuple) -> None:
        self.frase = panel[0]
        self.pista = panel[1]
        self.letras_acertadas = [" "]
        self.letras_falladas = ["j", "k", "w", "m"]

    def comprobar_letra(self, letra):
        if letra in self.frase["frase"]:
            self.letras_acertadas.append(letra)
            self.letras_acertadas.sort()
        else:
            self.letras_falladas.append(letra)
            self.letras_falladas.sort()

    def __str__(self) -> str:
        frase_oculta = " ".join(letra if letra in self.letras_acertadas else "_" for letra in self.frase["frase"]).upper()
        pista = self.frase["pista"]
        frase_fallos = f"Letras ya probadas: {", ".join(self.letras_falladas).upper()}"
        return frase_oculta + "\n"*2 + frase_fallos + "\n"*2 + pista


import animation
if __name__ == "__main__":

    pregunta1 = {
        "frase" : "Es una frase de prueba",
        "pista" : "Pista de prueba"
    }
    pregunta2 = {
        "frase" : "Es una frase de prueba dos",
        "pista" : "Pista de prueba dos"
    }


    frase_prueba = Panel(pregunta1)
    frase_prueba.comprobar_letra("a")
    frase_prueba.comprobar_letra("f")
    frase_prueba.comprobar_letra("b")
    frase_prueba.comprobar_letra("e")
    frase_prueba.comprobar_letra("r")
    print(frase_prueba)
    animation.animation()
