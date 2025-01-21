class Panel:

    def __init__(self,panel: tuple) -> None:
        self.frase = panel[0]
        self.pista = panel[1]
        self.letras_acertadas = [" "]
        self.letras_falladas = []

    def comprobar_letra(self, letra):
        if letra in self.frase:
            self.letras_acertadas.append(letra)
            self.letras_acertadas.sort()
            return self.frase.count(letra)
        else:
            self.letras_falladas.append(letra)
            self.letras_falladas.sort()

    def comprobar_resolucion(self, resolucion):
        if resolucion == self.frase:
            return True
        else:
            return False

    def __str__(self) -> str:
        frase_oculta = " ".join(letra if letra in self.letras_acertadas else "_" for letra in self.frase).upper()
        pista = self.pista
        frase_fallos = f"Letras ya probadas: {", ".join(self.letras_falladas).upper()}"
        return frase_oculta + "\n"*2 + frase_fallos + "\n"*2 + pista














if __name__ == "__main__":
    import animation

    pregunta1 = {
        "frase" : "es una frase de prueba",
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
    frase_prueba.comprobar_letra("j")
    frase_prueba.comprobar_letra("k")
    frase_prueba.comprobar_letra("w")
    frase_prueba.comprobar_letra("m")
    frase_prueba.comprobar_letra("l")
    print(frase_prueba)
    animation.animation()
