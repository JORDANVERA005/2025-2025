# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para almacenar las notas
notas = {}

# Pedir la nota de cada asignatura
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas[asignatura] = nota

# Mostrar resultados
print("\nResumen de tus notas:")
for asignatura in asignaturas:
    print(f"En {asignatura} has sacado {notas[asignatura]}")
