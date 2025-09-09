# Crear cartón 
import random
numeros_random = random.sample(range(1, 51), 25)
carton = [numeros_random[i:i+5] for i in range(0, 25, 5)]

print("¡Bienvenido/a al Bingo!")
print("Este es tu cartón:")
for fila in carton:
    print(fila)

# Lista para guardar los números que ya salieron
numeros_sorteados = []

# Bucle principal del juego
while True:
    # Sorteo sin repetir números
    numero = random.randint(1, 50)
    if numero in numeros_sorteados:
        continue
    numeros_sorteados.append(numero)

    print("\nNúmero sorteado:", numero)
    encontrado = False

    # Buscar el número en el cartón y reemplazarlo por un 0
    for i in range(len(carton)):
        for j in range(len(carton[i])):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print("¡El número está en tu cartón!")
    else:
        print("El número no está en tu cartón.")

    # Mostrar cartón actualizado
    print("Cartón actualizado:")
    for fila in carton:
        print(fila)

    # Verificar si todo el cartón está lleno de 0
    carton_completo = True
    for fila in carton:
        if fila.count(0) != len(fila):
            carton_completo = False
            break

    if carton_completo:
        print("¡Bingo!")
        break
