from random import randint, choices
import time
import datetime

# Listas de nombres y apellidos para generar pacientes con datos más reales
nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

# Niveles de riesgo posibles
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']

# Probabilidades de aparición de cada tipo de paciente (más probables los de riesgo bajo)
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        # Se elige un nombre y apellido aleatorio de las listas
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        # Se asigna el nivel de riesgo con las probabilidades dadas (0.1, 0.3, 0.6)
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        # Se asigna la descripción textual según el riesgo asignado (1->crítico, etc.)
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        # Se almacena el momento exacto de ingreso usando timestamp (número flotante de segundos desde 1970)
        self.__timestamp = time.time()  

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_timestamp(self):
        return self.__timestamp
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        # Convierte el timestamp a hora legible (solo muestra hora, minutos y segundos)
        hora_ingreso = datetime.datetime.fromtimestamp(self.__timestamp).strftime('%H:%M:%S')  

        # Devuelve una cadena con todos los datos importantes del paciente
        cad = f"{self.__nombre} {self.__apellido}\t -> {self.__riesgo} - {self.__descripcion} {hora_ingreso} "
        return cad
