from datetime import datetime

# Obtener fecha y hora actual
ahora = datetime.now()
print(ahora)

# Obtener solo la fecha
print(datetime.now().date())
print(ahora.date())

# Obteber solo la hora
print(datetime.now().time())
print(ahora.time())

# Año, mes, dia por separado

print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)

# Formatear la fecha en Python
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#
print(ahora.strftime("%Y-%m-%d"))
