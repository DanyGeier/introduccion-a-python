def sumar(lista):
    return sum(lista)

def promedio(lista):
    suma = sum(lista)
    cont = len(lista)
    if cont > 0:
        prom = (suma / cont)
    return prom

def numero_mayor(lista):
    num_mayor = lista[0]
    for i in lista:
        if i > num_mayor:
            num_mayor = i
    return num_mayor

def numero_menor(lista):
    num_menor = lista[0]
    for i in lista:
        if i < num_menor:
            num_menor = i
    return num_menor
