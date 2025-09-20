#Caso 2 – Clínica – Turnos por especialidad (cupos del día)
especialidades=[]
cupos=[]
seguir=True
while seguir==True:
    print("// Operaciones Disponibles //")
    print("1) Ingresar especialidades ")
    print("2) Mostrar agenda")
    print("3) Consultar cupos de una especialidad")
    print("4) Listar especialidades sin cupo")
    print("5) Agregar especialidad")
    print("6) Actualizar cupos (Reservar/Cancelar)")
    print("7) Salir")
    opcion=input("Seleccione una operación: ")
    if int(opcion)==1:
        numero_especialidades=input("¿Cuantas especialidades desea ingrear? ")
        if numero_especialidades.isdigit():
            for i in range(int(numero_especialidades)):
                ingresar_especialidades=input("Ingrese una especialidad: ")
                if ingresar_especialidades=="":
                    print("Ingrese una especialidad válida")
                else:
                    especialidades.append(ingresar_especialidades)
                    ingresar_cupos=input("Ingrese la cantidad de cupos disponibles: ")
                    if ingresar_cupos.isdigit():
                        cupos.append(int(ingresar_cupos))
                    else:
                        print("Ingrese una cantidad de cupos válida")
    elif int(opcion)==2:
        print("// Agenda //")
        for i in range(len(especialidades)):
            print(f"{especialidades[i]} : {cupos[i]} cupos disponibles")
    elif int(opcion)==3:
        print("// Especialidades //")
        for i in range(len(especialidades)):
            print(especialidades[i])
        consultar_especialidad=input("Ingrese una especialidad para ver los cupos disponibles: ")
        if consultar_especialidad in especialidades:
            indice_especialidad=especialidades.index(consultar_especialidad)
            print(f"{especialidades[indice_especialidad]} : {cupos[indice_especialidad]} cupos")
        else:
            print("Ingrese una especialidad válida")
    elif int(opcion)==4:
        for i in range(len(cupos)):
            if cupos[i]==0:
                print(especialidades[i])
    elif int(opcion)==5:
        agregar_especialidad=input("Ingrese una nueva especialidad: ")
        if agregar_especialidad=="" or agregar_especialidad.isdigit():
            print("Ingrese una especialidad válida")
        else: 
            especialidades.append(agregar_especialidad)
            cupos.append(0)
            agregar_cupos=input("Ingrese la cantidad de cupos: ")
            if agregar_cupos.isdigit():
                cupos[(len(cupos)-1)]=agregar_cupos
            else:
                print("Ingrese una cantidad de cupos válida")
    elif int(opcion)==6:
        cantidad_a_actualizar=input("¿Cuantas especialidades desea actualizar? ")
        if cantidad_a_actualizar.isdigit() and int(cantidad_a_actualizar)<=len(especialidades):
            print("// Especialidades //")
            for i in range(len(especialidades)):
                print(especialidades[i])
            actualizar_especialidad=input("Selecciona una especialidad: ")
            if actualizar_especialidad in especialidades:
                print("// Operaciones //")
                print("1) Reservar cupo")
                print("2) Cancelar reserva")
                operacion_opcion6=input("Seleccion una operación: ")
                if operacion_opcion6.isdigit() and (int(operacion_opcion6)>=1 and int(operacion_opcion6)<=2):
                    indice_cupos=especialidades.index(actualizar_especialidad)
                    if int(operacion_opcion6)==1:
                        cupos[indice_cupos]-=1
                    elif int(operacion_opcion6)==2:
                        cupos[indice_cupos]+=1
                else:
                    print("Ingrese una operación válida")
            else:
                print("Ingrese una especialidad válida")
        else:
            print("Ingrese una cantidad válida")
    elif int(opcion)==7:
        seguir=False
        
    else:
        print("Ingrese una operación válida")