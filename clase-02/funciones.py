def imprimir(lista):
    for numero in lista:
        print(numero)
    return lista

def calcular_suma(lista):
    sum = 0
    for numero in lista:
        sum+= numero
    return sum

def calcular_promedio(suma, lista):
    return suma / len(lista)


