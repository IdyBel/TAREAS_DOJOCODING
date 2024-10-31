diccionario_vacio = {}

persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}

persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente

persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente

print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor

print(altura)    # Imprime: 1.71

print(persona)

print(type(3.1416))