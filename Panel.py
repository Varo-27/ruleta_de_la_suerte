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
    incognita = Panel("Es una frase de prueba")
    incognita.comprobar_letra("a")
    incognita.comprobar_letra("f")
    incognita.comprobar_letra("b")
    incognita.comprobar_letra("e")
    incognita.comprobar_letra("r")
    print(incognita)
    animation.animation()
