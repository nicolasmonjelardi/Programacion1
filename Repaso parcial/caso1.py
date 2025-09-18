#caso uno: sistema para biblioteca
titulos=[] 
ejemplares=[] 
prestamos=0
devolucion=0  
sistema=True
while sistema==True:
    print("// Operaciones Disponibles //")
    print("1) Ingresar títulos disponibles")
    print("2) Ingresar ejemplares disponibles actualizados")
    print("3) Mostrar catálogo con stock")
    print("4) Consultar disponibilidad de un título")
    print("5) Listar títulos agotados")
    print("6) Agregar títulos")
    print("7) Actualizar ejemplares (préstamo/devolución)")
    print("8) Ver catálogo")
    print("9) Salir")
    operacion=(input("Selecciona una operación: "))
    if operacion.isdigit() and (int(operacion)>=1 and int(operacion)<=9):
        if int(operacion)==1:
            #Ingresar títulos disponibles
            cantidad_titulos=input("¿Cuantos títulos quiere ingresar? ")
            if cantidad_titulos.isdigit() and int(cantidad_titulos)>0:
                for i in range(int(cantidad_titulos)):
                    añadir_titulo=(input("Ingrese un título: "))
                    if añadir_titulo=="":
                        print("Por favor ingrese un título válido")
                    else:
                        titulos.append(añadir_titulo)
                    ejemplares_disponibles=(input("Ingrese la cantidad de ejemplares disponibles: "))
                    if ejemplares_disponibles.isdigit() and int(ejemplares_disponibles)>0:
                        ejemplares.append(int(ejemplares_disponibles))
                    else:
                        print("Por favor ingrese una cantidad válida")
            else:
                print("Por favor ingrese una cantidad válida")
        elif int(operacion)==2:
            #Ingresar ejemplares disponibles actualizados
            for i in range(len(titulos)):
                print(f"Ingrese la cantidad actualizada de ejemplares disponibles del título {titulos[i]}")
                ejemplares_disponibles_actualizados=input("ejemplares: ")
                if ejemplares_disponibles_actualizados.isdigit() and int(ejemplares_disponibles_actualizados)>=0:
                    ejemplares[i]=int(ejemplares_disponibles_actualizados)
                else:
                    print("Por favor ingrese una cantidad válida")
        elif int(operacion)==3:
            #Mostrar catálogo con stock
            print("// Catálogo //")
            for i in range(len(titulos)):
                if int(ejemplares[i])>0:
                    print(f"{titulos[i]}: {ejemplares[i]} copias")
        elif int(operacion)==4:
            #Consultar disponibilidad de un título
            operacion_4=True
            while operacion_4==True:
                print("// Opciónes disponibles //")
                print("1) Ingresar un título")
                print("2) Salir")
                opcion_operacion_4=input("Selecciona una opción: ")
                if opcion_operacion_4.isdigit() and (int(opcion_operacion_4)>0 and int(opcion_operacion_4)<3 ):
                    if int(opcion_operacion_4)==1:
                        print(titulos)
                        seleccion_ejemplar=input("Ingrese el nombre del título: ")
                        if seleccion_ejemplar in titulos:
                            indice_titulos=titulos.index(seleccion_ejemplar)
                            print(f"{titulos[indice_titulos]} : {ejemplares[indice_titulos]} copias")
                        else:
                            print("Por favor ingrese un títulos válido")
                    elif int(opcion_operacion_4)==2:
                        break
                    else:
                        print("Por favor ingrese una opción válida")
                        continue
                else:
                    print("Por favor ingrese una opción válida")
        elif int(operacion)==5:
            #Listar títulos agotados
            print("// Títulos agotados //")
            for i in range(len(ejemplares)):
                if ejemplares[i]==0:
                    print(titulos[i])
        elif int(operacion)==6:
            #Agregar títulos
            cantidad_titulos_agregados=input("¿Cuantos títulos desea agregar? ")
            if cantidad_titulos_agregados.isdigit() and int(cantidad_titulos_agregados)>0:
                for i in range(int(cantidad_titulos_agregados)):
                    titulo_nuevo=input("Ingrese el nuevo título: ")
                    if titulo_nuevo=="":
                        print("Por favor ingrese un título válido")
                    else:
                        titulos.append(titulo_nuevo)
                    ejemplares_nuevos=input("Ingrese el número de ejemplares: ")
                    if ejemplares_nuevos.isdigit() and int(ejemplares_nuevos)>0:
                        ejemplares.append(ejemplares_nuevos)
                    else:
                        print("Por favor ingrese una cantida válida")
            else:
                print("Por favor ingrese una cantidad válida")
        elif int(operacion)==7:
            #Actualizar ejemplares (préstamo/devolución)
            cantidad_ejemplares_actualizados=input("¿Cuantos títulos quiere actualizar? ")
            if int(cantidad_ejemplares_actualizados)<=len(titulos):
                if cantidad_ejemplares_actualizados.isdigit() and int(cantidad_ejemplares_actualizados)>0:
                    print(titulos)
                    for i in range(int(cantidad_ejemplares_actualizados)):
                            ejemplar_actualizado=input("Ingrese el título que desea actualizar: ")
                            if ejemplar_actualizado in titulos:
                                indice_ejemplares=titulos.index(ejemplar_actualizado)
                                print("// Opciónes disponibles //")
                                print("1) Prestamo")
                                print("2) Devolución")
                                opcion_operacion_7=input("Ingrese la opción deseada: ")
                                if opcion_operacion_7.isdigit() and (int(opcion_operacion_7)>0 and int(opcion_operacion_7)<3):
                                    if int(opcion_operacion_7)==1:
                                        prestamo=input("Ingrese cuantos ejemplares se dieron a préstamo: ")
                                        if prestamo.isdigit() and (int(prestamo)>0 and int(prestamo)<= ejemplares[indice_ejemplares]):
                                            ejemplares[indice_ejemplares] -= int(prestamo)
                                    elif int(opcion_operacion_7)==2:
                                        devolucion=input("Ingrese cuantos ejemplares se devolvieron: ")
                                        if devolucion.isdigit() and int(devolucion)>0:
                                            ejemplares[indice_ejemplares]+=int(devolucion)
                                else:
                                    print("Por favor ingrese una opción válida ")
                            else:
                                print("Por favor ingrese un título válido")
                else:
                    print("Por favor ingrese una cantidad válida")
            else:
                print("Por favor ingrese una cantidad válida")
        elif int(operacion)==8:
            #Ver catálogo
            print("// Catálogo //")
            for i in range(len(titulos)):
                print(titulos[i])
        elif int(operacion)==9:
            #Salir
            sistema=False
        else: 
            print("Por favor ingrese una opción válida")
            continue
    else:
        print("Por favor ingresar una opcón válida")
        continue