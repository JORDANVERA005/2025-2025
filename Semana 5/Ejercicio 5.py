# Crear la lista con los números del 1 al 10
numeros = list(range(1, 11))

# Invertir la lista
numeros_invertidos = numeros[::-1]

# Mostrar los números invertidos, separados por comas
print(", ".join(str(numero) for numero in numeros_invertidos))