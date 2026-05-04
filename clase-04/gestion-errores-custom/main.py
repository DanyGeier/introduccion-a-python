from saldo_insuficiente_error import saldo_insuficiente_error
import retirar_dinero

try:
    saldo = 10000
    monto = float(input("Ingrese monto a retirar: "))
    saldo = retirar_dinero.retirar_dinero(saldo, monto)
    print("Nuevo saldo:", saldo)
except saldo_insuficiente_error as e:
    print("Operación cancelada:", e)
except ValueError:
    print("El monto debe ser un número")
