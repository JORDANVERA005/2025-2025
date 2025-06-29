# Lista para almacenar los números ganadores
numeros_ganadores = []

# Pedir 6 números ganadores al usuario
print("Introduce los 6 números ganadores de la Lotería Primitiva:")

while len(numeros_ganadores) < 6:
    try:
        numero = int(input(f"Número {len(numeros_ganadores)+1}: "))
        if 1 <= numero <= 49:
            if numero not in numeros_ganadores:
                numeros_ganadores.append(numero)
            else:
                print("Ese número ya ha sido introducido. Introduce uno diferente.")
        else:
            print("El número debe estar entre 1 y 49.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Ordenar la lista
numeros_ganadores.sort()

# Mostrar los números ordenados
print("\nLos números ganadores ordenados de menor a mayor son:")
print(numeros_ganadores)
