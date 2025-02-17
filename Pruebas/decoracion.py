
import pyfiglet

# Listar todas las fuentes disponibles
fonts = pyfiglet.FigletFont.getFonts()
print("Fuentes disponibles:")
for font in fonts:
    figlet = pyfiglet.Figlet(font= font)
    texto_grande = figlet.renderText('pista')
    print(font)
    print(texto_grande)

while True:
    pass


# broadway_kb
# calvin_s
# thin


# cards