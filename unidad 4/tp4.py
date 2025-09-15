#Trabajo Práctico n3: Bucles

#En este trabajo intento en lo posible no usar la funcion break ya que se considera una mala práctica


#punto 1
for i in range (0,101):
    print(i)

#punto 2
opcion="si"
while opcion.lower()=="si":
    numero=input("Ingrese un número: ")
    digitos=len(str(abs(int(numero))))
    print(f"La cantidad de dígitos que tiene el número es: {digitos}")
    print("//Seleccione la opción deseada//")
    opcion=input("SI) Ingresar otro número.\nNO) Finalizar. : ")

#punto 3
opcion="si"
suma=int(0)
while opcion.lower()=="si":
    rango=input("Ingrese un rango numérico con el formato (10-20): ")
    #Procedo a separar el inicio y el final del rango numérico ingresados por el usuario
    auxiliar=rango.split("-")
    inicio_rango=int(auxiliar[0])
    fin_rango=int(auxiliar[1])
    for i in range (inicio_rango+1, fin_rango):
        suma=suma+i
    print(f"la suma de todos los números comprendidos entre {inicio_rango} y {fin_rango } es: {suma}")
    print("//Seleccione la opción deseada//")
    opcion=input("SI) Ingresar más números.\nNO) Finalizar. : ")
    suma=int(0)

#punto 4
opcion="1"
suma=int(0)
while opcion=="1":
    numero=int(input("ingrese un número para sumar: "))
    suma=suma+numero
    print("//Ingrese la opción deseada//")
    opcion=input("1)Ingresar otro número.\n0)Finalizar y mostrar el resultado. ")
    if opcion=="0":
        print(f"El resultado de la suma de todos los números ingresados es: {suma}")
        break
    else:
        continue

#punto 5
import random 
contador=int(0)
numero=int(0)
numero_aleatorio=random.randint(1,10)
while numero!=numero_aleatorio:
    numero=int(input("Ingrese un número entre 1 y 10: "))
    contador=contador+1

print(f"Adivinaste! El número era: {numero_aleatorio}\nutilizaste {contador} intentos")

#punto 6 
for i in range (100,0,-1):
    if i%2==0:
        print(i)

#punto 7
numero=int(input("ingrese un número: "))
suma=0
for i in range (0,numero+1):
    suma=suma+i

print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")

#punto 8
positivo=int(0)
negativo=int(0)
par=int(0)
impar=int(0)
for i in range (1,101):
    numero=int(input("Ingrese 100 números: "))
    if numero<0:
        negativo=negativo+1
    else:
        positivo=positivo+1
    
    if numero%2==0:
        par=par+1
    else:
        impar=impar+1

print(f"De los números ingresados hay:\n{par} números pares\n{impar} números impares\n{positivo} números positivos\n{negativo} números negativos")

#punto 9
from statistics import mean
cantidad_numeros=100
numeros=[]
for i in range(cantidad_numeros):
    numero=int(input("Ingrese un número: "))
    #La función .append() la saqué de chat gpt ya que no sabía como agregar los números ingresados a la lista
    numeros.append(numero)
media=mean(numeros)
print(f"La media de los números ingresados es: {media}")

#punto 10
opcion="si"
while opcion.lower()=="si":
    numero=input("Ingresa un número para darlo vuelta: ")
    #Esta función (numero[::-1]) tambien la saqué de chat gpt, lo que hace es dividir los dígitos del número e ingresarlos de atrás hacia adelante para eso el (-1)
    numero_invertido=numero[::-1]
    print(f"El número {numero} invertido es: {numero_invertido}")
    print("//Seleccione la opcion deseada//")
    opcion=input("SI)Ingresar otro número.\nNO)Finalizar el programa. ")