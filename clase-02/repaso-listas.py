print("Repaso Listas")

# Listas (Mutables)
## - Y que se puedan modificar
## - Agregar nuevos elementos
## - Reordenamiento
## (alumnos, producto de carrito)
## Lista alumnos, lista de los productos dentro del carrito
#

animales = ["rana", "perro", "gato", "tortuga", "raton", "ajolote", "paloma"]

print(animales)

# Acceso a los datos

print(animales[5])

print(animales[0])
print(animales)

# Recorriendo una lista

for animal in range(len(animales)):
    print(animales[animal])

# Matrices

matriz = [[1,2], [3, 4]]

print(matriz)

# Acceso a los datos

print(matriz[0][1]) # 2
print(matriz[1][1]) # 4

# Modificar elementos dentro de una matriz:

matriz[0][1] = 22
matriz[1][1] = 44

print(matriz[0][1]) # 22
print(matriz[1][1]) # 44

## Recorriendo las filas
for fila in matriz:
    print(fila)

## Recorriendo las filas y columnas
for fila in matriz:
    for valor in fila:
        print(valor)

# Tuplas (inmutables)
# - Los datos no deben cambiar
# - Queremos evitar errores accidentales
# - Coordeandas (x,y)
# - Configuraciones
# - Claves de diccionarios

coordenadas = (10, 20)
print(coordenadas[0])
print(coordenadas[1])

config = ("localhost", 5432)

print(config[0])
print(config[1])

for coord in coordenadas:
    print(coord)

## Desestructuración (desempaquetado)
host, port = config

## Ejemplo real

usuarios = (
    ("maxi", "admin"),
    ("ana", "editor"),
    ("leo", "viewer")
)

## Recorrer

for data in usuarios:
    print(data)


# Desectructurando del array usuarios, las claves username, rol

for username, role in usuarios:
    print(username, role)

## Nos dice la cantidad de elementos que tengo dentro de una lista o tupla

print(len(animales)) # la cantidad de elementos de la lista
print(len(usuarios)) # la cantidad de elementos de la tupla

# Lista de usuarios, solo puedo acceder a los valores con el indice (o sea la posición)
#          0,       1,         2
listas_usuarios = ["Pedro", "Juan", "Roberto"]

# Una estructura de datos clave -> valor

usuario = {
    "id": 1,
    "nombre": "Maxi",
    "rol": "admin"
}

#                 0     1       2
#                 id, nombre,  role
lista_usuarios = [1, "Maxi", "Roberto"]

usuario_maxi_dic = {
    "id": 1,
    "nombre": "Maxi",
    "rol": "admin",
    "direccion":{
        "calle": "Siempre viva",
        "altura": 123
    }
}

# notación corchete de js
print(usuario_maxi_dic["nombre"]) # maxi
print(usuario_maxi_dic["direccion"]["calle"]) # siempre viva
print(usuario_maxi_dic["direccion"]["altura"]) # 123

print("Fin del programa")

print(usuario_maxi_dic.get("nombre")) # Más segura de acceder al valor de la key
print(usuario_maxi_dic.get("nom")) # Si no encuentra la clave, devuelve none
print("Fin del programa")
# primera forma de recorrer
for key in usuario_maxi_dic:
    print(key, usuario_maxi_dic[key])
# segunda forma de recorrer
for key, value in usuario_maxi_dic.items():
    print(key, value)

print("Fin del programa")

