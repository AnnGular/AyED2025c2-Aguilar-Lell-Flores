# modulos/cola_prioridad.py
import heapq

class ColaPrioridad:
    def __init__(self):
        self.heap = []
        self.contador = 0  # Para manejar orden de llegada

    def encolar(self, prioridad, dato):
        heapq.heappush(self.heap, (prioridad, self.contador, dato))
        self.contador += 1

    def desencolar(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        else:
            return None

    def esta_vacia(self):
        return len(self.heap) == 0

    def obtener_todos(self):
        # Retorna una lista ordenada sin alterar la cola original
        return sorted(self.heap)
