from mipaquete import math

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


""""
TEST RESTAR
"""
def test_restar_positivos_enteros():
    """Comprueba que la de dos numeros positivos enteros"""
    assert math.restar(2,2) == 0

def test_restar_positivos_float():
    """Comprueba que la de dos numeros positivos con decimales"""
    assert round(math.restar(0.1, 0.2), 2) == -0.1

def test_restar_positivos_enteros_distinto_signo():
    """Comprueba que la de dos numeros distintos enteros"""
    assert math.restar(2,-2) == 4
    assert math.restar(-2,2) == -4

def test_restar_positivos_float_distinto_signo():
    """Comprueba que la de dos numeros distintos con decimales"""
    assert round(math.restar(-0.1, 0.2), 2) == -0.3
    assert round(math.restar(0.1, -0.2), 2) == 0.3

""""
TEST multiplicar
"""
def test_multiplicar_positivos_enteros():
    """Comprueba que la de dos numeros positivos enteros"""
    assert math.multiplicar(2,2) == 4

def test_multiplicar_positivos_float():
    """Comprueba que la de dos numeros positivos con decimales"""
    assert round(math.multiplicar(0.1, 0.2), 2) == 0.02

def test_multiplicar_positivos_enteros_distinto_signo():
    """Comprueba que la de dos numeros distintos enteros"""
    assert math.multiplicar(2,-2) == -4
    assert math.multiplicar(-2,2) == -4

def test_multiplicar_positivos_float_distinto_signo():
    """Comprueba que la de dos numeros distintos con decimales"""
    assert round(math.multiplicar(-0.1, 0.2), 2) == -0.02
    assert round(math.multiplicar(0.1, -0.2), 2) == -0.02