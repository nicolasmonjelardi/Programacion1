alumnos=[]
asistencias=[]
seguir=True
while seguir==True:
    print("// Operaciones Disponinles //")
    print("1) Ingresar nombre  de estudiantes")
    print("2) Mostrar listado de alumnos con sus asistencias")
    print("3) Consultar las asistencias de un estudiante")
    print("4) listar estudiantes con asistencia 0")
    print("5) agregar un nuevo estudiante")
    print("6) registrar la asistencia de un estudiante")
    print("7) Salir del programa")
    opcion=input("Ingrese una opción: ")
    if int(opcion)==1:
        numero_de_alumnos=input("¿Cuantos alumnos desea cargar al sistemas? ")
        if numero_de_alumnos.isdigit() and int(numero_de_alumnos)>0:
            for i in range(int(numero_de_alumnos)):
                nombre_alumno=input("Ingrese el nombre completo del alumno: ")
                if nombre_alumno=="" or nombre_alumno.isdigit():
                    print("Ingrese un nombre válido")
                else:
                    alumnos.append(nombre_alumno)
                    asistencias.append(0)
                    asistencias_alumno=input("Ingrese el número de asistencias del alumno: ")
                    if asistencias_alumno.isdigit() and int(asistencias_alumno)>=0:
                        asistencias[i]=asistencias_alumno
                    else:
                        print("Ingrese un número de asistencias válido")
        else:
            print("Ingrese un número de alumnos válido")
    elif int(opcion)==2:
        for i in range(len(alumnos)):
            print(f"{alumnos[i]} : {asistencias[i]} asistencias")
    elif int(opcion)==3:
        consultar_alumno=input("Ingrese el nombre del alumno para ver sus asistencias: ")
        if consultar_alumno.isdigit() or consultar_alumno=="":
            print("Ingrese un alumno válido")
        else:
            indice_alumno=alumnos.index(consultar_alumno)
            print(f"{alumnos[indice_alumno]} : {asistencias[indice_alumno]} asistencias")
    elif int(opcion)==4:
        print("// Alumnos con asistencias 0 //")
        for i in range(len(alumnos)):
            if asistencias[i]==0:
                print(f"{alumnos[i]}")
    elif int(opcion)==5:
        nuevo_estudiante=input("Ingrese el nombre completo del nuevo estudiante: ")
        if nuevo_estudiante.isdigit() or nuevo_estudiante=="":
            print("Ingrese un nombre válido")
        else:
            alumnos.append(nuevo_estudiante)
            asistencias.append(0)
    elif int(opcion)==6:
        agregar_asistencia=input("Ingrese el nombre completo del estudiante para agregarle una asistencia: ")
        if agregar_asistencia in alumnos:
            indice_alumno=alumnos.index(agregar_asistencia)
            asistencias[indice_alumno]+=1
        else:
            print("Ingrese un alumno válido")
    elif int(opcion)==7:
        seguir=False
    else:
        print("Ingrese una opción válida")
        continue