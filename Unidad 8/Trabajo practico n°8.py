#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad


# Crear y escribir en el archivo productos.txt
productos = [
    "Lapicera,120.50,10",
    "Cuaderno,350.00,5",
    "Mochila,2500.00,2"
]

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(producto + "\n")

print("Archivo productos.txt creado con éxito.")



#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea,
# la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Leer y mostrar productos desde productos.txt
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")



#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.


# Mostrar productos existentes
with open("productos.txt", "r") as archivo:
    print("Productos actuales:")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${float(precio)} | Cantidad: {int(cantidad)}")

# Solicitar nuevo producto
print("Agregar nuevo producto")
nuevo_nombre = input("Nombre del producto: ")
nuevo_precio = input("Precio: ")
nueva_cantidad = input("Cantidad: ")

# Validar y guardar
precio_float = float(nuevo_precio)
cantidad_int = int(nueva_cantidad)
nueva_linea = f"{nuevo_nombre},{precio_float},{cantidad_int}\n"

with open("productos.txt", "a") as archivo:
    archivo.write(nueva_linea)

print("Producto agregado correctamente.")



#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

# Cargar productos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar productos
print("Lista de productos:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")




#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, 
# mostrar un mensaje de error.

# Cargar productos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre.lower(),  # para búsqueda insensible a mayúsculas
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Buscar producto por nombre
buscado = input("Ingresá el nombre del producto a buscar: ").lower()
encontrado = False

for p in productos:
    if p["nombre"] == buscado:
        print(f"Producto encontrado:\nProducto: {p['nombre'].capitalize()} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado en el inventario.")




#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
#sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.


# Sobrescribir el archivo con los productos actualizados
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("Archivo productos.txt actualizado correctamente.")
