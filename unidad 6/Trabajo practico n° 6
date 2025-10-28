#1- Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Definición de la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada desde el programa principal
if __name__ == "__main__":
    imprimir_hola_mundo()

#2 - Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), 
#deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.
    
def saludar_usuario(nombre):
  """
  Recibe un nombre como parámetro y devuelve un saludo personalizado.
  """
  return f"¡Hola {nombre}!"

# --- Programa Principal ---

# 1. Solicitar el nombre al usuario
nombre_usuario = input("Por favor, introduce tu nombre: ")

# 2. Llamar a la función con el nombre ingresado
saludo_personalizado = saludar_usuario(nombre_usuario)

# 3. Imprimir el saludo devuelto por la función
print(saludo_personalizado)

#3- Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
  """
  Recibe cuatro parámetros (nombre, apellido, edad, residencia)
  e imprime una frase formateada con esos datos.
  """
  # Esta función imprime directamente el resultado, no devuelve nada (return)
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 1. Solicitar los cuatro datos al usuario
print("--- Completa tu información personal: ---")
nombre_usuario = input("Introduce tu nombre: ")
apellido_usuario = input("Introduce tu apellido: ")
edad_usuario = input("Introduce tu edad: ")
residencia_usuario = input("Introduce dónde vives: ")

# 2. Llamar a la función
# Le pasamos las variables que capturamos del usuario como argumentos
print("\n--- Información personal: ---")
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)


#4 - Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el 
# radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
   
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
   
    return 2 * math.pi * radio

# Programa principal
if __name__ == "__main__":

 radio = float(input("Ingrese el radio del círculo: "))
 area = calcular_area_circulo(radio)
 perimetro = calcular_perimetro_circulo(radio)

print(f"\n Resultados para un círculo de radio {radio}:")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


#5- Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y
# mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
  
  # Hay 3600 segundos en una hora (60 seg/min * 60 min/hora)
  horas = segundos / 3600
  return horas

#Programa Principal 

# 1. Solicitar los segundos al usuario
try:
  segundos_usuario = int(input("Por favor, introduce la cantidad de segundos: "))

  # 2. Llamar a la función con el valor ingresado
  horas_resultado = segundos_a_horas(segundos_usuario)

  # 3. Imprimir el resultado
  # Usamos :.4f para mostrar el resultado con 4 decimales para mayor precisión
  print(f"{segundos_usuario} segundos equivalen a {horas_resultado:.4f} horas.")

except ValueError:
  print("Error: El valor introducido no es un número entero válido.")


#6- Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    
    print(f"\n Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
if __name__ == "__main__":
    try:
        entrada = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        tabla_multiplicar(entrada)
    except ValueError:
        print(" Por favor, ingrese un número entero válido.")



#7 -Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


def operaciones_basicas(a, b):
    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None  # Evita división por cero
    return (suma, resta, multiplicacion, division)

# Programa principal
if __name__ == "__main__":
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultados = operaciones_basicas(a, b)

        print(f"\n Resultados de las operaciones entre {a} y {b}:")
        print(f"Suma: {resultados[0]:.2f}")
        print(f"Resta: {resultados[1]:.2f}")
        print(f"Multiplicación: {resultados[2]:.2f}")
        if resultados[3] is not None:
            print(f"División: {resultados[3]:.2f}")
        else:
            print("División: No se puede dividir por cero.")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")



#8- Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función.
        
def calcular_imc(peso, altura):
    
    return peso / (altura ** 2)

# Programa principal
if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        imc = calcular_imc(peso, altura)
        print(f"\n Su índice de masa corporal (IMC) es: {imc:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
    except ZeroDivisionError:
        print("La altura no puede ser cero.")



#9- Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
        

def celsius_a_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

# Programa principal
if __name__ == "__main__":
    try:
        temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
        print(f"\n Equivalente en Fahrenheit: {temp_fahrenheit:.2f} °F")
    except ValueError:
        print(" Por favor, ingrese un valor numérico válido.")




#10- Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.
        
def calcular_promedio(a, b, c):
   
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
        promedio = calcular_promedio(a, b, c)
        print(f"\n El promedio de los tres números es: {promedio:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")