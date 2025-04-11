from modules.modulo1 import burbuja, quicksort, radixsort
import random

def main():
 
    lista_original = [random.randint(10000, 99999) for _ in range(10)]
    
    print("Lista original:")
    print(lista_original)

    # Ordenar con Burbuja
    lista_burbuja = lista_original.copy()
    burbuja(lista_burbuja)
    print("Lista ordenada con Burbuja:")
    print(lista_burbuja)

    # Ordenar con Quicksort
    lista_quick = lista_original.copy()
    lista_ordenada_quick = quicksort(lista_quick)
    print("Lista ordenada con Quicksort:")
    print(lista_ordenada_quick)

    # Ordenar con Radixsort
    lista_radix = lista_original.copy()
    radixsort(lista_radix)
    print("Lista ordenada con Radixsort:")
    print(lista_radix)

    # Ordenar con sorted() 
    lista_sorted = sorted(lista_original)
    print("Lista ordenada con sorted():")
    print(lista_sorted)

if __name__ == "__main__":
    main()


