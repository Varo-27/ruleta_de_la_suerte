import json

# Diccionario original
data = {
    "varo": {"score": "1000", "date": "2025-01-01 12:00:00"},
    "juan": {"score": "950", "date": "2025-01-02 15:30:00"},
    "ana": {"score": "1100", "date": "2025-01-03 09:00:00"}
}

# Convertir scores a enteros para la ordenación
for key in data:
    data[key]["score"] = int(data[key]["score"])

# Ordenar los ítems sin modificar el diccionario original
items_ordenados = sorted(data.items(), key=lambda item: item[1]["score"], reverse=True)

# Recorrer los ítems ordenados
for key, value in items_ordenados:
    print(f"Nombre: {key}, Score: {value['score']}, Fecha: {value['date']}")
