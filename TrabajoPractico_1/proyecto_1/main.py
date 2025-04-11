import time
import random
from modules.burbuja import burbuja
from modules.quicksort import quicksort
from modules.radixsort import radixsort
import matplotlib.pyplot as plt


tamaños = list(range(1, 1001))
tiempo_burbuja = []
tiempo_quicksort = []
tiempo_radixsort = []

for n in tamaños:
    lista = [random.randint(0, 10000) for _ in range(n)]

    # Burbuja
    lista_burbuja = lista.copy()
    inicio = time.time()
    burbuja(lista_burbuja)
    final = time.time()
    tiempo_burbuja=final - inicio

    # Quicksort
    lista_quick = lista.copy()
    inicio = time.time()
    quicksort(lista_quick)
    final = time.time()
    tiempo_quicksort=final - inicio

    # Radixsort
    lista_radix = lista.copy()
    inicio = time.time()
    radixsort(lista_radix)
    final = time.time()
    tiempo_radixsort=final - inicio
    
    if n == 1000:
        print(f"Tamaño: {n}, Tiempo Burbuja: {tiempo_burbuja:.6f} segundos")
        print(f"Tamaño: {n}, Tiempo Quicksort: {tiempo_quicksort:.6f} segundos")
        print(f"Tamaño: {n}, Tiempo RadixSort: {tiempo_radixsort:.6f} segundos")

#Graficas
# plt.plot(tamaños, tiempo_burbuja, label='Burbuja')
# plt.plot(tamaños, tiempo_quicksort, label='Quicksort')
# plt.plot(tamaños, tiempo_radixsort, label='Radixsort')
# plt.xlabel('Tamaño de la lista')
# plt.ylabel('Tiempo de ejecución (s)')
# plt.title('Comparación de algoritmos de ordenamiento')
# plt.legend()
# plt.grid(True)
# plt.show()



plt.figure(figsize=(10, 6))
plt.plot(tamaños, tiempo_burbuja, label='Burbuja', color='red')
plt.plot(tamaños, tiempo_quicksort, label='Quicksort', color='blue')
plt.plot(tamaños, tiempo_radixsort, label='Radixsort', color='green')

plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


















# from modules.modulo1 import burbuja, quicksort, radixsort
# import random

# def main():
 
#     lista_original = [random.randint(10000, 99999) for _ in range(10)]
    
#     print("Lista original:")
#     print(lista_original)

#     # Ordenar con Burbuja
#     lista_burbuja = lista_original.copy()
#     burbuja(lista_burbuja)
#     print("Lista ordenada con Burbuja:")
#     print(lista_burbuja)

#     # Ordenar con Quicksort
#     lista_quick = lista_original.copy()
#     lista_ordenada_quick = quicksort(lista_quick)
#     print("Lista ordenada con Quicksort:")
#     print(lista_ordenada_quick)

#     # Ordenar con Radixsort
#     lista_radix = lista_original.copy()
#     radixsort(lista_radix)
#     print("Lista ordenada con Radixsort:")
#     print(lista_radix)

#     # Ordenar con sorted() 
#     lista_sorted = sorted(lista_original)
#     print("Lista ordenada con sorted():")
#     print(lista_sorted)

# if __name__ == "__main__":
#     main()


#medicion de tempo