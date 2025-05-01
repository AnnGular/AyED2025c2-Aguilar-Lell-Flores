from modules.listadoblementeenlazada import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception): #aqui se define la excepcion
    pass
class Mazo:
    def __init__(self):
        #Inicializa el mazo usando una lista doblemente enlazada (la que creamos)
        self.cartas = ListaDobleEnlazada()
        self.mazo = self

    def __len__(self):
        #Devuelve la cantidad de cartas que hay en el mazo
        return self.cartas.tamanio  

    def poner_carta_arriba(self, carta):
        #Agrega una carta la parte superior del mazo
        self.cartas.agregar_al_inicio(carta)  
    
    def poner_carta_abajo(self, carta):
        #Agrega una carta al final del mazo
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        #Saca la carta que está al inicio del mazo (parte superior)
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.extraer(0)  # Extrae la primera carta (al inicio)
        
        if mostrar:
            carta.visible = True  # Mostrar la carta si el argumento es True
            
        return carta  
#No colocamos un sacar_carta_abajo porque no tiene sentido en el juego de guerra, ya que no se puede sacar una carta del final del mazo
    def esta_vacio(self):
        #Devuelve True si el mazo está vacío, False si tiene cartas
        return len(self.cartas) == 0

    def tamanio(self):
        #Devuelve la cantidad de cartas que hay en el mazo
        return len(self.cartas)
            
#usaremos @property para conocer el estado del mazo (cabeza y cola)
    @property
    def cabeza(self):
        if self.cartas.cabeza:
            return self.cartas.cabeza.dato#devuelve la carta que está en la cabeza del mazo
        return None
    
    @property
    def cola(self):
        if self.cartas.cola:
            return self.cartas.cola.dato #devuelve la carta que está en la cola del mazo
        return None
