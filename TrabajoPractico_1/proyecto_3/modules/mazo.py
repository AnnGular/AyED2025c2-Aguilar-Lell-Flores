from modules.listadoblementeenlazada import ListaDobleEnlazada
from .carta import Carta

class DequeEmptyError(Exception):
    pass
class Mazo:
    def __init__(self):
        """Inicializa el mazo usando una lista doblemente enlazada."""
        self.cartas = ListaDobleEnlazada()
        self.mazo = self

    def __len__(self):
        """Devuelve la cantidad de cartas que hay en el mazo."""
        return self.cartas.tamanio  

    def poner_carta_arriba(self, carta):
        """Añade una carta al inicio del mazo (parte superior)."""
        self.cartas.agregar_al_inicio(carta)  
    
    def poner_carta_abajo(self, carta):
        """Añade una carta al final del mazo (parte inferior)."""
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Saca la carta que está al inicio del mazo (parte superior)."""
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.extraer(0)  # Extrae la primera carta (al inicio)
        
        if mostrar:
            carta.visible = True  # Mostrar la carta si el argumento es True
            
        return carta  

    def sacar_carta_abajo(self):
        """Saca la carta que está al final del mazo (parte inferior)."""
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")
        return self.cartas.extraer()  # Extrae la última carta (al final)

    def esta_vacio(self):
        """Devuelve True si el mazo está vacío, False si tiene cartas."""
        return len(self.cartas) == 0

    def tamanio(self):
        """Devuelve la cantidad de cartas que hay en el mazo."""
        return len(self.cartas)

    @property
    def cabeza(self):
        if self.cartas.cabeza:
            return self.cartas.cabeza.dato
        return None
    
    @property
    def cola(self):
        return self.cartas.cola
    
#mazo