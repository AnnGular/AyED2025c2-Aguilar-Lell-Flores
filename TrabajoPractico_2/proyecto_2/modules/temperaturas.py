from modules.arbol import ArbolAVL
from datetime import datetime

class TemperaturasDB:
    
    def __init__(self):
        
        self.arbol_avl = ArbolAVL()

    def guardar_temperatura(self, temperatura, fecha):
        # Convertir la fecha a datetime para usarla como clave
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.arbol_avl.agregar(fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        # Convertir la fecha a datetime
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self.arbol_avl.buscar(fecha_dt)
        if nodo:
            return nodo.valor
        return None

    def max_temp_rango(self, fecha1, fecha2):
        # Convertir las fechas a datetime
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self._temperaturas_en_rango(fecha1_dt, fecha2_dt)
        if temperaturas:
            return max(temperaturas)
        return None

    def min_temp_rango(self, fecha1, fecha2):
        # Convertir las fechas a datetime
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self._temperaturas_en_rango(fecha1_dt, fecha2_dt)
        if temperaturas:
            return min(temperaturas)
        return None

    def temp_extremos_rango(self, fecha1, fecha2):
        # Convertir las fechas a datetime
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self._temperaturas_en_rango(fecha1_dt, fecha2_dt)
        if temperaturas:
            return min(temperaturas), max(temperaturas)
        return None, None

    def borrar_temperatura(self, fecha):
        # Convertir la fecha a datetime
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.arbol_avl.eliminar(fecha_dt)

    def devolver_temperaturas(self, fecha1, fecha2):
        # Convertir las fechas a datetime
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        nodos = self._nodos_en_rango(fecha1_dt, fecha2_dt)
        return [f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.valor} ºC" for nodo in nodos]

    def cantidad_muestras(self):
        return self.arbol_avl.tamano
    
    # Métodos auxiliares para obtener las temperaturas en el rango dado.
    def _temperaturas_en_rango(self, fecha1, fecha2):
        nodos = self._nodos_en_rango(fecha1, fecha2)
        return [nodo.valor for nodo in nodos]

    def _nodos_en_rango(self, fecha1, fecha2):
        # Este método deberá recorrer el AVL y devolver los nodos dentro del rango
        nodos = []
        self._recorrer_rango(self.arbol_avl.raiz, fecha1, fecha2, nodos)
        return nodos

    def _recorrer_rango(self, nodo, fecha1, fecha2, nodos):
        if nodo is None:
            return
        if fecha1 <= nodo.clave <= fecha2:
            self._recorrer_rango(nodo.izquierdo, fecha1, fecha2, nodos)
            nodos.append(nodo)
            self._recorrer_rango(nodo.derecho, fecha1, fecha2, nodos)
        elif nodo.clave < fecha1:
            self._recorrer_rango(nodo.derecho, fecha1, fecha2, nodos)
        else:
            self._recorrer_rango(nodo.izquierdo, fecha1, fecha2, nodos)