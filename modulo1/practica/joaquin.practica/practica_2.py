# Crear un menu iterativo en python con las siguientes opciones 
# opcion 1 'Saludar' , pedir datos personales
# opcion 2 Realizar una operacion matematica pedir 2 numeros 
# opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). 
# Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
# opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
# opcion 5 mostrar listado de alumnos aprobados 
# opcion 6 mostrar listado de alumnos desaprobados
# opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista 
# los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
# opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
# opcion 9 Salir. 
# Generar una secuencia de números del 0 al 9 con un paso de 2


def saludar():
    print("¡Hola! Por favor, ingresa tus datos personales.")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")
    print(nombre,"\n",edad,"\n",correo)

def operacion_matematica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2  
    print(f"El resultado de la operación es: {resultado}")

alumnos = []

def agregar_a_lista():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")
    cursos = []
    while True:
        curso_nombre = input("Introduzca el nombre de curso (o 'fin' para terminar): ")
        if curso_nombre.lower() == 'fin':
            break
        notas = input("Notas del curso (separadas por coma): ").split(',')
        curso = {'nombre_curso': curso_nombre, 'notas': [float(nota) for nota in notas]}
        cursos.append(curso)
    alumno = {'nombre': nombre, 'edad': edad, 'correo': correo, 'cursos': cursos}
    alumnos.append(alumno)
    
promedio_notas = []
def calcular_promedio():
    while True:
        nom= input("Introduzca nombre de curso (o 'fin' para teminar): ")
        if nom.lower() == "fin":
            break
        nta = input("notas del curso (separadas por coma): ").split(",")
        datos = [{"nombre_cur": nom, "notas": [float(i) for i in nta]}]
        for i in datos:
            nom_cur = i["nombre_cur"]
            not_cur = i["notas"]
            promedio = sum(not_cur)/len(not_cur)
            print(f"El promedio del curso {nom_cur} es de {promedio}")
            promedio_notas.append({"nombre_del_curso": nom_cur, "notas_promedio": promedio})
    
############## SUPONIENDO QUE EXISTE UNA LSITA DE ALUMNOS Y SUS NOTAS:
alumnos = [
    {'alumno_nombre': 'Juan', 'promedio_nt': 16},
    {'alumno_nombre': 'María', 'promedio_nt': 11},
    {'alumno_nombre': 'Pedro', 'promedio_nt': 15},
    {'alumno_nombre': 'joaquin', 'promedio_nt': 20},
    {'alumno_nombre': 'Raquel', 'promedio_nt': 13},
    {'alumno_nombre': 'Ricardo', 'promedio_nt': 12},
    {'alumno_nombre': 'Martin', 'promedio_nt': 15},
    ]
##############################################################


def generar_rango():
    print("AUN NO SE COMO HACER ESTO :c")

def obtener_mayor():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    mayor = max(num1, num2)
    print("El número mayor es:", mayor)

def secuencia():
    for i in range(0, 9, 2):
        print(i)

while True:
    print("\nMenú:")
    print("1. Introducir mis datos personal")
    print("2. Realizar operación matemática (SUMA)")
    print("3. Agregar a lista un diccionario con datos de cursos")
    print("4. Calcular promedio de notas y agregar a lista")
    print("5. Mostrar listado de alumnos aprobados")
    print("6. Mostrar listado de alumnos desaprobados")
    print("7. Generar lista de números según condiciones")
    print("8. Obtener el mayor de 2 números")
    print("9. Salir")
    print("10. secuencia de número del 0 al 9 con un paso de 2")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        saludar()
    elif opcion == '2':
        operacion_matematica()
    elif opcion == '3':
        agregar_a_lista()
    elif opcion == '4':
        calcular_promedio()
    elif opcion == '5':
        def mostrar_aprobados(promedio):
            return promedio >= 14
        aprobados = [i for i in alumnos if mostrar_aprobados(i['promedio_nt'])]
        print("Alumnos Aprobados:")
        for v in aprobados:
             print(f"{v['alumno_nombre']} - Promedio: {v['promedio_nt']}") 
    elif opcion == '6':
        def mostrar_desaprobados(promedio):
            return promedio <= 13
        desaprobados = [i for i in alumnos if mostrar_desaprobados(i['promedio_nt'])]
        print("Alumnos Desaprobados:")
        for v in desaprobados:
            print(f"{v['alumno_nombre']} - Promedio: {v['promedio_nt']}") 
    elif opcion == '7':
        generar_rango()
    elif opcion == '8':
        obtener_mayor()
    elif opcion == '9':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    elif opcion == "10":
        secuencia()
    else:
        print(input("Número incorrecto, vuelva a escribir el número de su elección: "))