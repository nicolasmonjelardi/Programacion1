#Trabajo Práctico N°7: Datos Complejos 

#punto 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

#punto 2

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800

#punto 3

frutas=["Banana", "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"]

#Punto 4

contactos={}

for i in range (5):
    
    contacto=input("Ingrese el nombre de contacto para registrarlo: ")
    
    numero=input("Ingrese el número del contacto: ")
    
    contactos[contacto]=numero

consultar_contacto=input("Ingrese el nombre de un contacto para saber su número: ")

print(f"Número de {consultar_contacto} : {contactos[consultar_contacto]}")

#punto 5

frase=input("Ingrese una frase: ")

palabras=frase.split()

set_de_palabras=set(palabras)

contador={}

for palabra in palabras:
    
    contador[palabra]=contador.get(palabra, 0) + 1

print(f"Palabras sin repetir: {set_de_palabras}")

print("Cantidad de veces que aparecen las palabras")

for palabra, cantidad in contador.items():
    
    print(f"{palabra} : {cantidad}")

#punto 6

alumnos = {}
notas_alumnos=[]

for i in range(3):
    
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    for j in range(3):
        
        notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")))
        
        notas_alumnos.append(notas)

    alumnos[nombre]=tuple(notas_alumnos)

print("Promedio de los alumnos:")

for nombre, notas in alumnos.items():
    
    promedio = sum(notas) / len(notas)
    
    print(f"{nombre}: {promedio:.2f}")

#punto 7

parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105, 106}

aprobaron_ambos = parcial1 & parcial2

aprobaron_solo_uno = (parcial1 ^ parcial2)

lista_total = parcial1 | parcial2

print("Aprobaron ambos parciales:", aprobaron_ambos)
print("Aprobaron solo uno de los dos parciales:", aprobaron_solo_uno)
print("lista total de aprobados en al menos un parcial:", lista_total)

#punto 8

def agregar_producto():
    
    while True:
        producto=input("Ingrese el  nombre del producto: ")
        
        if producto in productos:
            print("Este producto ya está registrado")
            continue
        
        if producto=="":
            print("Error - Ingrese un producto válido")
            continue
        
        productos[producto]=0
        break

def actualizar_stock():
    
    while True:
        
        if not productos:
            print("Todavía no hay productos registrados")
            break
        
        producto=input("Ingrese el nombre del producto para actualizar su stock: ")
        
        if not producto in productos or producto=="":
            print("Ingrese un producto válido")
            continue
            
        stock=input("Ingrese el stock del producto: ")
        
        if not stock.isdigit() or stock=="":
            print("Ingrese un número de stock válido")
            continue
        
        productos[producto]=stock
        
        break


def consultar_stock():
    
    if not productos:
        print("Todavía no hay productos registrados")
        return
    
    while True:
        
        producto=input("Ingrese el nombre del producto para consultar su disponibilidad: ")
        
        if not producto in productos:
            
            print("Ingrese un producto válido")
            continue
        
        else:
            
            print(f"{producto} : {productos[producto]} disponibles")
            break


productos={}

while True:
    
    print("Opciones Disponibles")
    print("1) Agregar un producto")
    print("2) Actualizar stock de un producto")
    print("3) Consultar stock de un producto")
    print("4) Salir del programa")
    
    opcion=input("Seleccione una opción: ")
    
    match opcion:
        
        case "1":
            
            agregar_producto()
            
        case "2":
            
            actualizar_stock()
            
        case "3":
            
            consultar_stock()
            
        case "4":
            
            print("Saliendo....")
            break
        
        case _:
            
            print("Error - Seleccione una opción válida")
            continue

#punto 9

agenda = {
    ("lunes", "09:00"): "Reunión con el equipo",
    ("martes", "14:30"): "Clase de Educación Física",
    ("miércoles", "11:00"): "Preparación de materiales",
    ("jueves", "16:00"): "Tutoría con alumnos",
    ("viernes", "08:00"): "Planificación semanal"
}

dia = input("Ingresá un día de la semana: ").lower()
hora = input("Ingresá un horario: ")

evento = agenda.get((dia, hora))

if evento:
    print(f"Actividad programada: {evento}")
else:
    print("No hay actividades agendadas en este horario.")

#punto 10

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Italia": "Roma"
}

capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    
    capitales_a_paises[capital] = pais


print("Diccionario invertido (capital → país):")
print(capitales_a_paises)



