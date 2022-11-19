from mipaquete import math as m

def test_suma_positivos():
    "Comprueba que la de dos numeros positivos"
    assert m.sumar(2,2) == 4
    assert m.sumar(0.1, 0.2) == 0.3