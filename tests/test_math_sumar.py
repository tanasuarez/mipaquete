from mipaquete.mipaquete import math

"""
TEST SUMAR
"""

def test_suma_positivos_enteros():
    """Comprueba que la de dos numeros positivos enteros"""
    assert math.sumar(2,2) == 4

def test_suma_positivos_float():
    """Comprueba que la de dos numeros positivos con decimales"""
    assert round(math.sumar(0.1, 0.2), 2) == 0.3

def test_suma_positivos_enteros_distinto_signo():
    """Comprueba que la de dos numeros distintos enteros"""
    assert math.sumar(2,-2) == 0
    assert math.sumar(-2,2) == 0

def test_suma_positivos_float_distinto_signo():
    """Comprueba que la de dos numeros distintos con decimales"""
    assert round(math.sumar(-0.1, 0.2), 2) == 0.1
    assert round(math.sumar(0.1, -0.2), 2) == -0.1