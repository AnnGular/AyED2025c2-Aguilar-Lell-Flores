#implementa un montículo binario eficiente para el algoritmo de Prim.
import math

class MonticuloBinario:
    """Define un montículo binario mínimo para organizar vértices según su distancia."""
    def __init__(self):
        self._lista_monticulo = [-math.inf]
        self._tamano_actual = 0
        self._indice_vertice = {}

    def _infilt_arriba(self, i):
        """Reorganiza el montículo hacia arriba para mantener la propiedad de heap."""
        while i // 2 > 0:
            if self._lista_monticulo[i].distancia < self._lista_monticulo[i // 2].distancia:
                self._indice_vertice[self._lista_monticulo[i]] = i // 2
                self._indice_vertice[self._lista_monticulo[i // 2]] = i
                self._lista_monticulo[i], self._lista_monticulo[i // 2] = self._lista_monticulo[i // 2], self._lista_monticulo[i]
            i = i // 2

    def insertar(self, vertice):
        """Inserta un vértice en el montículo."""
        self._lista_monticulo.append(vertice)
        self._tamano_actual += 1
        self._indice_vertice[vertice] = self._tamano_actual
        self._infilt_arriba(self._tamano_actual)

    def _infilt_abajo(self, i):
        """Reorganiza el montículo hacia abajo para mantener la propiedad de heap."""
        while (i * 2) <= self._tamano_actual:
            hm = self._hijo_min(i)
            if self._lista_monticulo[i].distancia > self._lista_monticulo[hm].distancia:
                self._indice_vertice[self._lista_monticulo[i]] = hm
                self._indice_vertice[self._lista_monticulo[hm]] = i
                self._lista_monticulo[i], self._lista_monticulo[hm] = self._lista_monticulo[hm], self._lista_monticulo[i]
            i = hm

    def _hijo_min(self, i):
        """Devuelve el índice del hijo con menor distancia."""
        if i * 2 + 1 > self._tamano_actual:
            return i * 2
        return i * 2 if self._lista_monticulo[i * 2].distancia < self._lista_monticulo[i * 2 + 1].distancia else i * 2 + 1

    def eliminar_min(self):
        """Elimina y devuelve el vértice con menor distancia."""
        if self.esta_vacio():
            raise ValueError("El montículo está vacío.")
        valor_sacado = self._lista_monticulo[1]
        self._lista_monticulo[1] = self._lista_monticulo[self._tamano_actual]
        self._indice_vertice[self._lista_monticulo[1]] = 1
        self._tamano_actual -= 1
        self._lista_monticulo.pop()
        del self._indice_vertice[valor_sacado]
        if self._tamano_actual > 0:
            self._infilt_abajo(1)
        return valor_sacado

    def construir_monticulo(self, lista):
        """Construye el montículo inicial a partir de una lista de vértices."""
        self._tamano_actual = len(lista)
        self._lista_monticulo = [0] + lista[:]
        for i, vertice in enumerate(lista, 1):
            self._indice_vertice[vertice] = i
        for i in range(self._tamano_actual // 2, 0, -1):
            self._infilt_abajo(i)

    def esta_vacio(self):
        """Verifica si el montículo está vacío."""
        return self._tamano_actual == 0

    def buscar_min(self):
        """Devuelve el vértice con menor distancia sin eliminarlo."""
        if self.esta_vacio():
            raise ValueError("El montículo está vacío.")
        return self._lista_monticulo[1]

    def tamano(self):
        """Devuelve el tamaño del montículo."""
        return self._tamano_actual

    def actualizar_distancia(self, vertice, nueva_distancia):
        """Actualiza la distancia de un vértice y ajusta su posición en el montículo."""
        if vertice not in self._indice_vertice:
            return
        i = self._indice_vertice[vertice]
        if self._lista_monticulo[i].distancia <= nueva_distancia:
            return
        self._lista_monticulo[i].distancia = nueva_distancia
        self._infilt_arriba(i)