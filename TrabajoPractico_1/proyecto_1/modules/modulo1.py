# modulo1.py

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)


def counting_sort(lista, exp):
    n = len(lista)
    salida = [0] * n
    cuenta = [0] * 10

    for i in range(n):
        indice = (lista[i] // exp) % 10
        cuenta[indice] += 1

    for i in range(1, 10):
        cuenta[i] += cuenta[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[cuenta[indice] - 1] = lista[i]
        cuenta[indice] -= 1
        i -= 1

    for i in range(n):
        lista[i] = salida[i]


def radixsort(lista):
    maximo = max(lista)
    exp = 1
    while maximo // exp > 0:
        counting_sort(lista, exp)
        exp *= 10
    return lista

