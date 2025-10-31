#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos las nuevas frutas asignando el valor a la nueva clave
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Verificamos el resultado
print(precios_frutas)




#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000,
'Uva': 1450, 'Naranja':1200, 'Manzana': 1500, 'Pera': 2300}

# Añadimos nuevos valores a las furtas

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)




#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas 
# sin los precios.

# Diccionario actualizado
precios_frutas = {'Banana': 1330,'Ananá': 2500,'Melón': 2800,'Uva': 1450,
'Naranja': 1200,'Manzana': 1700,'Pera': 2300}

# Crear lista solo con los nombres de las frutas
precios_frutas = list(precios_frutas)

# Mostrar la lista
print("Lista de frutas:")
print(precios_frutas)




#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

# Cargar contactos
contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto #{i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

# Consultar contacto
consulta = input("\nIngrese el nombre a consultar: ")
if consulta in contactos:
    print(f"{consulta} → muestra \"{contactos[consulta]}\"")
else:
    print("Contacto no encontrado.")




#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicitar frase al usuario
frase = input("Ingrese una frase: ")

# Separar palabras
palabras = frase.split()

# Obtener palabras únicas
palabras_unicas = set(palabras)

# Contar ocurrencias
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")





#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# Crear diccionario de alumnos
alumnos = {}

# Cargar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno n°{i+1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Mostrar promedio de cada alumno
print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Alumno {nombre}: su promedio es: {promedio:.2f}")





#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron
# Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "María", "Jorge"}
parcial2 = {"Luis", "María", "Sofía", "Pedro"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobó al menos un parcial:", al_menos_uno)





#8) Armá un diccionario donde las claves sean nombres de productos y los 
#valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.


# Diccionario de productos y stock
stock_productos = {
    "Arroz": 50,
    "Fideos": 30,
    "Aceite": 20
}

# Mostrar productos disponibles
print("Productos actuales:")
for producto, cantidad in stock_productos.items():
    print(f"{producto}: {cantidad} unidades")

# Consultar producto
nombre = input("\n🔍 Ingrese el nombre del producto a consultar o actualizar: ").strip()

if nombre in stock_productos:
    print(f"{nombre} tiene {stock_productos[nombre]} unidades en stock.")
    try:
        agregar = int(input(f"¿Cuántas unidades desea agregar a {nombre}? "))
        stock_productos[nombre] += agregar
        print(f"Stock actualizado: {nombre} → {stock_productos[nombre]} unidades.")
    except ValueError:
        print("Ingrese un número válido.")
else:
    try:
        nuevo_stock = int(input(f"{nombre} no existe. ¿Cuántas unidades desea agregar como nuevo producto? "))
        stock_productos[nombre] = nuevo_stock
        print(f"Producto agregado: {nombre} → {nuevo_stock} unidades.")
    except ValueError:
        print("Ingrese un número válido.")





#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.


# Agenda con eventos programados
agenda = {
    ("lunes", "07:00"): "Reunión de jefes",
    ("martes", "14:00"): "Controlar stock",
    ("miércoles", "09:30"): "Llamada con cliente",
    ("jueves", "14:00"): "Capacitación interna",
    ("viernes", "11:00"): "Revisión de proyecto"
}
# Consulta de actividad
dia = input("Ingrese el día (ej: lunes): ").strip().lower()
hora = input("Ingrese la hora (ej: 10:00): ").strip()

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada para el {dia} a las {hora} Hs : {agenda[clave]}")
else:
    print("No hay actividad programada en ese horario.")





#10) Dado un diccionario que mapea nombres de países con sus capitales, construí 
#un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
    
# Diccionario original: país → capital
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Invertir el diccionario: capital → país
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

# Mostrar resultado
print("Diccionario invertido (capital → país):")
print(capitales)


