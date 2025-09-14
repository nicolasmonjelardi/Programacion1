#Trabajo práctico n4: listas

#punto 1
multiplos_de_4=[]
print("Multiplos de 4 del 1 al 100")
for numero in range(1,101):
    if numero % 4 ==0:
        multiplos_de_4.append(numero)

print(multiplos_de_4)

#punto 2
lista_numeros=[1,2,3,4,5]
print(f"Lista de números\n {lista_numeros}")
print("Penúltimo elemento:")
print(lista_numeros[-1])

#punto 3
lista_vacia=[]
lista_vacia.append("A")
lista_vacia.append("B")
lista_vacia.append("C")
print("//Lista con palabras//")
print(lista_vacia)

#punto 4
animales=["perro", "gato", "conejo", "pez"]
print("//Lista con animales//")
print(animales)
animales[-1]="oso"
animales[-3]="loro"
print("//Lista con animales nuevos//")
print(animales)

#punto 5

#numeros=[8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)

#lo que se realiza en este caso es buscar en valor mas grande en la lista numeros con: max(numeros)
#luego remover ese valor con: .remove()
#y por último se muestra la lista sin ese valor 

#punto 6
numeros=[]
numeros=list(range(10,31,5))
print(f"Primer número: {numeros[0]}\nSegundo número: {numeros[1]}")

#punto 7
autos=["sedan", "polo", "suran", "gol"]
print(f"Lista de autos: {autos}")
for i in range(1,3):
    auto_nuevo=input("Ingrese 2 autos: ")
    autos[i]=auto_nuevo

print(f"Nueva lista de autos: {autos}")

#punto 8
dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(f"Lista con dobles: {dobles}")

#punto 9
print("Compras: ")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(compras)
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(f"Lista de compras actualizada:\n{compras}")

#punto 10
lista_anidada=[15, True, [25.5, 57.9, 30.6], False ]
print(f"Lista anidada:\n{lista_anidada}")