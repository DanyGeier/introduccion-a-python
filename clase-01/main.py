print("Hola mundo!")

print("Comentario en una línea")

# Una sola línea papa

print("Comentario multilínea")

""" En
varias
lineas """

print("Variables")

nombre = "Dani"
print(nombre) # Cadena

print(type(nombre))

edad = 22
print(edad)

print(type(edad))

is_teacher = True # snake case -> palabra1_palabra2_palabra3
print(type(is_teacher))
print(is_teacher)
is_teacher = False
print(type(is_teacher))
print(is_teacher)

precio = 39.99
print(type(precio))
print(precio)

# Shortcut -> Play -> buscar uno que sea comodo (Ctrl + F6)

print("Concatenación de cadenas")

# Concatenar (juntar texto -> unir textoa)

segundo_nombre = "Alejandro"
apellido = "Geier"

nombre_completo = nombre + " " + segundo_nombre + " " + apellido
print(nombre_completo)

texto = "La" * 3
print(texto) # LaLaLa

print("Función input(): Para pedir datos al usuario")
dato = input("Escribe aqui tu nombre: ")
# print(input("Escribe aqui tu nombre: "))
print(dato)
print("Hola " + dato)
print(f'Hola {dato}') # Otra forma de concatenar (El print tiene caracteristicas para formatar la salda)

print("Casteo (Conversión de tipos)")
print("funcion int() <-- castea la cadena a un número entero")
cantidad_alumnos = (int(input("¿Cuantos alumnos están en clase? ")))
print(cantidad_alumnos)
print(type(cantidad_alumnos))
#                       cadena       + numero # ! No se puede concatenar una cadena y un número
cantidad_personas = cantidad_alumnos + 2

print(cantidad_personas)
print(type(cantidad_alumnos))