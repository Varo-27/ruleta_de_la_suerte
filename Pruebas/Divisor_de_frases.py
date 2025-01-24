if __name__ == "__main__":
    import textwrap
    frase = "la mejor frase de prueba posible"
    lineas_divididas = textwrap.wrap(frase, 17)
    frase_dividida = "\n".join(lineas_divididas)
    print(frase_dividida)