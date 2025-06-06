# -*- coding: utf-8 -*-
"""
Sala de emergencias:
Simula un sistema de triaje donde los pacientes se atienden según su nivel de riesgo
(1: crítico, 2: moderado, 3: bajo), con timestamp como criterio secundario.
Código aportado por la cátedra, modificado por el alumno para adaptarlo a la práctica.
"""

import time
import datetime
import random
from modules.monticulo import MonticuloMinimo
import modules.paciente as pac

#primero comparamos pacientes por riesgo y timestamp
def comparar_pacientes(p1, p2):
    """Compara dos pacientes por riesgo y timestamp
        p1: Primer paciente.
        p2: Segundo paciente.
    """
    if p1.get_riesgo() != p2.get_riesgo():
        return p1.get_riesgo() - p2.get_riesgo()  # Menor riesgo = mayor prioridad
    return p1.get_timestamp() - p2.get_timestamp()  # Desempate por llegada!

# Crear el montículo con la función de comparación
cola_de_espera = MonticuloMinimo(comparar_pacientes)

# Número de ciclos de simulación
n = 20

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    # Insertar en el montículo
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: 50% de probabilidad y si hay pacientes
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        paciente_atendido = cola_de_espera.extraer_min()
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)
    #se elimina el else porque es redundante, ya que si no hay pacientes no se atiende a nadie
    # Mostrar pacientes en espera
    print('\nPacientes que faltan atenderse:', len(cola_de_espera))
    print('Lista de pacientes en espera:')
    cola_de_espera.mostrar()
    
    print('\n' + '-*-' * 15)
    
    time.sleep(1)