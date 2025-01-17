class Panel:

    def __init__(self,frase: str) -> None:
        self.frase = frase.lower()

        self.letras_acertadas = [" "]
        self.letras_falladas = ["j", "k", "w", "m"]

    def comprobar_letra(self, letra):
        if letra in self.frase:
            self.letras_acertadas.append(letra)
            self.letras_acertadas.sort()
        else:
            self.letras_falladas.append(letra)
            self.letras_falladas.sort()
    
    def __str__(self) -> str:
        frase_oculta = " ".join(letra if letra in self.letras_acertadas else "_" for letra in self.frase).upper()
        frase_fallos = f"Letras ya probadas: {", ".join(self.letras_falladas).upper()}"
        return frase_oculta + "\n"*2 + frase_fallos


import animation
if __name__ == "__main__":

    pregunta1 = {
        "frase" : "Es una frase de prueba",
        "pista" : "Pista de prueba"
    }
    pregunta1 = {
        "frase" : "Es una frase de prueba",
        "pista" : "Pista de prueba"
    }


    frase_prueba = Panel("Es una frase de prueba")
    frase_prueba.comprobar_letra("a")
    frase_prueba.comprobar_letra("f")
    frase_prueba.comprobar_letra("b")
    frase_prueba.comprobar_letra("e")
    frase_prueba.comprobar_letra("r")
    print(frase_prueba)
    animation.animation()
