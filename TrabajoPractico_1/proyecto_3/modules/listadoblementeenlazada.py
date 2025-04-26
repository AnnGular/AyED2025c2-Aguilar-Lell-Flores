class Nodo:
    # Esta clase representa un nodo individual de la lista doblemente enlazada
    def __init__(self, dato):
        self.dato = dato            # El dato almacenado en este nodo
        self.siguiente = None       # El puntero al nodo siguiente (inicialmente None)
        self.anterior = None        # El puntero al nodo anterior (inicialmente None)


class ListaDobleEnlazada:
    # Esta clase define la lista doblemente enlazada con las operaciones solicitadas
    def __init__(self):
        self.cabeza = None          # La cabeza de la lista (primer nodo)
        self.cola = None            # La cola de la lista (último nodo)
        self.tamanio = 0            # El tamaño actual de la lista

    def esta_vacia(self):
        # Devuelve True si la lista está vacía
        return self.tamanio == 0

    def __len__(self):
        # Devuelve el número de elementos en la lista
        return self.tamanio

    def agregar_al_inicio(self, item):
        # Crea un nuevo nodo y lo agrega al inicio de la lista
        nuevo_nodo = Nodo(item)    # Creamos un nuevo nodo con el dato 'item'

        if self.esta_vacia():
            # Si la lista está vacía, el nuevo nodo es tanto la cabeza como la cola
            self.cabeza = self.cola = nuevo_nodo
        else:
            # Si la lista no está vacía, el nuevo nodo apunta a la actual cabeza
            nuevo_nodo.siguiente = self.cabeza
            # La actual cabeza debe apuntar hacia atrás, hacia el nuevo nodo
            self.cabeza.anterior = nuevo_nodo
            # Actualizamos la cabeza de la lista para que sea el nuevo nodo
            self.cabeza = nuevo_nodo
        if self.cabeza:
                        self.cabeza.anterior = None
        # Incrementamos el tamaño de la lista
        self.tamanio += 1

    def agregar_al_final(self, item):
        # Crea un nuevo nodo y lo agrega al final de la lista
        nuevo_nodo = Nodo(item)    # Creamos un nuevo nodo con el dato 'item'

        if self.esta_vacia():
            # Si la lista está vacía, el nuevo nodo es tanto la cabeza como la cola
            self.cabeza = self.cola = nuevo_nodo
        else:
            # Si la lista no está vacía, el nuevo nodo apunta hacia atrás, a la cola actual
            nuevo_nodo.anterior = self.cola
            # La cola actual debe apuntar hacia adelante, al nuevo nodo
            self.cola.siguiente = nuevo_nodo
            # Actualizamos la cola de la lista para que sea el nuevo nodo
            self.cola = nuevo_nodo
        if self.cabeza:
                        self.cabeza.anterior = None
        # Incrementamos el tamaño de la lista
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        # Inserta un nuevo nodo en la posición indicada o al final si no se pasa la posición
        if posicion is None:
            # Si no se indica una posición, lo agregamos al final
            self.agregar_al_final(item)
            return
        
        # Comprobamos que la posición es válida
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")

        # Insertamos en la posición 0 (al inicio)
        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        # Insertamos en la posición final (igual que agregar al final)
        if posicion == self.tamanio:
            self.agregar_al_final(item)
            return
        
        # Insertamos en una posición intermedia
        nuevo_nodo = Nodo(item)    # Creamos el nuevo nodo
        actual = self.cabeza       # Empezamos desde la cabeza

        # Recorremos la lista hasta encontrar la posición anterior a donde insertar
        for _ in range(posicion - 1):
            actual = actual.siguiente
        
        # Ajustamos los punteros del nuevo nodo y los nodos vecinos
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo
        if self.cabeza:
                        self.cabeza.anterior = None
        # Incrementamos el tamaño de la lista
        self.tamanio += 1
    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("La lista está vacía")

        # Si la posición es None, eliminamos el último nodo
        if posicion is None:
            posicion = self.tamanio - 1

        # Manejar posiciones negativas
        if posicion < 0:
            posicion = self.tamanio + posicion

        # Comprobamos si la posición es válida
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")

        # Extraer el primer nodo (la cabeza) en O(1)
        if posicion == 0:
            valor = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        # Extraer el último nodo (la cola) en O(1)
        elif posicion == self.tamanio - 1:
            valor = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        # Extraer un nodo en una posición intermedia en O(n), optimizado
        else:
            if posicion < self.tamanio // 2:
                # Recorrer desde la cabeza si la posición está más cerca de la cabeza
                actual = self.cabeza
                for _ in range(posicion):
                    actual = actual.siguiente
            else:
                # Recorrer desde la cola si la posición está más cerca de la cola
                actual = self.cola
                for _ in range(self.tamanio - 1, posicion, -1):
                    actual = actual.anterior

            valor = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        # Reducimos el tamaño de la lista
        self.tamanio -= 1
        return valor



    def copiar(self):
        # Devuelve una nueva lista que es una copia de la lista actual
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        
        # Recorremos la lista actual y agregamos los elementos a la nueva lista
        while actual:
            nueva_lista.agregar_al_final(actual.dato)  # Esta operación es O(1)
            actual = actual.siguiente
        
        return nueva_lista


    def invertir(self):
        # Invierte el orden de los nodos en la lista
        actual = self.cabeza
        
        # Recorremos la lista y cambiamos los punteros 'siguiente' y 'anterior' de cada nodo
        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior #se actualiza a actual.anterior en la iteracion ya que la variable se re asigna en la linea anterior
        
        # Intercambiamos la cabeza y la cola
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista):
        if otra_lista.esta_vacia():
            return  # Si la otra lista está vacía, no hay nada que hacer

        if self.esta_vacia():
            # Si la lista actual está vacía, simplemente hacemos que apunte a la otra lista
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
        else:
            # Conectamos la cola de la lista actual con la cabeza de la otra lista
            self.cola.siguiente = otra_lista.cabeza
            if otra_lista.cabeza:
                otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola

        # Aseguramos que la cabeza de la lista concatenada (self) no tenga un nodo anterior
        if self.cabeza:
            self.cabeza.anterior = None   # Esto asegura que la cabeza de la lista tenga `anterior = None`

        # Aseguramos que la cabeza de la otra lista también tenga `anterior = None`
        if otra_lista.cabeza:
            otra_lista.cabeza.anterior = None

        self.tamanio += len(otra_lista)  # Actualizamos el tamaño de la lista



    
    
    def __add__(self, otra_lista):
        #El elemento anterior a la cabeza de la lista debe ser None
        nueva_lista = self.copiar()  # Creamos una copia de la lista actual
        nueva_lista.concatenar(otra_lista)  # Concatenamos la 'otra_lista'
        return nueva_lista  # Devolvemos la nueva lista con los elementos de ambas listas
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
