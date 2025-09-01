#Ejercicio bucle for
abecedario="abcdefghijklmnopqrstuvwxyz"
corrimiento=int(input("Ingrese el corrimiento de las letras: "))
frase_encriptada=""
for i in range (5):
    frase=input("Ingrese el mensaje que quiere enviar: ")
    frase_encriptada=""
    for letra in frase:
        if letra in abecedario:
            posicion=abecedario.index(letra)
            frase_encriptada=frase_encriptada+abecedario[(posicion+corrimiento)%27]
        else:
            frase_encriptada=frase_encriptada+letra
    else:
        print(frase_encriptada)
else: 
    print("Finalizado")

#Ejercicio bucle while

contador_maquina=0
contador_usuario=0
contador_empate=0
import random
opciones=["piedra","papel","tijera"]
while True:
    usuario=input("seleccione una opcion: piedra/papel/tijera. o escriba cancelar para finalizar: ").lower()
    if usuario=="cancelar":
        break
    if usuario in opciones:
        maquina=random.choice(opciones)
        print(f"la maquina eligio: {maquina}")
        if usuario=="piedra" and maquina=="tijera":
            print("gana el usuario!")
            contador_usuario+=1
        elif usuario=="tijera" and maquina=="papel":
            print("gana el usuario!")
            contador_usuario+=1
        elif usuario=="papel" and maquina== "piedra":
            print("gana el usuario!")
            contador_usuario+=1
        elif usuario==maquina:
            print("empate!")
            contador_empate+=1
        else:
            print("gana la maquina!")
            contador_maquina+=1
    else:
        print("opcion inválida")
        continue

print(f"contador usuario: {contador_usuario}")
print(f"contador maquina: {contador_maquina}")
print(f"contador empate: {contador_empate}")