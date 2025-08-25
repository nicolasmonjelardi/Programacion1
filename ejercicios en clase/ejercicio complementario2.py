fecha=input("ingrese la fecha de hoy")
dia=fecha.split(",")
dia_semana=dia[0]
aux=dia[1].strip().split("/")
dd=int(aux[0])
mm=int(aux[1])
if dd>31:
    print("día inválido")
elif mm>12: 
    print("mes inválido")
elif dia_semana.lower()=="lunes":
    examen=input("¿se tomó exámen?")
    if examen.lower()=="si":
        aprobados=int(input("¿cuantos alumnos aprobaron?"))
        desaprobados=int(input("¿cuantos alumnos desaprobaron?"))
        porcentaje_aprobados=float(((aprobados/(aprobados+desaprobados))*100))
        print(f"aprobó el {porcentaje_aprobados}% de alumnos")
elif dia_semana.lower()=="martes":
    examen=input("¿se tomó exámen?")
    if examen.lower()=="si":
        aprobados=int(input("¿cuantos alumnos aprobaron?"))
        desaprobados=int(input("¿cuantos alumnos desaprobaron?"))
        porcentaje_aprobados=(aprobados/(aprobados+desaprobados))*100
        print(f"aprobó el {porcentaje_aprobados}% de alumnos")
elif dia_semana.lower()=="miercoles":
    examen=input("¿se tomó exámen?")
    if examen.lower()=="si":
        aprobados=int(input("¿cuantos alumnos aprobaron?"))
        desaprobados=int(input("¿cuantos alumnos desaprobaron?"))
        porcentaje_aprobados=float((aprobados/(aprobados+desaprobados))*100)
        print(f"aprobó el {porcentaje_aprobados}% de alumnos")
elif dia_semana.lower()=="jueves":
        asistencia=float(input("¿que porcentaje de alumnos asistió?"))
        if asistencia > 50:
            print("asistió la mayoría")
        else: 
            print("no asistió la mayoría")
elif dia_semana.lower()=="viernes":
        if dd==1 and mm==1 or mm==7:
            print("comienzo de nuevo ciclo")
            cantidad_alumnos=int(input("ingrese la cantidad de alumnos"))
            arancel=int(input("ingrese el arancel por alumno en $"))
            ingreso_total=arancel*cantidad_alumnos
            print(f"el ingreso total es de: ${ingreso_total} ")
else: 
    print("día inválido")