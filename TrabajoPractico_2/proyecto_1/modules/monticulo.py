class MonticuloMinimo:
    """Clase que implementa un montículo binario mínimo (min-heap) genérico. Permite almacenar elementos de cualquier tipo, priorizando el elemento con menor valor
    """
    
    def __init__(self, cmp_func=None):
        """Inicializa un montículo mínimo vacío. El objetivo aca es aceptar una función de comparación como parámetro
            cmp_func se usó como término genérico qque toma dos elementos
                y devuelve un entero negativo si el primero es menor, positivo si es mayor, o cero si son
                iguales. Si es None, se usa comparación por defecto (<, >, ==).
        """
        self.data = []  # Lista que contendrá los elementos del montículo
        self.cmp_func = cmp_func if cmp_func is not None else self.__default_cmp
    
    def __default_cmp(self, a, b):
        #Función de comparación por defecto para elementos comparables. a: primer elemento a comparar; b: segundo elemento a comparar.
       
        return -1 if a < b else 1 if a > b else 0
    
    def insertar(self, elemento):
        #Inserta un elemento en el montículo y mantiene la propiedad del min-heap.
        self.data.append(elemento)
        self.__ajustar_hacia_arriba(len(self.data) - 1)
    
    def extraer_min(self):
        #Extrae y devuelve el elemento con mayor prioridad (menor valor) del montículo.
        if len(self.data) == 0:
            return None
        
        # Intercambiamos el primer y último elemento
        self.__intercambiar(0, len(self.data) - 1)
        # Sacamos el elemento mínimo
        min_elemento = self.data.pop()
        # Ajustar hacia abajo si el montículo no está vacío
        if len(self.data) > 0:
            self.__ajustar_hacia_abajo(0)
        
        return min_elemento
    
    def peek(self):
        #Devuelve el elemento con mayor prioridad (menor valor) sin extraerlo.
        return self.data[0] if len(self.data) > 0 else None
    
    def esta_vacia(self):
        #Verifica si el montículo está vacío.
        return len(self.data) == 0
    
    def __ajustar_hacia_arriba(self, idx):
        #Ajusta un elemento hacia arriba para restaurar la propiedad del min-heap.
        padre_idx = (idx - 1) // 2 
        if idx > 0 and self.__comparar(self.data[idx], self.data[padre_idx]) < 0:
            self.__intercambiar(idx, padre_idx)
            self.__ajustar_hacia_arriba(padre_idx) 
    
    def __ajustar_hacia_abajo(self, idx):
        #Ajusta un elemento hacia abajo para restaurar la propiedad del min-heap.
        hijo_izq = 2 * idx + 1
        hijo_der = 2 * idx + 2
        menor_idx = idx

        # Comparar con el hijo izquierdo
        if hijo_izq < len(self.data) and self.__comparar(self.data[hijo_izq], self.data[menor_idx]) < 0:
            menor_idx = hijo_izq

        # Comparar con el hijo derecho
        if hijo_der < len(self.data) and self.__comparar(self.data[hijo_der], self.data[menor_idx]) < 0:
            menor_idx = hijo_der

        # Si el menor no es el elemento actual, intercambiamos y seguimos ajustando
        if menor_idx != idx:
            self.__intercambiar(idx, menor_idx)
            self.__ajustar_hacia_abajo(menor_idx)
    
    def __intercambiar(self, i, j):
        """Intercambia dos elementos en el montículo.
            i (int): Índice del primer elemento.
            j (int): Índice del segundo elemento.
        """
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def __comparar(self, elemento1, elemento2):
        """Compara dos elementos usando la función de comparación proporcionada.
            elemento1: Primer elemento a comparar.
            elemento2: Segundo elemento a comparar.
        """
        return self.cmp_func(elemento1, elemento2)
    
    def __len__(self):
        """Devuelve el número de elementos en el montículo.
        """
        return len(self.data)
    
    def mostrar(self):
        #Imprime todos los elementos del montículo en su orden actual.

        if len(self.data) == 0:
            print("Montículo vacío")
        else:
            for elemento in self.data:
                print(elemento)