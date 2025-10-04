#1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# Lista con las notas de 10 estudiantes
notas = [7, 8, 6, 9, 5, 10, 4, 8, 7, 6]

# Mostrar la lista completa
print("Notas de los estudiantes:", notas)

# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print("Promedio de notas:", (promedio))

# Indicar la nota más alta y la más baja
nota_maxima = max(notas)
nota_minima = min(notas)
print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)



#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.


productos = []

# Pedir al usuario que cargue 5 productos
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente usando sorted()
productos_ordenados = sorted(productos)
print("Lista de productos ordenada alfabéticamente:")
print(productos_ordenados)

# Preguntar qué producto desea eliminar
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")

# Verificar si el producto está en la lista y eliminarlo
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"Producto '{producto_a_eliminar}' eliminado correctamente.")
else:
    print(F"El producto '{producto_a_eliminar}' no se encuentra en la lista.")

# Mostrar la lista actualizada
print("Lista actualizada de productos: ")
print(productos)


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista

import random

# Generar una lista con 15 números enteros al azar entre 1 y 100
numeros = [random.randint(1, 100) 
for _ in range(15)]
print("Lista original de números:", numeros)

# Crear listas de pares e impares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# Mostrar cuántos números tiene cada lista
print("Números pares:", pares)
print("Cantidad de pares:", len(pares))

print("Números impares:", impares)
print("Cantidad de impares:", len(impares))


#4) Dada una lista con valores repetidos: 
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3] 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado.

# Lista original con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Crear una nueva lista sin elementos repetidos usando set
datos_sin_repetidos = list(set(datos))

# Mostrar el resultado
print("Lista sin elementos repetidos:", datos_sin_repetidos)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.


# Lista inicial con 8 estudiantes
estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Facundo", "Gabriela", "Hugo"]

# Mostrar la lista original
print("Estudiantes presentes en clase:")
print(estudiantes)

# Bucle para modificar la lista
while True:
    print("Opciones: agregar / eliminar/ salir")
    accion = input("¿Qué querés hacer?: ").strip().lower()

    if accion == "agregar":
        nuevo = input("Ingresá el nombre del nuevo estudiante: ").strip()
        estudiantes.append(nuevo)
        print(f"Estudiante '{nuevo}' agregado correctamente.")
        # Mostrar la lista actualizada
        print("Lista final de estudiantes presentes:")
        print(estudiantes)
    elif accion == "eliminar":
        eliminar = input("Ingresá el nombre del estudiante que querés eliminar: ").strip()
        if eliminar in estudiantes:
            estudiantes.remove(eliminar)
            print(f"Estudiante '{eliminar}' eliminado correctamente.")
        else:
            print(f"El estudiante '{eliminar}' no se encuentra en la lista.")
        # Mostrar la lista actualizada
        print("Lista final de estudiantes presentes:")
        print(estudiantes)
    elif accion == "salir":
        break
    else:
        print("Opción no válida. Por favor escribí 'agregar', 'eliminar' o 'salir'.")
    

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia
# la derecha (el último pasa a ser el primero).
        
# Lista original con 7 números
numeros = [10, 20, 30, 40, 50, 60, 70]

# Rotar la lista una posición hacia la derecha
rotada = [numeros[-1]] + numeros[:-1]

# Mostrar el resultado
print("Lista original:", numeros)
print("Lista rotada:", rotada)


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas 
#mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.


# Matriz 7x2 con temperaturas mínimas y máximas de una semana
# Formato: [min, max] por día
temperaturas = [
    [12, 22],  # Día 1
    [14, 25],  # Día 2
    [10, 20],  # Día 3
    [13, 27],  # Día 4
    [11, 21],  # Día 5
    [15, 30],  # Día 6
    [9, 18]    # Día 7
]

# Calcular promedios
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print(f"Promedio de temperaturas mínimas: {int(promedio_min)}°C")
print(f"Promedio de temperaturas máximas: {int(promedio_max)}°C")

# Calcular amplitudes térmicas y encontrar la mayor
amplitudes = [dia[1] - dia[0] for dia in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1  # Día 1 a 7

print(f"La mayor temperatura registrada fue de {mayor_amplitud}°C y ocurrió el día {dia_mayor_amplitud}.")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

# Matriz de 5x3: cada fila representa un estudiante, cada columna una materia
notas = [
    [7, 8, 9],   # Estudiante 1
    [6, 7, 8],   # Estudiante 2
    [9, 8, 10],  # Estudiante 3
    [5, 6, 7],   # Estudiante 4
    [8, 9, 9]    # Estudiante 5
]

# Mostrar promedio de cada estudiante
print("Promedio por estudiante:")
for i, fila in enumerate(notas):
    promedio_est = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {round(promedio_est, 2)}")

# Mostrar promedio de cada materia
print("Promedio por materia:")
for j in range(3):
    suma_materia = sum(notas[i][j] for i in range(5))
    promedio_mat = suma_materia / 5
    print(f"Materia {j+1}: {round(promedio_mat, 2)}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada
    
# Inicializar el tablero 3x3 con guiones
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

# Mostrar el tablero inicial
print("Tablero inicial:")
mostrar_tablero()

# Turnos alternados entre dos jugadores
for turno in range(9):  # Máximo 9 jugadas
    jugador = "x" if turno % 2 == 0 else "0"
    print(f"Turno del jugador {jugador}")

    # Pedir posición al jugador
    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada. Perdés el turno.")
        continue
    # Mostrar el tablero actualizado
    mostrar_tablero()


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
    
# Matriz de ventas: 4 productos x 7 días
# Cada fila representa un producto, cada columna un día
ventas = [
    [10, 12, 9, 14, 11, 13, 15],   # Producto 1
    [8, 9, 10, 7, 12, 11, 9],      # Producto 2
    [15, 14, 13, 16, 15, 14, 17],  # Producto 3
    [5, 6, 7, 8, 6, 7, 9]          # Producto 4
]

# Total vendido por cada producto
print("Total vendido por cada producto:")
totales_productos = []
for i, fila in enumerate(ventas):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {i+1}: {total} unidades")

# Día con mayores ventas totales
print("Ventas totales por día:")
totales_dias = []
for j in range(7):
    total_dia = sum(ventas[i][j] for i in range(4))
    totales_dias.append(total_dia)
    print(f"Día {j+1}: {total_dia} unidades")

dia_max_ventas = totales_dias.index(max(totales_dias)) + 1
print(f"El día con mayores ventas totales fue el día {dia_max_ventas}.")