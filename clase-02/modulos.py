import operacion
from logica import calcular_doble, calcular_triple as ct
from logica import * # evitarlo usar
# Modulos y funciones 
# Se puede poner un alias a la función delmodulo que estoy incorporando, lo hago con as

# Una función en python se crea a partir de la palabra reservada def

# funcion javascript
""" funcion sumar (a, b){
    return a + b
} """

def sumar(a,b):
    return a + b

print(sumar(4,4)) # 8

def sumarModulo(x, y):
    return x + y

print(operacion.sumar_modulo(4, 2))
print(operacion.resta_modulo(10, 7))

print(calcular_doble(50))
print(ct(10))

