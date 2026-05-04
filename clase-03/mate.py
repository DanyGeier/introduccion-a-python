import math

# Raiz cuadrada
print(math.sqrt(16)) # 4.0 # float

# Potencia
print(math.pow(2, 3)) # 8.0

# PI (constante)
print(math.pi) # 3.14159

# Redondear hacía arriba
print(math.ceil(4.2)) # 5

# Redondear hacia abajo
print(math.floor(4.8)) # 4

# Not a Number
print(math.isnan(2)) # Es un número
print(math.isnan(-4)) # Es un número
val = float('nan') 
print(math.isnan(val)) # No es número