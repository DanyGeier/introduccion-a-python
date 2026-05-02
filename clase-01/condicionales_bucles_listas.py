print("Condicionales (Tomar decisiones)")

edad = 20
#print("Eres mayor de edad")

if edad >= 18:
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad")

# IMPORTANTE TRABAJAR IDENTANDO NUESTRAS SENTENCIAS CUANDO TRABAJAMOS CON BLOQUES
print("---------------------")

if edad >= 18:
    print("Mayor de edad")
    print("Puedes votar")
print("Fin del programa")

print("3 caminos o más con el if ")

# nota = 10

nota = int(input("Ingrese una nota de 1 a 10: "))

if nota < 4:
    print("Desaprobado")
elif nota < 7:
    print("Aprobado")
elif nota <9:
    print("Muy bien")
else: 
    print("Excelente")

print("Operadores lógicos")

# and (y lógico)
print("and (y lógico)")

edad = 23
tiene_licencia = True
if (edad>= 18 and tiene_licencia):
    print("Puedes manejar")
else:
    print("No puedes manejar")

# or (o lógico)
es_fin_semana = True
es_feriado = False

if es_fin_semana or es_feriado:
    print("No patino")
else:
    print("Patinamos")

# not (negación o lo opuesto)

print("Listas: Almacenar varios valores")

""" 
nombre = "Pedro"
nombre2 = "Carlos"
nombre3 = "Ana"
# Es dificil de mantener almacenar 100 personas cada una en una variable
 """

nombre = ["Pedro", "Carlos", "Ana"]

# Listas homogeneas (Recomendables)
## Lista de números
numeros = [10, 20, 30, 40]
## Lista de cadenas
frutas = ["manzana", "banana", "naranja"]

# Listas heterogeneas
## Lista mixta
datos = [25, "Maxi", 1.70, True]

# Lista vacia
lista_vacia = []

# Indices empieza en ', NO EN 1

print(frutas[1]) # banana
print(frutas[2]) # naranja

frutas[0] = "sandia"

print(frutas)

