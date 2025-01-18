import json

# El archivo donde se guardan los datos
users_file = 'preguntas.json'

# Cargar los datos del archivo JSON
def load_users():
    with open(users_file, 'r') as f:
        return json.load(f)

# Cargar los usuarios desde el archivo JSON
usuarios = load_users()

# Acceder a los datos de un "id"
id_usuario = "id2"  # Puedes cambiar esto a cualquier id como 'id1', 'id3', etc.
usuario = usuarios.get(id_usuario)

if usuario:
    frase = usuario['frase']
    pista = usuario['pista']
    print(f"Frase: {frase}")
    print(f"Pista: {pista}")
else:
    print("Usuario no encontrado")
