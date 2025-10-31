#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
 
print("Hola mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.    

nombre = input("Ingrese su nombre: ")
print( "Hola" , nombre ,"!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima 
#por pantalla su área y su perímetro. 

radio = float(input("Ingrese el radio de un circulo: "))

area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio

print("Su area es: ", area )
print("Su perimetro es: ", perimetro )


#5) Crear un programa que pida al usuario una cantidad de segundos e 
# imprima por pantalla a cuántas horas equivale. 

segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos / 3600

print("Equivale a :" , horas , "horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la
# tabla de multiplicar de dicho número. 

numero = int(input("Ingresar un numero : "))

print( numero * 1)
print( numero * 3) 
print( numero * 4)
print( numero * 5)
print( numero * 6)
print( numero * 7)
print( numero * 8)
print( numero * 9)
print( numero * 10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

numero1 = int(input("ingresar primer numero entero: "))
numero2 = int(input("ingresar segundo numero entero: "))

print(f"El resultado de sumarlo es: {numero1 + numero2} ")
print(f"El resultado de dividirlos es: {numero1 / numero2} ")
print(f"El resultado de multiplicarlos es: {numero1 * numero2} ")
print(f"El resultado de restarlos es: {numero1 - numero2} ")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. 

peso = float(input("Introduce tu peso en kilogramos (kg): "))
altura = float(input("Introduce tu altura en metros (m): "))

imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal es: {imc}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius 
# e imprima por pantalla su equivalente en grados Fahrenheit. 

Temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

Temperarura_fahrhenint = 9/5 * Temperatura_celsius + 32

print(f"Su equivalente en grados fahrenheint es: {Temperarura_fahrhenint}")


#10) Crear un programa que pida al usuario  3 números e imprima por pantalla 
 # el promedio de dichos números.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero:"))
num3 = float(input("Ingrese el tercer numero:"))

promedio = (num1 + num2 + num3) / 3

print(f"El pormedio de los tres numeros dados es: {promedio}")