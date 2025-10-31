#1) Crea un programa que imprima en pantalla todos los números enteros 
# desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente,
# mostrando un número por línea.

for numero in range(0, 101):
 print(numero)
 
# 2) Desarrolla un programa que solicite al usuario un número entero 
# y determine la cantidad de dígitos que contiene.


numero = int(input("ingrese un numero entero: "))  

if numero == 0:
   numero_digitos = 1
else:
  numero_digitos = len(str(abs(numero)))  
print(f"El número tiene {numero_digitos} dígito(s)")


#3)Escribe un programa que sume todos los números enteros comprendidos
# entre dos valores dados por el usuario, excluyendo esos dos valores

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))


inicio = min(num1, num2)
fin = max(num1, num2)

suma_total = sum(range(inicio + 1, fin))

print(f"la suma de los números enteros entre {inicio} y {fin} es: {suma_total}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print("Ingrese números enteros para sumarlos. Ingrese 0 para terminar.")

# Inicializar acumulador
suma = 0

for _ in range(10000):  # Límite 
    numero = int(input("Número: "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total es: {suma}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
# Generar número aleatorio
numero_secreto = random.randint(0, 9)
intentos = 0

print("Adivina el número secreto entre 0 y 9.")

while numero_secreto :
    intento = int(input("Tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
        
# Imprimir números pares del 100 al 0 en orden descendente
print("Números pares entre 100 y 0 (decreciente):")

for numero in range(100, -1, -2):
    print(numero)        


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Solicitar número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Validar que sea positivo
if numero < 0:
    print("Error: Debe ingresar un número positivo.")
else:
    suma = 0
    for i in range(numero + 1):  # Incluye el número ingresado
        suma += i
    print(f"La suma de los números entre 0 y {numero} es: {suma}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Configurable: cantidad de números a ingresar
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad} números enteros:")

for i in range(1,cantidad + 1):
    try:
        numero = int(input(f"Número {i}: "))

        # Par o impar
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        # Positivo o negativo
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
        

# Resultados
print("----Resultados----")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).


# Configurable: cantidad de números a ingresar
CANTIDAD = 100 

# Inicializar suma
suma = 0

print(f"Ingrese {CANTIDAD} números enteros:")

for i in range(1, CANTIDAD + 1):
    try:
        numero = int(input(f"Número {i}: "))
        suma += numero
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
        continue

# Calcular media
media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} números ingresados es: {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número entero: ")

# Verificar que sea un número válido
if numero.isdigit():
    invertido = numero[::-1]  
    print(f"Número invertido: {invertido}")
else:
    print(" Error: Ingrese solo dígitos numéricos.")