#Trabajo práctico n3: condicionales 

#punto 1:
edad=int(input("ingrese su edad: "))
if edad > 18:
    print("es mayor de edad")

#punto 2:
nota=float(input("ingrese su nota: "))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")

#punto 3:
numero=int(input("ingrese un número: "))
if numero % 2 ==0:
    print("ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#punto 4:
edad=int(input("ingrese su edad: "))
if edad>=0 and edad<12:
    print("Niño/a")
elif edad>=12 and edad<18:
    print("adolescente")
elif edad>=18 and edad<30:
    print("adulto/a joven")
else: 
    print("adulto/a")

#punto 5:
contraseña=input("ingrese una contraseña: ")
if len(contraseña) >=8 and len(contraseña) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#punto6
import random 
numeros_aleatorios=[random.randint(1,100) for _ in range(50)]
from statistics import mode, median, mean
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
print(f"moda: {moda}")
print(f"mediana: {mediana}")
print(f"media: {media}")
if media>mediana>moda:
    print("Sesgo positivo a la derecha")
elif media<mediana<moda:
    print("Sesgo negativo a la izquierda")
elif media==mediana==moda:
    print("sin sesgo")

#punto 7:
frase=input("ingrese una palabra o frase: ")
if frase[-1].lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)

#punto 8:
nombre=input("ingrese su nombre: ")
print("1) Nombre en mayúsculas")
print("2) Nombre en minúsculas")
print("3) Letra inicial en mayúscula")
opcion=input("Seleccione una opcion: ")
if opcion == "1":
    nombre=nombre.upper()
    print(f"{nombre}")
elif opcion=="2":
    nombre=nombre.lower()
    print(f"{nombre}")
else:
    nombre=nombre.title()
    print(f"{nombre}")

#punto 9:
magnitud=float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (Imperceptible)")
elif magnitud>=3 and magnitud<4:
    print("Leve (Ligeramente perceptible)")
elif magnitud>=4 and magnitud<5:
    print("Moderado(Sentido por personas, pero generalmente no causa daños)")
elif magnitud>=5 and magnitud<6:
    print("Fuerte (Puede causar daños en estructuras débiles)")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte (Puede causar daños significativos)")
elif magnitud>=7:
    print("Extremo (Puede causar grandes daños a gran escala)")

#punto 10:
hemisferio=input("Ingrese en que hemisferio se encuentra (Norte/Sur): ")
mes=int(input("ingrese el mes actual (número): "))
dia=int(input("ingrese el día actual (número): "))
if hemisferio.lower()=="norte":
    if (mes==12 and dia>=21) or mes==1 or mes==2 or (mes==3 and dia<=20):
        print("Se encuentra en invierno")
    elif (mes==3 and dia>=21) or mes==4 or mes==5 or (mes==6 and dia<=20):
        print("Se encuentra en primavera")
    elif (mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<=20):
        print("Se encuentra en verano")
    elif (mes==9 and dia>=21) or mes==10 or mes==11 or (mes==12 and dia<=20):
        print("Se encuentra en otoño")
elif hemisferio.lower()=="sur":
    if (mes==12 and dia>=21) or mes==1 or mes==2 or (mes==3 and dia<=20):
        print("Se encuentra en verano")
    elif (mes==3 and dia>=21) or mes==4 or mes==5 or (mes==6 and dia<=20):
        print("se encuentra en otoño")
    elif (mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<=20):
        print("Se encuentra en invierno")
    elif (mes==9 and dia>=21) or mes==10 or mes==11 or (mes==12 and dia<=20):
        print("Se encuentra en primavera")

