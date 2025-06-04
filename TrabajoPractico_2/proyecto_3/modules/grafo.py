#proporciona la estructura para representar las aldeas y sus conexiones, y lee el archivo aldeas.txt.
import sys

class Vertice:
    """Define un vértice con conexiones a otros vértices y distancia inicial infinita."""
    def __init__(self, nombre):
        self._nombre = nombre
        self._conexiones = {}
        self._distancia = sys.maxsize
        self._predecesor = None

    def agregar_conexion(self, vertice, ponderacion):
        """Agrega una conexión a otro vértice con un peso."""
        self._conexiones[vertice] = ponderacion

    def obtener_conexiones(self):
        """Devuelve los vértices conectados."""
        return self._conexiones.keys()

    def obtener_ponderacion(self, vertice):
        """Devuelve el peso de la conexión a un vértice."""
        return self._conexiones[vertice]

    @property
    def distancia(self):
        """Obtiene la distancia del vértice."""
        return self._distancia

    @distancia.setter
    def distancia(self, dist):
        """Establece la distancia del vértice."""
        self._distancia = dist

    @property
    def predecesor(self):
        """Obtiene el predecesor del vértice."""
        return self._predecesor

    @predecesor.setter
    def predecesor(self, predecesor):
        """Establece el predecesor del vértice."""
        self._predecesor = predecesor

    def obtener_nombre(self):
        """Devuelve el nombre del vértice."""
        return self._nombre

class Grafo:
    """Define un grafo como un conjunto de vértices y aristas no dirigidas."""
    def __init__(self):
        self._vertices = {}

    def agregar_vertice(self, nombre):
        """Agrega un vértice al grafo."""
        vertice = Vertice(nombre)
        self._vertices[nombre] = vertice
        return vertice

    def obtener_vertice(self, nombre):
        """Obtiene un vértice por su nombre."""
        return self._vertices.get(nombre, None)

    def agregar_arista(self, desde, hasta, peso):
        """Agrega una arista bidireccional con un peso."""
        if desde not in self._vertices:
            self.agregar_vertice(desde)
        if hasta not in self._vertices:
            self.agregar_vertice(hasta)
        self._vertices[desde].agregar_conexion(self._vertices[hasta], peso)
        self._vertices[hasta].agregar_conexion(self._vertices[desde], peso)

def cargar_grafo(desde_archivo):
    """Carga un grafo desde un archivo donde cada línea representa una arista con peso."""
    grafo = Grafo()
    try:
        with open(desde_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(', ')
                if len(datos) != 3:
                    raise ValueError(f"Formato inválido en línea: {linea}")
                desde, hasta, distancia = datos
                try:
                    distancia = int(distancia)
                    if distancia <= 0:
                        raise ValueError(f"Distancia inválida en línea: {linea}")
                except ValueError:
                    raise ValueError(f"Distancia no es un entero positivo en línea: {linea}")
                grafo.agregar_arista(desde, hasta, distancia)
            if "Peligros" not in grafo._vertices:
                raise ValueError("La aldea Peligros no está en el grafo")
            if len(grafo._vertices) != 22:
                raise ValueError(f"El grafo debe contener 22 aldeas, pero tiene {len(grafo._vertices)}")
            if not grafo.obtener_vertice("Peligros").obtener_conexiones():
                raise ValueError("La aldea Peligros no tiene conexiones en el grafo")
            return grafo
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {desde_archivo} no se encuentra")