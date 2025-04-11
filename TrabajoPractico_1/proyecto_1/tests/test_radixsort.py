from modules.radixsort import radixsort
import random

# def test_radixsort():
#     lista = [5, 3, 1, 4, 2]
#     esperado = [1, 2, 3, 4, 5]
#     resultado = radixsort(lista.copy())
#     if resultado == esperado:
#         print("radixsort(): OK")
#     else:
#         print("radixsort(): ERROR")
        
# if __name__ == "__main__":
#     test_radixsort()

def test_radixsort():
    lista = [random.randint(10000, 99999) for _ in range(500)]
    esperado = sorted(lista)
    resultado = radixsort(lista.copy())
    #print(resultado)
    if resultado == esperado:
        print("radixsort(): OK")
    else:
        print("radixsort(): ERROR")
        
if __name__ == "__main__":
    test_radixsort()