#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos en el catálogo:")
            for producto in self.productos:
                print(f"{producto.nombre} - Precio: {producto.precio}")


producto_1 = Producto("Producto A", 50)
producto_2 = Producto("Producto B", 15.2)
producto_3 = Producto("Producto C", 100.6)

catalogo = Catalogo()

catalogo.agregar_producto(producto_1)
catalogo.agregar_producto(producto_2)
catalogo.agregar_producto(producto_3)

catalogo.mostrar_productos()

#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote

class prodcuto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    def __str__(self):
        separar = self.codigo.split("-")
        if len(separar) == 3:
            pais = separar[0]
            lote = separar[1]
            return f"País de orige: {pais} - Número de Lote: {lote}"
        else:
            print("coloque el formato del códgio correctamente")

producto_x = prodcuto("Producto H", "PERÚ-00256-2024")
print(producto_x)


#3. Del siguiente texto :
x = """
Lorem Ipsum is simply dummy text of the printing and types
etting industry. Lorem Ipsum has been the industry's standard
 dummy text ever since the 1500s, when an unknown printer took a 
 galley of type and scrambled it to make a type specimen book. 
 It has survived not only five centuries, but also the leap into electronic typesetting, 
 remaining essentially unchanged. It was popularised in the 1960s 
 with the release of Letraset sheets containing Lorem Ipsum passages, 
 and more recently with desktop publishing software like Aldus PageMaker 
 including versions of Lorem Ipsum.
"""
# realizar al menos 4 funciones de string 

mayusculas = x.upper()
print(mayusculas)

split = x.split()
print(split)

if len(split) < 50:
    print("El texto tiene menos de 50 palabras de 50 palabras"
)
else:
    print("El texto tiene más de 50 palabras")

contar = x.count("Lorem")
print(f"en el texto, la palabra Lorem se dice {contar} veces")

#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle
import funcion
while True:
    try:
        funcion.dividir()
        break
    except:
        print("coloque correctamente los números")
        continue
