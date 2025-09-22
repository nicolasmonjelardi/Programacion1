#Caso Número 3 (Tarjetas SUBE)
tarjetas=[]
saldos=[]
while True:
    print("// Opciones Disponibles //")
    print("1) Registrar tarjetas")
    print("2) Ingresar saldos")
    print("3) Mostrar tarjetas con su saldo")
    print("4) Consultar saldo de una tarjeta")
    print("5) Mostrar tarjetas sin saldo")
    print("6) Registrar una nueva tarjeta")
    print("7) Cargar/Debitar saldo")
    print("8) Salir")
    opcion=input("Seleccione una opción: ").strip()
    match opcion:
        case "1":
            
            cant=input("¿Cuantas tarjetas desea registrar? ")
            
            if not cant.isdigit():
                print("Debe ingresar un número")
                continue
            
            cant=int(cant)
            for i in range(cant):
                tarjeta=input("Ingrese el número de la tarjeta: ")
                tarjeta=tarjeta.strip()
                
                if not tarjeta.isdigit() or not len(tarjeta) == 16:
                    print("Ingrese un número de tarjeta válido")
                    continue
                
                if tarjeta in tarjetas:
                    print("Esta tarjeta ya está registrada")
                    continue
                
                tarjetas.append(tarjeta)
                saldos.append(0)
            
        case "2":
            
            if not tarjetas:
                print("Aún no hay tarjetas registradas")
                continue
            
            for i in range(len(tarjetas)):
                saldo=input(f"Ingrese el saldo de la tarjeta {tarjetas[i]} : ")
                
                if not saldo.isdigit():
                    print("Debe ingresar un número")
                    break
                
                saldo=int(saldo)
                saldos[i]=saldo
            
        case "3":
            
            if not tarjetas:
                print("Aún no hay tarjetas registradas")
                continue
            
            for i in range(len(tarjetas)):
                
                print(f"Tarjeta: {tarjetas[i]} - Saldo: {saldos[i]}")

        case "4":
            
            if not tarjetas:
                print("Aún no hay tarjetas registradas")
                continue
            
            consulta=input("Ingrese el número de la tarjeta: ")
            consulta=consulta.strip()
            
            if not consulta in tarjetas:
                print("La tarjeta no está registrada ")
                continue
            
            if not consulta.isdigit() or not len(consulta)==16:
                print("Ingrese un número de tarjeta válido")
            
            indice_tarjeta=tarjetas.index(consulta)
            
            print(f"Tarjeta: {tarjetas[indice_tarjeta]} - Saldo: {saldos[indice_tarjeta]}")
            
        case "5":
            
            if not tarjetas:
                print("Aún no hay tarjetas registradas")
                continue
            
            if 0 not in saldos:
                print("No hay tarjetas sin saldo")
                continue
            
            print("// tarjetas sin saldo //")
            for i in range(len(tarjetas)):
                
                if saldos[i]==0:
                    print(f"tarjeta: {tarjetas[i]} - saldo: {saldos[i]}")

        case "6":
            
            tarjeta_nueva=input("Ingrese el número de la tarjeta: ")
            tarjeta_nueva=tarjeta_nueva.strip()
            
            if not tarjeta_nueva.isdigit() or not len(tarjeta_nueva) == 16:
                print("Ingrese un número de tarjeta válido")
                continue
            
            if tarjeta_nueva in tarjetas:
                print("Esta tarjeta ya está registrada")
                continue
            
            saldo_nuevo=input("Ingrese el saldo de la tarjeta: ")
            
            if not saldo_nuevo.isdigit():
                print("Debe ingresar un número")
                continue
            
            tarjetas.append(tarjeta_nueva)
            saldos.append(saldo_nuevo)
            
        case "7":
            
            if not tarjetas:
                print("Aún no hay tarjetas registradas")
                continue
            
            while True:
                
                print("// Opciones Disponibles //")
                print("1) Cargar Saldo")
                print("2) Debitar saldo")
                print("3) Salir")
                opcion_7=input("Seleccione una opción: ")
                
                for i in range(len(tarjetas)):
                    print(f"Tarjeta: {tarjetas[i]} - Saldo: {saldos[i]}")
                    
                match opcion_7:
                    
                    case "1":
                        
                        cargar_tarjeta=input("Ingrese el número de la tarjeta: ").strip()

                        if not cargar_tarjeta.isdigit() or not len(cargar_tarjeta)==16:
                            print("Ingrese un número de tarjeta válido")
                            continue
                        
                        if not cargar_tarjeta in tarjetas:
                            print("La tarjeta no está registrada")
                            continue
                        
                        indice_saldo=tarjetas.index(cargar_tarjeta)
                        
                        cargar=input("¿Cuanto saldo desea cargar? ")
                        
                        if not cargar.isdigit():
                            print("Debe ingresar un número")
                            continue
                        
                        saldos[indice_saldo] += int(cargar)
                        
                    case "2":
                        
                        debitar_tarjeta=input("Ingrese el número de la tarjeta: ").strip()
                        
                        if not debitar_tarjeta.isdigit() or not len(debitar_tarjeta)==16:
                            print("Ingrese un número de tarjeta válido")
                            continue
                        
                        if not debitar_tarjeta in tarjetas:
                            print("La tarjeta no está registrada")
                            continue
                        
                        indice_saldo=tarjetas.index(debitar_tarjeta)
                        
                        debitar=input("¿Cuanto saldo desea debitar? ")
                        
                        if not debitar.isdigit():
                            print("Debe ingresar un número")
                            continue
                        
                        saldos[indice_saldo] -= int(debitar)

                    case "3":
                        print("Saliendo..")
                        break
                    
                    case _:
                        print("Seleccione una opción válida")
                        continue
                    
        case "8":
            print("Saliendo..")
            break
            
        case _:
            print("Seleccione una opción válida")
            continue