#DEFENSA TP

# from monticulo import MonticuloBinario

# class ColaDePrioridad:
#     def __init__(self):
#         self.monticulo = MonticuloBinario()
#         self.contador = 0

#     def encolar(self, prioridad, dato):
#         self.monticulo.insertar((prioridad, self.contador, dato))
#         self.contador += 1

#     def desencolar(self):
#         min_elem = self.monticulo.extraer_min()
#         return min_elem[2] if min_elem else None

#     def esta_vacia(self):
#         return self.monticulo.esta_vacia()

#     def obtener_todos(self):
#         return [elem[2] for elem in self.monticulo.data]
