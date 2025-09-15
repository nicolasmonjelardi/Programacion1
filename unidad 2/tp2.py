#Trabajo Práctico n2: Secuenciales

#Ejercicio 1

print("Hola Mundo!")

#Ejercicio2

nombre=input("ingrese su nombre")
print (f"Hola {nombre}!")

#Ejercicio 3

nombre=input("ingrese su nombre")
apellido=input("ingrese su apellido")
edad=input("ingrese su edad")
residencia=input("ingrese su lugar de residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4

radio=float(input("ingrese el radio del círculo"))
print(f"el área del círculo es de: {(radio**2)*3.14}")
print(f"el perímetro del círculo es de: {(radio*2)*3.14}")

#Ejercicio 5

segundos=float(input("ingrese una cantidad de segundos"))
horas=float(segundos/3600)
print(f"{segundos} segundos, equivale a {horas} horas")

#Ejercicio 6

numero=float(input("ingrese un número"))
print(f"{numero} X 1 = {numero*1}")
print(f"{numero} X 2 = {numero*2}")
print(f"{numero} X 3 = {numero*3}")
print(f"{numero} X 4 = {numero*4}")
print(f"{numero} X 5 = {numero*5}")
print(f"{numero} X 6 = {numero*6}")
print(f"{numero} X 7 = {numero*7}")
print(f"{numero} X 8 = {numero*8}")
print(f"{numero} X 9 = {numero*9}")
print(f"{numero} X 10 = {numero*10}")

#Ejercicio 7

numero1=float(input("ingrese el primer número"))
numero2=float(input("ingrese el segundo número"))
print(f"{numero1} + {numero2} = {numero1+numero2}")
print(f"{numero1} - {numero2} = {numero1-numero2}")
print(f"{numero1} X {numero2} = {numero1*numero2}")
print(f"{numero1} : {numero2} = {numero1/numero2}")

#Ejercicio 8 

peso=float(input("ingrese su peso en kilogramos"))
altura=float(input("ingrese su altura en metros"))
print(f"su índice de masa corporal es igual a: {peso/altura**2}")

#Ejercicio 9

temperatura=float(input("ingrese una temperatura en grados celsius"))
print(f"{temperatura} grados celsius equivalen a {((9/5)*temperatura)+32} grados fahrenheit")

#Ejercicio 10

numero1=float(input("ingrese el primer número"))
numero2=float(input("ingrese el segundo número"))
numero3=float(input("ingrese el tercer número"))
print(f"el promedio entre {numero1}, {numero2} y {numero3} es: {(numero1+numero2+numero3)/3} ")