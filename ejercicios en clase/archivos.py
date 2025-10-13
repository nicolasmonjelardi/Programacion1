import csv
import os

ARCHIVO = "productos.csv"

#Crea el archivo si no existe
def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            writer.writeheader()

#Mostrar lista de productos
def mostrar_productos():
    try:
        with open(ARCHIVO, mode='r') as f:
            reader = csv.DictReader(f)
            productos = list(reader)
            if not productos:
                print("No hay productos registrados.")
                return
            total = 0
            print("\nProductos registrados:")
            for prod in productos:
                nombre = prod["nombre"]
                precio = float(prod["precio"])
                print(f"- {nombre} -> ${precio:.2f}")
                total += precio
            print(f"\nTotal de precios: ${total:.2f}\n")
    except Exception as e:
        print("Error al leer el archivo:", e)

#Agregar un nuevo producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = input("Ingrese el precio: ").strip()
    try:
        precio = float(precio)
        with open(ARCHIVO, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            writer.writerow({"nombre": nombre, "precio": precio})
        print("Producto agregado correctamente.\n")
    except ValueError:
        print("El precio debe ser un número.\n")

#Eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    try:
        with open(ARCHIVO, mode='r') as f:
            productos = list(csv.DictReader(f))
        nuevos = [p for p in productos if p["nombre"].lower() != nombre.lower()]
        if len(nuevos) == len(productos):
            print("Producto no encontrado.\n")
            return
        with open(ARCHIVO, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            writer.writeheader()
            writer.writerows(nuevos)
        print("Producto eliminado correctamente.\n")
    except Exception as e:
        print("Error al eliminar el producto:", e)

#Actualizar precio de un producto
def actualizar_precio():
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    try:
        with open(ARCHIVO, mode='r') as f:
            productos = list(csv.DictReader(f))
        encontrado = False
        for p in productos:
            if p["nombre"].lower() == nombre.lower():
                nuevo_precio = input("Ingrese el nuevo precio: ").strip()
                try:
                    p["precio"] = float(nuevo_precio)
                    encontrado = True
                except ValueError:
                    print("El precio debe ser un número.\n")
                    return
        if not encontrado:
            print("Producto no encontrado.\n")
            return
        with open(ARCHIVO, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            writer.writeheader()
            writer.writerows(productos)
        print("Precio actualizado correctamente.\n")
    except Exception as e:
        print("Error al actualizar el precio:", e)

#Menú principal
def menu():
    inicializar_archivo()
    while True:
        print("===== MENÚ DE PRODUCTOS =====")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Actualizar precio")
        print("5. Salir")
        print("=============================")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            
            case"1":
                mostrar_productos()
            case "2":
                agregar_producto()
            case "3":
                eliminar_producto()
            case "4":
                actualizar_precio()
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")

menu()