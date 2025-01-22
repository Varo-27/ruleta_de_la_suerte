import ctypes
import subprocess

# Función para establecer el modo de pantalla completa
def pantalla_completa():
    # Obtener el manejador de la ventana de la consola
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    SW_MAXIMIZE = 3

    h_wnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(h_wnd, SW_MAXIMIZE)

# Ejecutar la función para establecer el modo de pantalla completa

# El resto de tu código aquí
print("Hola, mundo!")
pantalla_completa()

while True:
    pass
