class Decorador:
    def __init__(self, letras_acertadas):
        self.letras_acertadas = letras_acertadas

    def decorar_letra(self, letra: str):
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
                "|░░░░░|",
                "|░   ░|",
                "|░░░░░|",
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

    def decorar_frase(self, frase):
        # Buscar el espacio más cercano a la mitad de la frase
        mitad = len(frase) // 2
        mejor_corte = len(frase)
        for i in range(mitad - 3, mitad + 10):
            if frase[i] == ' ':
                mejor_corte = i
                break

        #Ocultar las letras no acertadas
        print(frase)
        frase_oculta = "".join([letra.upper() if letra in self.letras_acertadas else "_" for letra in frase])

        # Dividir la frase en dos líneas
        linea1 = frase_oculta[:mejor_corte].strip()
        linea2 = frase_oculta[mejor_corte:].strip()

        # Decorar cada línea
        decorada1 = [self.decorar_letra(letra) for letra in linea1]
        decorada2 = [self.decorar_letra(letra) for letra in linea2]

        # Unir las partes de cada línea en filas horizontales
        filas1 = ["", "", "", "", ""]
        filas2 = ["", "", "", "", ""]
        for letra in decorada1:
            for i in range(5):
                filas1[i] += letra[i] + "  "
        for letra in decorada2:
            for i in range(5):
                filas2[i] += letra[i] + "  "

        # Combinar las filas de ambas líneas con un separador
        return "\n".join(filas1) + "\n\n" + "\n".join(filas2)

# Ejemplo de uso
letras_acertadas = {'E', 'S', 'U', 'A', 'R', 'O', ' '}  # Ejemplo de letras acertadas
decorador = Decorador(letras_acertadas)
frase = "ES UNA FRASE DE PRUEBA UNO"
print(decorador.decorar_frase(frase))
