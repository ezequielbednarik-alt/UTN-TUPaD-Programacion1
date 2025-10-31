#1) Escribir un programa que solicite la edad del usuario. 
#Si el usuario es mayor de 18 años,deberá mostrar un mensaje 
#en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. 
#Si la nota es mayor o igual a 6, deberá mostrar por pantalla un 
#mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Por favor, ingrese su nota: " ))
if nota >= 6:
    print("Aprobado")
elif nota < 6:
    print("desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Por favor, ingrese un num par: "))
if num % 2 == 0:
    print("Ha ingresado un número par: ")
else:
    print("Por favor, ingrese un numero par: ")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
    
num = int(input("Por favor, ingrese su edad: "))
if num < 12:
    print("Nino/a")
elif num >= 12 and num < 18:
    print("Adolescente")
elif num >= 18 and num < 30:
    print("Adulto/a joven")
elif num >= 30:
    print("Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contrasena = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")

longuitud = len(contrasena)

if longuitud >= 8 and longuitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
    
import random

numeros_aleatorios = [ random.randint(1, 100) for i in range(50)]

import statistics

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo significativo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Por favor, ingrese una frase o palabra: ") 
vocales = "a, e, i ,o, u, A, E, I, O, U"

if frase [-1] in vocales:
    frase_cambiada = frase + "!"
    print(frase_cambiada)
else:
    print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
    
nombre = input("Por favor, ingrese su nobre: ")
print("Que opcion desea la opcion deseada realizar:")
print(" 1. Si quiere su nombre en mayúsculas ")
print(" 2. Si quiere su nombre en minúsculas ")
print(" 3. Si quiere su nombre con la primera letra mayúscula ")
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

if opcion == "1":
    nombre_modificado = nombre.upper()
    print(f"Su nombre en mayúsculas es: {nombre_modificado}")
elif opcion == "2":
    nombre_modificado = nombre.lower()
    print(f"Su nombre en minúsculas es: {nombre_modificado}")
elif opcion == "3":
    nombre_modificado = nombre.title()
    print(f"Su nombre en formato de título es: {nombre_modificado}")
else:
    print("Opción no válida.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Leve" (ligeramente perceptible)..
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("ingrese la magnitud de un terremoto del 1 al 10: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >=4 and magnitud < 5:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte(puede causar daños significativos")
elif magnitud >= 7 and magnitud < 10:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("numero fuera de escala")


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio_norte ={ 
    "verano": [("21-06", "20-09")],
    "otoño": [("21-09", "20-12")],
    "invierno": [("21-12", "20-03")],
    "primavera": [("21-03", "20-06")]}


hemisferio_sur ={
    "invierno": [("21-06", "20-09")],
    "primavera": [("21-09", "20-12")],
    "verano": [("21-12", "20-03")],
    "otoño": [("21-03", "20-06")]}

hemisferio = input("Por favor ingrese en que hemisferio se encuentra (ej:norte o sur):")
dia = int(input("Ingrese el numero de dia es:"))
mes = int(input("Ingrese el numero de mes es: "))


if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Fecha no válida. Por favor, ingresa un mes y día correctos.")
else: 
    fecha_usuario = f"{mes:02d}-{dia:02d}" 
    estaciones = {}


if hemisferio_norte == 'norte':
    print("hemisferio norte")
elif hemisferio_sur == 'sur':
    print ("hemisferio sur")        
else:
    print("Entrada de hemisferio no válida. Por favor, ingresa 'norte' o 'Sur'.")
