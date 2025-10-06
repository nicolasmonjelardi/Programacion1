#ejercicio: crear una mochila mágica


#Crear mochila
def crear_mochila():
    
    mochila=[]
    
    while True:
        try:
            espacio_mochila=input("Ingrese cuantos espacios tendrá la mochila: ")
            
            if not espacio_mochila.isdigit():
                raise ValueError
            
            espacio_mochila=int(espacio_mochila)
            
        except ValueError:
            
            print("Debe ingresar un número válido")
            
            continue
        
        break
    
    return espacio_mochila


#Guardar un objeto en la mochila

def guardar_objeto():
    
    while True:
        
        try:
            
            objeto=input("Ingrese el objeto a guardar: ")
            
            if objeto=="":
                raise ValueError

        except ValueError:
            print("Ingrese un objeto válido")
            
            continue
        
        try:
            posicion=input("Ingrese la posición en la que desea guardarlo: ")

            if not posicion.isdigit() or int(posicion) > (len(mochila)-1):
                
                raise IndexError
            
            if posicion=="":
                
                raise ValueError
            
        except IndexError:
            
            print("Ingrese una posición Válida")
            
            continue
            
        except ValueError:
            
            print("Debe ingresar una posición")
            
        break
    
    posicion=int(posicion)
    
    mochila[posicion]=objeto
    
    return posicion


#Ver contenido de la mochila

def ver_contenido():
    
    for i in range (len(mochila)):
        
        if mochila[i]=="":
            print(f"Espacio {i}: --- vacío ---")
        else:
            print(f"Espacio {i}: {mochila[i]}")


mochila=[""] * crear_mochila()


#Bucle principal

while True:
    

    print("Opciones Disponibles")
    print("1) Guardar un objeto")
    print("2) Ver contenido de la mochila")
    print("3) Salir")

    opcion=input("Seleccione una opción: ")

    match opcion:
        
        case "1":
            
            guardar_objeto()
            
        case "2":
            
            ver_contenido()

        case "3":
            
            print("Saliendo...")
            
            break
        
        case _:
            
            print("Debe ingresar una opcion válida")
            
            continue
