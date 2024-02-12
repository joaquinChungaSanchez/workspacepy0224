# 1.Realizar un programa que pida tus datos personales y mostrar en pantalla los datos solisitados
print("DATOS PERSONALES")
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
mes_de_nacimiento=input("Ingrese su mes de nacimiento: ")
print("Su normbre es {}, tiene {} años y nacio el mes de {}".format(nombre,edad,mes_de_nacimiento))

# 2.Realizar un programa que calcule el area y el perimetro de un poligono a tu eleccion( triangulo , cuadrado , circulo)
## AREA DEL CICULO

print("AREA DEL CIRCULO")
import math
PI=math.pi
radio=float(input("Ingrese el radio del ciculo: "))
area_del_cirulo=PI*math.pow(radio,2)
print("El area del circulo es de {}".format(area_del_cirulo))

## PERÍMETRO DEL TRIANGULO

print("PERIMETRO DEL TRIANGULO")
base=float(input("Ingrese la base del triangulo: "))
lado1=float(input("Ingrese la medida de uno de los lados del triangulo: "))
lado2=float(input("Ingrese la medida del otro lado del triangulo: "))
perimetro=base+lado1+lado2
print("El perimetro del triangulo es de {}".format(perimetro))

# 3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos . 
# Como resultado debe decir  todos los egresos y el ahorro.

print("EGRESOS Y AHORRO DEL HOGAR")
IngresoTOTAL=float(input("Coloque el ingreso total del hogar: "))
consumo=float(input("Colque el total de sus gastos en consumo de alimentos: "))
pagos=float(input("Coloque el total de pagos de servicios: "))
consumo1=float(input("Coloque el total de sus gastos en necesidades secundarias: "))
EgresoTOTAL=consumo+pagos+consumo1
AhorroTOTAL=IngresoTOTAL-EgresoTOTAL
print("El egreso total del hogar es de {} y su total de ahorro es de {}".format(EgresoTOTAL,AhorroTOTAL))

# 4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: mayor de edad , 
# tener ruc y tener un nombre comercial ,los inputs son si y /o no . la salida debe ser si esta apto o no para abrir un comercio.

print("¿APTO PARA REGISTRAR UN NEGOCIO?")
mayor_de_edad=input("¿Es mayor de edad? (si/no): ")
ruc=input("¿Tienes RUC? (si/no): ")
nombre_comercial=input("¿Tienes un nombre comercial? (si/no): ")
if mayor_de_edad=="si" and ruc=="si" and nombre_comercial=="si":
    print("Usted es apto para aperturar un negocio")
else:
    print("Usted no cumple con las condiciones requeridas para aperturar un negocio")