from errores import SaldoInsuficienteError
from operaciones import retirar_dinero

try:
    saldo = 1000.0
    monto = float(input("Ingrese monto a retirar: "))
    saldo = retirar_dinero(saldo, monto)
    print("Nuevo saldo: ", saldo)
except SaldoInsuficienteError as e:
    print("Operación cancelada: ", e)
except ValueError:
    print("El monto debe ser un número")