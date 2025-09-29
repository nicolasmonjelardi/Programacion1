import random

# Lista con palabras, tematica: marcas de auto
palabras = ["ford", "audi", "bmw", "ferrari", "lamborghini", "fiat", "porsche", "renault", "volswagen", "citroen", "toyota"]

# Función para elegir una marca al azar
def elegir_palabra():
    return random.choice(palabras)

# Función para mostrar el tablero actualizado
def mostrar_tablero(palabra_secreta, letras_ingresadas, intentos_restantes):
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_ingresadas:
            estado += letra + " "
        else:
            estado += "_ "
    print("\nPalabra:", estado.strip())
    print("Letras ingresadas:", " ".join(letras_ingresadas))
    print(f"Intentos restantes: {intentos_restantes}")

# Función principal del juego
def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_ingresadas = []
    intentos = 6
    print("¡Bienvenido/a al juego del Ahorcado!")
    print("\nTemática: Marcas de autos")
    
    while intentos > 0:
        mostrar_tablero(palabra, letras_ingresadas, intentos)
        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingrese una letra válida")
            continue

        if letra in letras_ingresadas:
            print("Ya ingresó esa letra")
            continue

        letras_ingresadas.append(letra)

        if letra in palabra:
            print("¡Adivinaste una letra!")
        else:
            intentos -= 1
            print(f"Letra incorrecta, le quedan {intentos} intentos.")

        # Verificar si el jugador ganó
        if all(letra in letras_ingresadas for letra in palabra):
            mostrar_tablero(palabra, letras_ingresadas, intentos)
            print("\n¡Felicidades! Adivinaste la palabra:", palabra)
            break
    else:
        print("\nTe quedaste sin intentos, La palabra era:", palabra)

# Ejecutar el juego
jugar_ahorcado()