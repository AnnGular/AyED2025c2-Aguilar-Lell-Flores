# Archivo de test para realizar pruebas unitarias del modulo1
from modules.modulo1 import burbuja, quicksort, radixsort

def test_burbuja():
    lista = [5, 3, 1, 4, 2]
    esperado = [1, 2, 3, 4, 5]
    resultado = burbuja(lista.copy())
    if resultado == esperado:
        print("burbuja(): OK")
    else:
        print("burbuja(): ERROR")

def test_quicksort():
    lista = [5, 3, 1, 4, 2]
    esperado = [1, 2, 3, 4, 5]
    resultado = quicksort(lista.copy())
    if resultado == esperado:
        print("quicksort(): OK")
    else:
        print("quicksort(): ERROR")

def test_radixsort():
    lista = [5, 3, 1, 4, 2]
    esperado = [1, 2, 3, 4, 5]
    resultado = radixsort(lista.copy())
    if resultado == esperado:
        print("radixsort(): OK")
    else:
        print("radixsort(): ERROR")


if __name__ == "__main__":
    test_burbuja()
    test_quicksort()
    test_radixsort()

