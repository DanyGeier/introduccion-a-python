from saldo_insuficiente_error import saldo_insuficiente_error

def retirar_dinero(saldo, monto):
    if monto > saldo:
        raise saldo_insuficiente_error("No tenés saldo suficiente")
    return saldo - monto
