class NodoDoble: #el nodo de la lista doblemente enlazada, que guarda el dato y referencias del nodo anterior y siguiente
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

class ListaDobleEnlazada: #crea una lista con un principio y final, es una lista de tamaño 0 principalmente
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        
    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def esta_vacia(self): #corrobora si està vacia #corrobora si el mazo se quedó sin cartas
        return self.tamanio == 0

    def __len__(self): #devuelve el tamaño #podría darnos el tamaño del mazo
        return self.tamanio

    def agregar_al_inicio(self, item): #Agregaría cartas al inicio del mazo
        nuevo = NodoDoble(item, None, self.cabeza)
        if self.cabeza:
            self.cabeza.anterior = nuevo
        else:
            self.cola = nuevo
        self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, item):#agregaría cartas al final del mazo
        nuevo = NodoDoble(item, self.cola, None)
        if self.cola:
            self.cola.siguiente = nuevo
        else:
            self.cabeza = nuevo
        self.cola = nuevo
        self.tamanio += 1

    def insertar(self, item, posicion=None): #inserta una carta en una posición específica del mazo
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        if posicion == self.tamanio:
            self.agregar_al_final(item)
            return

        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nuevo = NodoDoble(item, actual.anterior, actual)
        if actual.anterior:
            actual.anterior.siguiente = nuevo
        actual.anterior = nuevo
        self.tamanio += 1

    def extraer(self, posicion=None): #extrae una carta de la posición indicada, si no se indica, extrae la última carta del mazo
        # Si la lista está vacía entonces no se puede extraer nada
        if self.esta_vacia():
            raise Exception("Lista vacía")

        if posicion is None or posicion == -1 or posicion == self.tamanio - 1: #para poder aceptar cualquier índicde, incluyendo los negativos
            posicion = self.tamanio - 1

        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            extraido = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return extraido

        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        extraido = actual.dato
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self.cola:
            self.cola = actual.anterior
        self.tamanio -= 1
        return extraido

    def copiar(self): #devuelve una copia de la lista, para no modificar el mazo original
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self): #invierte el orden de las cartas en el mazo, aunque no sabemos si es necesario
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista): #concatena dos listas, para poder unir dos mazos, si se quiere
        copia = otra_lista.copiar()
        actual = copia.cabeza
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente

    def __add__(self, otra_lista): #permite sumar dos listas, para poder unir dos mazos, repito, si se quiere
        nueva = self.copiar()
        nueva.concatenar(otra_lista)
        return nueva
