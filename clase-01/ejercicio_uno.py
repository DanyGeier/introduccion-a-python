""" 
Eejercicio 1: Variables y tipos ()

Consigna: Crear un programa que gaurde variables

* El nombre
* El apellido
* La altura en metros (números decimales)
* Si sos estudiante o no (verdadero o falso)
Mostrar en pantalla todos los datos.
 """

nombre = input("Escribe aqui tu nombre: ")
apellido = input("Escribe aqui tu apellido: ")
altura = float(input("Escribe aqui tu altura en metros: "))
es_estudiante = True 
respuesta = input("¿Sos estudiante? (si/no)").lower()
es_estudiante = (respuesta == "si")

print(f": {nombre} {apellido} {altura} {es_estudiante}")

