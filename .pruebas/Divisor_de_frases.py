# -*- coding: utf-8 -*-

import pyfiglet
import sys
from pathlib import Path

# Ruta relativa a la carpeta de fuentes personalizada
carpeta_fuentes = Path('Pruebas/my_fonts')

# Agregar la ruta de la carpeta de fuentes a sys.path
sys.path.append(str(carpeta_fuentes))

# Nombre de la fuente personalizada (sin extensión)
nombre_fuente = 'calvin_s'

# Crear un objeto Figlet con la fuente personalizada
figlet = pyfiglet.Figlet(font='standard')

# Generar texto grande
texto_grande = figlet.renderText(' é íúóO ñ ýúüU')

# Imprimir el texto grande
print(texto_grande)
