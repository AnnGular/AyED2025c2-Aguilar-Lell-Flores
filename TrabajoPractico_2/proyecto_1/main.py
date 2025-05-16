# -*- coding: utf-8 -*-
"""
Sala de emergencias usando cola de prioridad (Montículo de Mínimos adaptado al paciente.py real)
"""

import time
import datetime
import random
from modules.cola_de_prioridad import ColaPrioridad
import modules.paciente as pac

n = 20  # cantidad de ciclos de simulación

# Se crea una cola de prioridad genérica
cola_de_espera = ColaPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un nuevo paciente con datos reales y timestamp
    paciente = pac.Paciente()
    # Encolamos usando riesgo como prioridad principal, y timestamp como criterio secundario
    cola_de_espera.encolar((paciente.get_riesgo(), paciente.get_timestamp()), paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos y si hay pacientes en espera
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        paciente_atendido = cola_de_espera.desencolar()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        pass  # No se atiende paciente en este ciclo

    print()
    print('Pacientes que faltan atenderse:', len(cola_de_espera.heap))
    for item in cola_de_espera.obtener_todos():
        print('\t', item[2])  # Mostramos solo el paciente
    
    print()
    print('-*-'*15)
    
    time.sleep(1)
