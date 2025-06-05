# 🐍 Algoritmos TP

Breve descripción del proyecto:

Este proyecto presenta un sistema de triaje diseñado para optimizar la atención de pacientes en una sala de emergencias, implementado a través de una cola de prioridad basada en un montículo mínimo (min-heap). La estructura permite gestionar pacientes según su nivel de riesgo, priorizando a aquellos en estado crítico y respetando el orden de llegada en caso de empates.
---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)
Clases:
Paciente: Representa a cada paciente con sus atributos, como nombre y nivel de riesgo.
ColaPrioridad: Implementa la cola de prioridad utilizando un montículo mínimo para gestionar la atención de pacientes.
Funciones:
agregar_paciente(): Inserta un nuevo paciente en la cola.
atender_paciente(): Extrae el paciente con mayor prioridad.
simular_atencion(): Realiza la simulación del proceso de atención en la sala de emergencias.

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Flores Valentina
- Lell Camila Luciana
- Aguilar Gonzales Andrea Fernanda


---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
