class NodoDoble:
    def __init__(self, dato, anterior=None, siguiente=None):
        self._dato = dato
        self._anterior = anterior
        self._siguiente = siguiente

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, valor):
        self._dato = valor

    @property
    def anterior(self):
        return self._anterior

    @anterior.setter
    def anterior(self, nodo):
        self._anterior = nodo

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        self._siguiente = nodo


class ListaDobleEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamanio = 0

    @property
    def cabeza(self):
        return self._cabeza

    @cabeza.setter
    def cabeza(self, nodo):
        self._cabeza = nodo

    @property
    def cola(self):
        return self._cola

    @cola.setter
    def cola(self, nodo):
        self._cola = nodo

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor):
        self._tamanio = valor

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def esta_vacia(self):
        return self._tamanio == 0

    def __len__(self):
        return self._tamanio

    def agregar_al_inicio(self, item):
        nuevo = NodoDoble(item, None, self._cabeza)
        if self._cabeza:
            self._cabeza.anterior = nuevo
        else:
            self._cola = nuevo
        self._cabeza = nuevo
        self._tamanio += 1

    def agregar_al_final(self, item):
        nuevo = NodoDoble(item, self._cola, None)
        if self._cola:
            self._cola.siguiente = nuevo
        else:
            self._cabeza = nuevo
        self._cola = nuevo
        self._tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self._tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        if posicion == self._tamanio:
            self.agregar_al_final(item)
            return

        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nuevo = NodoDoble(item, actual.anterior, actual)
        if actual.anterior:
            actual.anterior.siguiente = nuevo
        actual.anterior = nuevo
        self._tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")

        if posicion is None or posicion == -1 or posicion == self._tamanio - 1:
            posicion = self._tamanio - 1

        if posicion < 0 or posicion >= self._tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            extraido = self._cabeza.dato
            self._cabeza = self._cabeza.siguiente
            if self._cabeza:
                self._cabeza.anterior = None
            else:
                self._cola = None
            self._tamanio -= 1
            return extraido

        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        extraido = actual.dato
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self._cola:
            self._cola = actual.anterior
        self._tamanio -= 1
        return extraido

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self._cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self._cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self._cabeza, self._cola = self._cola, self._cabeza

    def concatenar(self, otra_lista):
        copia = otra_lista.copiar()
        actual = copia.cabeza
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente

    def __add__(self, otra_lista):
        nueva = self.copiar()
        nueva.concatenar(otra_lista)
        return nueva

