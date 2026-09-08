import pytest
from calculadora import sumar, dividir, clasificar_numero


def test_sumar():
    assert sumar(5, 3) == 8


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_clasificar_positivo():
    assert clasificar_numero(10) == "positivo"
