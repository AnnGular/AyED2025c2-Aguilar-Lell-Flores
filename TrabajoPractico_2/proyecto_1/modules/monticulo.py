class MonticuloMinimo:
    def __init__(self):
        self.data = []  # Lista que contendrá los elementos del montículo
    
    def insertar(self, paciente):
        # Insertar el paciente en la última posición
        self.data.append(paciente)
        # Ajustar hacia arriba para restaurar la propiedad del montículo
        self.__ajustar_hacia_arriba(len(self.data) - 1) #haria las operaciones de infiltracion desde el ultimo elemento agregado hacia arriba, tantas veces como corresponda
    
    def extraer_min(self):
        if len(self.data) == 0:
            return None
        
        # Intercambiamos el primer y último elemento (mínimo y último)
        self.__intercambiar(0, len(self.data) - 1)
        # Sacamos el mínimo (que ahora está al final)
        min_paciente = self.data.pop()
        # Ajustar hacia abajo para restaurar la propiedad del montículo
        self.__ajustar_hacia_abajo(0)
        
        return min_paciente
    
    def __ajustar_hacia_arriba(self, idx):
        # Ajustamos el elemento hacia arriba si es menor que su padre
        padre_idx = (idx - 1) // 2
        if idx > 0 and self.__comparar(self.data[idx], self.data[padre_idx]) < 0:
            self.__intercambiar(idx, padre_idx)
            self.__ajustar_hacia_arriba(padre_idx)
    
    def __ajustar_hacia_abajo(self, idx):
        # Encontramos el índice de los hijos
        hijo_izq = 2 * idx + 1
        hijo_der = 2 * idx + 2
        menor_idx = idx

        # Comparar con el hijo izquierdo
        if hijo_izq < len(self.data) and self.__comparar(self.data[hijo_izq], self.data[menor_idx]) < 0:
            menor_idx = hijo_izq

        # Comparar con el hijo derecho
        if hijo_der < len(self.data) and self.__comparar(self.data[hijo_der], self.data[menor_idx]) < 0:
            menor_idx = hijo_der

        # Si el menor no es el padre, intercambiamos y ajustamos hacia abajo
        if menor_idx != idx:
            self.__intercambiar(idx, menor_idx)
            self.__ajustar_hacia_abajo(menor_idx)
    
    def __intercambiar(self, i, j):
        # Intercambiamos dos elementos en la lista
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def __comparar(self, paciente1, paciente2):
        # Primero convno tiene más prioridad)
        if paciente1.get_riesgo() != paciente2.get_riesgo():
            return paciente1.get_riesgo() - paciente2.get_riesgo()  # El menor riesgo tiene prioridad
        # Si los niveles de riesgo son iguales, comparamos por el timestamp (el que llegó antes tiene más prioridad)
        else:
            return paciente1.get_timestamp() - paciente2.get_timestamp()
    
    def __len__(self):
        return len(self.data)
    
    def mostrar(self):
        for paciente in self.data:
            print(paciente)
