# Ejercicio 1:
# Pedir un número positivo al usuario. Si ingresa un número negativo o cero, vuelve a pedir.
# Voy a necesitar un (while) porque con un for no puedo trabajar en este caso
# Una vez obtenido, muestra todos los números desde el primero hasta ese número
# Ejemplo > 5 -> out -> 1 2 3 4 5
# Ejemplo > 10 -> out -> 1 2 3 4 5 6 7 8 9 10
# Ejemplo > 15 -> out -> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# Ejercicio 2:
# Crear una matriz de 3x3 con calificaciones de 3 estudiantes (3 notas cada uno)
# [3, 10, 8] # Estudiante 1
# [4, 2, 6] # Estudiante 2
# [8, 7, 6] # Estudiante 3

# Imprimir:
# - Cada estudiante con todas sus notas
# - El promedio de cada estudiante

print("---Ejercicio 1---")
numero = int(input("Ingrese un numero: "))
while (numero <= 0):
    numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    if i == numero:
        print(i)
    else:
        print(i, end=" ")

print("---Ejercicio 2---")
matriz = [
    [3, 10, 8],
    [4, 2, 6],
    [8, 7, 6]
]

print(matriz)
