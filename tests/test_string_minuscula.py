from mipaquete import string

def test_mayuscula():
    """Comprueba que devuelve la string en mayuscula"""
    assert string.minuscula('tiene que aparecer')  == 'tiene que aparecer'

def test_mayuscula__una_mayuscula():
    """Comprueba qu solo pone una palabra en minuscula"""
    assert string.minuscula('TIENE que aparecer')  == 'tiene que aparecer'

def test_mayuscula_todo_minuscula():
    """Comprueba que solo pone una palabra en minuscula"""
    assert string.minuscula('TIENE QUE APARECER')  == 'tiene que aparecer'