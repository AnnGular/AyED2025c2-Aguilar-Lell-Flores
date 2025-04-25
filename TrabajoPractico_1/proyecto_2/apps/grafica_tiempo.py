import time
import matplotlib.pyplot as plt
from modules.lista_doble import ListaDobleEnlazada
from random import randint

# Listas para los resultados
tamaños = list(range(10, 1001, 60)) 
#tamaños = [for _ in range(10, 1001, 50)]
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in tamaños:
    lista = ListaDobleEnlazada()
    for i in range(n):
        lista.agregar_al_final(randint(0, 1000))

    # Medir len()
    inicio = time.perf_counter()
    _ = len(lista) #como no nos importa el valor asignado, entonces colocamos _
    fin = time.perf_counter()
    tiempos_len.append(fin - inicio)

    # Medir copiar()
    inicio = time.perf_counter()
    copia = lista.copiar()
    fin = time.perf_counter()
    tiempos_copiar.append(fin - inicio)

    # Medir invertir()
    inicio = time.perf_counter()
    lista.invertir()
    fin = time.perf_counter()
    tiempos_invertir.append(fin - inicio)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(tamaños, tiempos_len, label="len()", color="blue")
plt.plot(tamaños, tiempos_copiar, label="copiar()", color="green")
plt.plot(tamaños, tiempos_invertir, label="invertir()", color="red")
plt.xlabel("Cantidad de elementos (N)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Rendimiento de métodos de ListaDobleEnlazada")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
