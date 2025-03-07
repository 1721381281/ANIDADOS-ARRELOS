import numpy as np

# Definimos las ciudades, días de la semana y semanas
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Creamos una matriz 3D de temperaturas aleatorias (3 ciudades, 7 días, 4 semanas)
# Las temperaturas estarán entre 15 y 30 grados
temperaturas = np.random.randint(15, 31, size=(len(ciudades), len(dias), semanas))

# Inicializamos un diccionario para almacenar los promedios
promedios = {ciudad: [] for ciudad in ciudades}

# Calculamos el promedio de temperaturas para cada ciudad y cada semana
for i in range(len(ciudades)):
    for j in range(semanas):
        suma_temperaturas = 0
        for k in range(len(dias)):
            suma_temperaturas += temperaturas[i][k][j]
        promedio = suma_temperaturas / len(dias)
        promedios[ciudades[i]].append(promedio)

# Mostramos los resultados
for ciudad, promedio in promedios.items():
    for semana, temp_promedio in enumerate(promedio):
        print(f"Promedio de temperaturas en {ciudad} - Semana {semana + 1}: {temp_promedio:.2f} °C")
        
        
    




#coemntaario