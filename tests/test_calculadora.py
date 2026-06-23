from src.calculadora import sumar, restar


def test_suma():
    assert sumar(2,3) == 5


def test_resta():
    assert restar(5,3) == 2
