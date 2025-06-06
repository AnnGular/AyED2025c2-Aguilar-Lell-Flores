class NodoArbol:
    #Nodo de un árbol AVL, almacena clave, valor y relaciones con otros nodos.

    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        """Inicializa un nodo con clave, valor y referencias.
            clave: Clave del nodo.
            valor: Valor asociado.
            izquierdo (NodoArbol): Hijo izquierdo.
            derecho (NodoArbol): Hijo derecho.
            padre (NodoArbol): Nodo padre.
        """
        self._clave = clave
        self._valor = valor
        self._izquierdo = izquierdo
        self._derecho = derecho
        self._padre = padre
        self._factor_equilibrio = 0

    @property
    def valor(self):
        """Obtiene el valor del nodo."""
        return self._valor

    @valor.setter
    def valor(self, valor):
        """Establece el valor del nodo."""
        self._valor = valor

    @property
    def clave(self):
        """Obtiene la clave del nodo."""
        return self._clave

    @clave.setter
    def clave(self, valor):
        """Establece la clave del nodo."""
        self._clave = valor

    @property
    def izquierdo(self):
        """Obtiene el hijo izquierdo."""
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo):
        """Establece el hijo izquierdo."""
        self._izquierdo = nodo

    @property
    def derecho(self):
        """Obtiene el hijo derecho."""
        return self._derecho

    @derecho.setter
    def derecho(self, nodo):
        """Establece el hijo derecho."""
        self._derecho = nodo

    @property
    def padre(self):
        """Obtiene el nodo padre."""
        return self._padre

    @padre.setter
    def padre(self, nodo):
        """Establece el nodo padre."""
        self._padre = nodo

    @property
    def factor_equilibrio(self):
        """Obtiene el factor de equilibrio."""
        return self._factor_equilibrio

    @factor_equilibrio.setter
    def factor_equilibrio(self, valor):
        """Establece el factor de equilibrio."""
        self._factor_equilibrio = valor

    def tiene_hijo_izquierdo(self):
        """Verifica si tiene hijo izquierdo."""
        return self.izquierdo is not None

    def tiene_hijo_derecho(self):
        """Verifica si tiene hijo derecho."""
        return self.derecho is not None

    def es_hijo_izquierdo(self):
        """Verifica si es hijo izquierdo de su padre."""
        return self.padre and self.padre.izquierdo == self

    def es_hijo_derecho(self):
        """Verifica si es hijo derecho de su padre."""
        return self.padre and self.padre.derecho == self

    def es_raiz(self):
        """Verifica si es la raíz del árbol."""
        return self.padre is None

    def es_hoja(self):
        """Verifica si es una hoja (sin hijos)."""
        return not (self.derecho or self.izquierdo)

    def tiene_alguno_hijo(self):
        """Verifica si tiene al menos un hijo."""
        return self.derecho or self.izquierdo

    def tiene_ambos_hijos(self):
        """Verifica si tiene ambos hijos."""
        return self.derecho and self.izquierdo

    def reemplazar_datos(self, clave, valor, izquierdo, derecho):
        """Reemplaza los datos del nodo.
            clave: Nueva clave.
            valor: Nuevo valor.
            izquierdo (NodoArbol): Nuevo hijo izquierdo.
            derecho (NodoArbol): Nuevo hijo derecho.
        """
        self.clave = clave
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
        if self.tiene_hijo_izquierdo():
            self.izquierdo.padre = self
        if self.tiene_hijo_derecho():
            self.derecho.padre = self


class ArbolAVL:
    """Árbol AVL balanceado para almacenar pares clave-valor."""

    def __init__(self):
        """Inicializa un árbol AVL vacío."""
        self._raiz = None
        self._tamano = 0

    @property
    def raiz(self):
        """Obtiene la raíz del árbol."""
        return self._raiz

    @raiz.setter
    def raiz(self, nodo):
        """Establece la raíz del árbol."""
        self._raiz = nodo

    @property
    def tamano(self):
        """Obtiene el número de nodos en el árbol."""
        return self._tamano

    @tamano.setter
    def tamano(self, valor):
        """Establece el número de nodos."""
        self._tamano = valor

    def agregar(self, clave, valor):
        """Inserta un nodo con la clave y valor dados.
            clave: Clave del nodo
            valor: Valor asociado.
        """
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano += 1

    def _agregar(self, clave, valor, nodo_actual):
        """Inserta recursivamente un nodo.
            clave: Clave del nodo.
            valor: Valor asociado.
            nodo_actual (NodoArbol): Nodo actual en la recursión.
        """
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

    def buscar(self, clave):
        """Busca un nodo por su clave"""
        return self._buscar(clave, self.raiz)

    def _buscar(self, clave, nodo):
        """Busca recursivamente un nodo"""
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar(clave, nodo.izquierdo)
        else:
            return self._buscar(clave, nodo.derecho)

    def eliminar(self, clave):
        """Elimina un nodo por su clave"""
        nodo_eliminado = self._eliminar(clave, self.raiz)
        if nodo_eliminado is not None:
            self.tamano -= 1

    def _eliminar(self, clave, nodo):
        """Elimina recursivamente un nodo, clave es la clave del nodo a eliminar"""
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
        """Encuentra el nodo con la clave mínima en un subárbol."""
        if nodo is None or nodo.izquierdo is None:
            return nodo
        return self._minimo(nodo.izquierdo)

    def actualizar_equilibrio(self, nodo):
        """Actualiza el factor de equilibrio tras una inserción"""
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
        """Actualiza el factor de equilibrio tras una eliminación"""
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

    def rotar_izquierda(self, rot_raiz):
        """Realiza una rotación izquierda """
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
        """Realiza una rotación derecha """
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

    def reequilibrar(self, nodo):
        """Reequilibra el árbol en un nodo desbalanceado."""
        if nodo.factor_equilibrio < 0:
            if nodo.derecho and nodo.derecho.factor_equilibrio > 0:
                self.rotar_derecha(nodo.derecho)
            self.rotar_izquierda(nodo)
        elif nodo.factor_equilibrio > 0:
            if nodo.izquierdo and nodo.izquierdo.factor_equilibrio < 0:
                self.rotar_izquierda(nodo.izquierdo)
            self.rotar_derecha(nodo)