
def sumar(a : int, b: int) -> int:
    """La función devuelve la suma de las variables a y b"""    
    return a + b if son_numeros(a,b) else 0

def restar(a : int, b: int) -> int:
    """La función devuelve la suma de las variables a y b, si no """
    return a - b if son_numeros(a,b) else 0

def multiplicar(a : int, b: int) -> int:
    """La función devuelve la multiplicación de las variables a y b"""
    return a * b if son_numeros(a,b) else 0

def son_numeros(a, b) -> bool :
    """La función devuelve True si ambos numeros no son una cadena"""
    return type(a) and type(b) is not str
