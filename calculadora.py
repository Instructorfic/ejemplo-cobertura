def sumar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def clasificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    return "cero"
