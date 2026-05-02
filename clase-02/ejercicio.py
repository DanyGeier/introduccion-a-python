# Eejercicio: Listas
## Consigna: Crear una lista de números. Y luego:
# - [10, 22, 55, 2, 88, 7]
# - Imprimir cada número | imprimir(lista)
# - Calcular la suma de todos | suma = calcular_suma(lista)
# - Calcular el promedio | promedio = calcular_promedio(suma, lista)
# - Mostrar la suma de los números y el promedio

from funciones import imprimir, calcular_suma, calcular_promedio

lista = [10, 22, 55, 2, 88, 7]
print(imprimir(lista))

suma = calcular_suma(lista)
print("Suma: ", suma)

promedio = calcular_promedio(suma, lista)
print("El promedio: ", promedio)
