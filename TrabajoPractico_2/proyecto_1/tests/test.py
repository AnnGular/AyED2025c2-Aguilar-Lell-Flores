# Archivo de test para realizar pruebas unitarias del modulo1
from modules.burbuja import burbuja
import random

# def test_burbuja():
#     lista = [5, 3, 1, 4, 2]
#     esperado = [1, 2, 3, 4, 5]
#     resultado = burbuja(lista.copy())
#     if resultado == esperado:
#         print("burbuja(): OK")
#     else:
#         print("burbuja(): ERROR")

# if __name__ == "__main__":
#     test_burbuja()

def test_burbuja():
    lista = [random.randint(10000, 99999) for _ in range(500)]
    esperado = sorted(lista)
    resultado = burbuja(lista.copy())
    #print(resultado)
    if resultado == esperado:
        print("burbuja(): OK")
    else:
        print("burbuja(): ERROR")

if __name__ == "__main__":
    test_burbuja()

