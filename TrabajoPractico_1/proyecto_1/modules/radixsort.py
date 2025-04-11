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