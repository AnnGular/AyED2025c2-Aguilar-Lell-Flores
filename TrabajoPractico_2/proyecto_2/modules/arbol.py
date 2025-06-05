class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self._clave = clave
        self._valor = valor
        self._izquierdo = izquierdo
        self._derecho = derecho
        self._padre = padre
        self._factor_equilibrio = 0

    # Propiedades de acceso
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        self._clave = valor


    @property
    def izquierdo(self):
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo):
        self._izquierdo = nodo

    @property
    def derecho(self):
        return self._derecho

    @derecho.setter
    def derecho(self, nodo):
        self._derecho = nodo

    @property
    def padre(self):
        return self._padre

    @padre.setter
    def padre(self, nodo):
        self._padre = nodo

    @property
    def factor_equilibrio(self):
        return self._factor_equilibrio

    @factor_equilibrio.setter
    def factor_equilibrio(self, valor):
        self._factor_equilibrio = valor

    # Métodos de verificación de relaciones
    def tiene_hijo_izquierdo(self):
        return self.izquierdo is not None

    def tiene_hijo_derecho(self):
        return self.derecho is not None

    def es_hijo_izquierdo(self):
        return self.padre and self.padre.izquierdo == self

    def es_hijo_derecho(self):
        return self.padre and self.padre.derecho == self

    def es_raiz(self):
        return self.padre is None

    def es_hoja(self):
        return not (self.derecho or self.izquierdo)

    def tiene_alguno_hijo(self):
        return self.derecho or self.izquierdo

    def tiene_ambos_hijos(self):
        return self.derecho and self.izquierdo

    # Método para reemplazar datos de un nodo
    def reemplazar_datos(self, clave, valor, izquierdo, derecho):
        self.clave = clave
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
        if self.tiene_hijo_izquierdo():
            self.izquierdo.padre = self
        if self.tiene_hijo_derecho():
            self.derecho.padre = self


class ArbolAVL:
    def __init__(self):
        self._raiz = None
        self._tamano = 0

    # Propiedades de acceso para raíz y tamaño
    @property
    def raiz(self):
        return self._raiz

    @raiz.setter
    def raiz(self, nodo):
        self._raiz = nodo

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, valor):
        self._tamano = valor

    # Métodos de agregar
    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano += 1

    def _agregar(self, clave, valor, nodo_actual):
        if clave < nodo_actual.clave:
            if nodo_actual.tiene_hijo_izquierdo():
                self._agregar(clave, valor, nodo_actual.izquierdo)
            else:
                nodo_actual.izquierdo = NodoArbol(clave, valor, padre=nodo_actual)
                self.actualizar_equilibrio(nodo_actual.izquierdo)
        else:
            if nodo_actual.tiene_hijo_derecho():
                self._agregar(clave, valor, nodo_actual.derecho)
            else:
                nodo_actual.derecho = NodoArbol(clave, valor, padre=nodo_actual)
                self.actualizar_equilibrio(nodo_actual.derecho)

    # Métodos de búsqueda
    def buscar(self, clave):
        return self._buscar(clave, self.raiz)

    def _buscar(self, clave, nodo):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar(clave, nodo.izquierdo)
        else:
            return self._buscar(clave, nodo.derecho)

    # Métodos de eliminación
    def eliminar(self, clave):
        nodo_eliminado = self._eliminar(clave, self.raiz)
        if nodo_eliminado is not None:
            self.tamano -= 1

    def _eliminar(self, clave, nodo):
        if nodo is None:
            return None
        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar(clave, nodo.izquierdo)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar(clave, nodo.derecho)
        else:
            if nodo.tiene_ambos_hijos():
                sucesor = self._minimo(nodo.derecho)
                nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
                nodo.derecho = self._eliminar(sucesor.clave, nodo.derecho)
            else:
                nodo = nodo.izquierdo if nodo.tiene_hijo_izquierdo() else nodo.derecho
        if nodo is None:
            return None
        self.actualizar_equilibrio_post_eliminacion(nodo)
        return nodo

    def _minimo(self, nodo):
        if nodo is None or nodo.izquierdo is None:
            return nodo
        return self._minimo(nodo.izquierdo)

    # Métodos de balanceo
    def actualizar_equilibrio(self, nodo):
        if nodo.factor_equilibrio > 1 or nodo.factor_equilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.es_hijo_izquierdo():
                nodo.padre.factor_equilibrio += 1
            elif nodo.es_hijo_derecho():
                nodo.padre.factor_equilibrio -= 1
            if nodo.padre.factor_equilibrio != 0:
                self.actualizar_equilibrio(nodo.padre)

    def actualizar_equilibrio_post_eliminacion(self, nodo):
        if nodo.factor_equilibrio > 1 or nodo.factor_equilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.es_hijo_izquierdo():
                nodo.padre.factor_equilibrio -= 1
            elif nodo.es_hijo_derecho():
                nodo.padre.factor_equilibrio += 1
            if nodo.padre.factor_equilibrio != 0:
                self.actualizar_equilibrio_post_eliminacion(nodo.padre)

    # Rotaciones
    def rotar_izquierda(self, rot_raiz):
        nueva_raiz = rot_raiz.derecho
        rot_raiz.derecho = nueva_raiz.izquierdo
        if nueva_raiz.izquierdo:
            nueva_raiz.izquierdo.padre = rot_raiz
        nueva_raiz.padre = rot_raiz.padre
        if rot_raiz.es_raiz():
            self.raiz = nueva_raiz
        else:
            if rot_raiz.es_hijo_izquierdo():
                rot_raiz.padre.izquierdo = nueva_raiz
            else:
                rot_raiz.padre.derecho = nueva_raiz
        nueva_raiz.izquierdo = rot_raiz
        rot_raiz.padre = nueva_raiz
        rot_raiz.factor_equilibrio += 1 - min(nueva_raiz.factor_equilibrio, 0)
        nueva_raiz.factor_equilibrio += 1 + max(rot_raiz.factor_equilibrio, 0)

    def rotar_derecha(self, rot_raiz):
        nueva_raiz = rot_raiz.izquierdo
        rot_raiz.izquierdo = nueva_raiz.derecho
        if nueva_raiz.derecho:
            nueva_raiz.derecho.padre = rot_raiz
        nueva_raiz.padre = rot_raiz.padre
        if rot_raiz.es_raiz():
            self.raiz = nueva_raiz
        else:
            if rot_raiz.es_hijo_derecho():
                rot_raiz.padre.derecho = nueva_raiz
            else:
                rot_raiz.padre.izquierdo = nueva_raiz
        nueva_raiz.derecho = rot_raiz
        rot_raiz.padre = nueva_raiz
        rot_raiz.factor_equilibrio -= 1 + max(nueva_raiz.factor_equilibrio, 0)
        nueva_raiz.factor_equilibrio -= 1 + min(rot_raiz.factor_equilibrio, 0)

    # Reequilibración
    def reequilibrar(self, nodo):
        if nodo.factor_equilibrio < 0:
            if nodo.derecho and nodo.derecho.factor_equilibrio > 0:
                self.rotar_derecha(nodo.derecho)
            self.rotar_izquierda(nodo)
        elif nodo.factor_equilibrio > 0:
            if nodo.izquierdo and nodo.izquierdo.factor_equilibrio < 0:
                self.rotar_izquierda(nodo.izquierdo)
            self.rotar_derecha(nodo)
