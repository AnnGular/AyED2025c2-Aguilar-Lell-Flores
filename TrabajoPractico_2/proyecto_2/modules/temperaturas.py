from modules.arbol import ArbolAVL
from datetime import datetime

class TemperaturasDB:
    #Base de datos para gestionar mediciones de temperatura usando un árbol AVL
    
    def __init__(self):
        """Inicializa una base de datos vacía con un árbol AVL."""
        self.arbol_avl = ArbolAVL()

    def _parse_fecha(self, fecha):
        """Convierte una fecha string a datetime"""
        try:
            return datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Formato de fecha inválido, debe ser dd/mm/aaaa")
    def guardar_temperatura(self, temperatura, fecha):
        #Guarda o actualiza una temperatura para una fecha específica. Temperatura: flotante, valor de la temperatura en °C; Fecha: en formato "dd/mm/aaaa".
        fecha_dt = self._parse_fecha(fecha)
        nodo = self.arbol_avl.buscar(fecha_dt)
        if nodo:
            nodo.valor = temperatura  # Actualizar temperatura existente
        else:
            self.arbol_avl.agregar(fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        #Devuelve la temperatura de una fecha específica.
        fecha_dt = self._parse_fecha(fecha)
        nodo = self.arbol_avl.buscar(fecha_dt)
        return nodo.valor if nodo else None

    def max_temp_rango(self, fecha1, fecha2):
        """Devuelve la temperatura máxima en un rango de fechas y corrobora si el formato de las fechas es correcto o si esta vacío.
            fecha1 fecha inicial
            fecha2 fecha final 
        """
        fecha1_dt = self._parse_fecha(fecha1)
        fecha2_dt = self._parse_fecha(fecha2)
        if fecha1_dt > fecha2_dt:
            raise ValueError("fecha1 debe ser menor o igual a fecha2")
        temperaturas = self._temperaturas_en_rango(fecha1_dt, fecha2_dt)
        return max(temperaturas) if temperaturas else None

    def min_temp_rango(self, fecha1, fecha2):
        """Devuelve la temperatura mínima en un rango de fechas y corrobora si el formato de las fechas es correcto o si esta vacío.
            fecha1 fecha inicial
            fecha2 fecha final 
        """
        fecha1_dt = self._parse_fecha(fecha1)
        fecha2_dt = self._parse_fecha(fecha2)
        if fecha1_dt > fecha2_dt:
            raise ValueError("fecha1 debe ser menor o igual a fecha2")
        temperaturas = self._temperaturas_en_rango(fecha1_dt, fecha2_dt)
        return min(temperaturas) if temperaturas else None

    def temp_extremos_rango(self, fecha1, fecha2):
        """Devuelve las temperaturas mínima y máxima en un rango de fechas y corrobora si el formato de las fechas es correcto o si esta vacío.
            fecha1 fecha inicial
            fecha2 fecha final 
        """
        fecha1_dt = self._parse_fecha(fecha1)
        fecha2_dt = self._parse_fecha(fecha2)
        if fecha1_dt > fecha2_dt:
            raise ValueError("fecha1 debe ser menor o igual a fecha2")
        temperaturas = self._temperaturas_en_rango(fecha1_dt, fecha2_dt)
        return (min(temperaturas), max(temperaturas)) if temperaturas else (None, None)

    def borrar_temperatura(self, fecha):
        #Elimina la medición de temperatura de una fecha específica.
        fecha_dt = self._parse_fecha(fecha)
        self.arbol_avl.eliminar(fecha_dt)

    def devolver_temperaturas(self, fecha1, fecha2):
        #Devuelve un listado de temperaturas en un rango, ordenado por fecha y corrobora si el formato de las fechas es correcto o si esta vacío.
        fecha1_dt = self._parse_fecha(fecha1)
        fecha2_dt = self._parse_fecha(fecha2)
        if fecha1_dt > fecha2_dt:
            raise ValueError("fecha1 debe ser menor o igual a fecha2")
        nodos = self._nodos_en_rango(fecha1_dt, fecha2_dt)
        return [f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.valor} ºC" for nodo in nodos]

    def cantidad_muestras(self):
        #Devuelve la cantidad de mediciones almacenadas.
        return self.arbol_avl.tamano

    def _temperaturas_en_rango(self, fecha1, fecha2):
        #Obtiene las temperaturas en un rango de fechas, inicial y final, y corrobora si el formato de las fechas es correcto o si esta vacío.
        nodos = self._nodos_en_rango(fecha1, fecha2)
        return [nodo.valor for nodo in nodos]

    def _nodos_en_rango(self, fecha1, fecha2):
        #Obtiene los nodos del árbol en un rango de fechas en una lista, ordenados por fecha.
        nodos = []
        self._recorrer_rango(self.arbol_avl.raiz, fecha1, fecha2, nodos)
        return nodos

    def _recorrer_rango(self, nodo, fecha1, fecha2, nodos):
        """Recorre el árbol para obtener nodos en un rango de fechas.
            nodo (NodoArbol): Nodo actual del árbol.
            fecha1 fecha inicial.
            fecha2 fecha final.
            nodos (list): Lista para almacenar los nodos en el rango.
        """
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