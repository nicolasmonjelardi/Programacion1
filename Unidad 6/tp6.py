#Trabajo Práctico n6: Funciones

#Punto 1

#mostrar: Hola Mundo!
def imprimir_hola_mundo():
    
    print("Hola Mundo!")
    
imprimir_hola_mundo()

#Punto 2

#saludar al usuario
def saludar_usuario(nombre):
    
    print(f"Hola {nombre}!")

nombre=input("Ingresa tu nombre: ")

saludar_usuario(nombre)

#Punto 3

#mostrar información
def informacion_personal(nombre, apellido, edad, residencia):
    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre=input("Ingresa tu nombre: ")

apellido=input("Ingresa tu apellido: ")

edad=input("Ingresa tu edad: ")

residencia=input("Ingresa tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Punto 4

#calcular área del círculo
def calcular_area_circulo(radio):
    area=((radio ** 2) * 3.14)
    print(f"El área del círculo es de: {area}")

#calcular perímetro del círculo
def calcular_perimetro_circulo(radio):
    
    perimetro=((radio * 2) * 3.14)
    
    print(f"El perímetro del círculo es de {perimetro}")

radio=int(input("Ingresa el radio del círculo: "))

calcular_area_circulo(radio)

calcular_perimetro_circulo(radio)

#Punto 5

#pasar de segundos a horas
def segundos_a_horas(segundos):
    
    horas=((segundos/60)/60)
    
    print(f"{segundos} segundos, son {horas} horas")

segundos=int(input("Ingresa una cantidad de segundos: "))

segundos_a_horas(segundos)

#Punto 6

#imprimir tabla de multiplicar de un número (del 1 al 10)
def tabla_multiplicar(numero):
    
    for i in range(11):
        print(f"{numero} x {i} = {numero * i }")

numero=int(input("Ingresa un número: "))

tabla_multiplicar(numero)

#Punto 7

#operaciones básicas
def operaciones_basicas(a, b):
    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    
    tupla=(suma, resta, multiplicacion, division)
    
    print(tupla)

numero1=int(input("Ingresa el primer número: "))

numero2=int(input("Ingresa el segundo número: "))

operaciones_basicas(numero1, numero2)

#Punto 8

#calcular el índice de masa croporal
def calcular_imc(peso, altura):
    
    imc = (peso/(altura ** 2))
    
    print(f"Tu IMC es: {imc:.2f}")

peso=float(input("Ingresa tu peso en kgs: "))

altura=float(input("Ingresa tu altura en metros: "))

calcular_imc(peso, altura)

#Punto 9

#pasar de grados celsius a fahrenheit    
def celsius_a_fahrenheit(celsius):
    
    grados_fahrenheit = ((celsius * 1.8) + 32)

    print(f"{celsius} grados celcius equivalen a {grados_fahrenheit} grados fahrenheit")

celsius=int(input("Ingresa la temperatura actual en grados celsius: "))

celsius_a_fahrenheit(celsius)

#Punto 10

#calcular un promedio entre 3 números
def calcular_promedio(a, b, c):
    
    promedio=((a + b + c) / 3)
    
    print(f"El promedio es de: {promedio}")
    
numero1=int(input("Ingresa el primer número: "))

numero2=int(input("Ingresa el segundo número: "))

numero3=int(input("Ingresa el tercer número: "))

calcular_promedio(numero1, numero2, numero3)




