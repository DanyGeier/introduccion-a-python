import random

# Número aleatorio entre 1 y 10
numero = random.randint(1, 10)
print(numero)

# Elegir un elemento aleatorio de una lista
frutas = ["manzana", "banana", "naranja", "kiwi"]
fruta_sorteada = random.choice(frutas)
print(fruta_sorteada)

# Mezclar una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numeros)
print(numeros) # Orden aleatorio

