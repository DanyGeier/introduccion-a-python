from utils.promedio import calcular as calcular_promedio
from utils.suma import calcular as calcular_suma

lista = [10, 22, 55, 2, 88, 7]

sumatoria = calcular_suma(lista)
promedio = calcular_promedio(sumatoria, lista)

print(f'La sumatoria es igual: {sumatoria}')
print(f'El promedio es igual: {promedio}')