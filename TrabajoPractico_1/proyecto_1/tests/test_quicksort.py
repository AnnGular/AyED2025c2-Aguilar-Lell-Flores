from modules.quicksort import quicksort
import random

# def test_quicksort():
#     lista = [5, 3, 1, 4, 2]
#     esperado = [1, 2, 3, 4, 5]
#     resultado = quicksort(lista.copy())
#     if resultado == esperado:
#         print("quicksort(): OK")
#     else:
#         print("quicksort(): ERROR")
        
# if __name__ == "__main__":
#     test_quicksort()

def test_quicksort():
    lista = [random.randint(10000, 99999) for _ in range(500)]
    esperado = sorted(lista)
    resultado = quicksort(lista.copy())
    #print(resultado)
    if resultado == esperado:
        print("quicksort(): OK")
    else:
        print("quicksort(): ERROR")
        
if __name__ == "__main__":
    test_quicksort()