# ! Gestión de errores.
# * Errors de sintaxis
## El programa no arranca con estos errores

"""" if True
    print("Hola") """

# * Errores en tiempo de ejecución
# El código arranca... me permite ejecutarlo pero explota

# print(19 / 0)

# * Errores lógicos
# Este error depende de nosotros.

"""precio = 100
descuento = 20
total = precio - descuento / 100 """

# ? Gestión de errores con try / except
# print("Inicio de programa")
"""try:
    # Todx lo que quiero que se ejecute va dentro del try
    # Y que puede fallar
    print("Probando....")
    print(10 / 0)
    # otra sentencia
    # otra sentencia
    # otra sentencia
    print("Fin de la prueba probando...")
except ZeroDivisionError:
    print("No se puede dividir por cero")
print("Fin de programa") """
"""print("Inicio de programa")
try:
    numero = int(input("Ingrese un número"))
    print(10 / numero)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Ingresó un valor inválido")
print("Fin de programa")"""
"""print("Inicio de programa")
try:
    numero = int(input("Ingrese un número"))
    print(10 / numero)
except:
    print("Algo se rompió")"""

# ! else y finally
# * else: Lo que está en el cuerpo del else se ejecuta solo si el bloque try, está bien. no falla.

try:
    x = int("5") # si sale todo bien
    print(x)
except ValueError:
    print("Error")
else:
    print("Todo OK: ", x)

# * finally: No importa lo que ocurra en el try, siempre se va a ejecutar el finally

print("-------------------------------------------------")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto se ejecuta sin importar si hay excepción o no. Siempre")

# Cerrar archivos
# Cerrar conexión de la base de datos
# Liberar recursos
# Logs

# ! Errores personalizados
## Es un error que crea el desarrollador, un nombre claro, para una situación especifica

# -> Error generico -> ValueError - > genérico
# -> Error personalizado -> EdadInvalidaError

# EdadInvalidaError.py
# ? IMPORTANTE: Heredan de Exception
class EdadInvalidaError(Exception):
    pass

# raise -> Palabra reservada del lenguaje para lanzar una excepción
# validad_edad.py
def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")
    return edad

# main.py

try:
    edad = int(input("Ingresa tu edad: "))
    validar_edad(edad)
    print("Edad válida:", edad)
except EdadInvalidaError as e:
    print("Error:", e)
except ValueError:
    print("Eso no es un número")

