from mipaquete import string

def test_mayuscula():
    """Comprueba que devuelve la string en mayuscula"""
    assert string.mayuscula('tiene que aparecer')  == 'TIENE QUE APARECER'

def test_mayuscula_solo_una_palabra():
    """Comprueba con una palabra en mayuscula devuelve la string en mayuscula"""
    assert string.mayuscula('TIENE que aparecer')  == 'TIENE QUE APARECER'

def test_mayuscula_toda_la_frase():
    """Comprueba con una palabra en mayuscula devuelve la string en mayuscula"""
    assert string.mayuscula('TIENE QUE APARECER')  == 'TIENE QUE APARECER'
