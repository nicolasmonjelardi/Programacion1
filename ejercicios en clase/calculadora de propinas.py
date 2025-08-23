#Ejercicio: calculadora de propinas en un restaurante
cuenta=int(input("ingrese el monto de la cuenta"))
print(f"propina sugerida (10%): {(cuenta/100)*10}")
print(f"total a pagar (10%): {cuenta+((cuenta/100)*10)}")
print(f"propina sugerida (15%): {(cuenta/100)*15}")
print(f"total a pagar (15%): {cuenta+((cuenta/100)*15)}")