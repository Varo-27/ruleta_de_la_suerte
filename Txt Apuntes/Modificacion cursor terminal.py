import time

def ejemplo_10C():
    print("Comenzando ejemplo de \\033[10C:")
    print("Inicio: [1234567890] Aquí se moverá el cursor.")
    print("\033[10C", end="")  # Mueve 10 columnas a la derecha
    print("^ Aquí está después de mover 10 columnas.")
    time.sleep(2)

def ejemplo_20D():
    print("\033[20D", end="")  # Mueve 20 columnas a la izquierda
    print("Ahora el cursor está 20 columnas a la izquierda.")
    time.sleep(2)

def ejemplo_30G():
    print("\033[30G", end="")  # Mueve el cursor a la columna 30 de la fila actual
    print("^ El cursor está en la columna 30.")
    time.sleep(2)

def ejemplo_1F():
    print("Moviendo una línea arriba, se imprimiran dos y la segunda se sustituira:")
    print("Primera linea")
    print("Sefunda linea")
    time.sleep(1)
    print("\033[1F", end="")  # Mueve el cursor una línea arriba
    print("^ El cursor se movió una línea hacia arriba.")
    time.sleep(2)

def ejemplo_K():
    print("Esta es una línea larga donde se borrará parte del texto.")
    print("Aquí se eliminará todo a la derecha del cursor.")
    time.sleep(1)
    print("\033[K", end="")  # Borra todo desde la posición del cursor hasta el final de la línea
    print("^^ La línea fue borrada desde el cursor hacia la derecha.")
    time.sleep(2)

def ejemplo_20_40H():
    print("Este es el ejemplo de \\033[20;40H:")
    print("Antes de mover el cursor.")
    time.sleep(1)
    print("\033[20;40H", end="")  # Mueve el cursor a la fila 5, columna 40
    print("^ El cursor ahora está en la fila 20, columna 40.")
    time.sleep(2)

def main():
    """Ejecuta todos los ejemplos uno tras otro."""
    ejemplo_10C()
    ejemplo_20D()
    ejemplo_30G()
    ejemplo_1F()
    ejemplo_K()
    ejemplo_20_40H()
    print("Fin de los ejemplos.")

# Ejecutar el programa
main()
