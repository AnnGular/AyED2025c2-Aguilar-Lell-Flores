# 🐍 Algoritmos TP

Breve descripción del proyecto:

Este proyecto aborda el envío eficiente de mensajes entre aldeas utilizando palomas mensajeras, modelando la situación como un grafo no dirigido y ponderado. Cada aldea se representa como un vértice y los caminos entre ellas como aristas con distancias como peso. Se implementó el algoritmo de Prim para construir un Árbol de Expansión Mínima (MST), asegurando que todas las aldeas estén conectadas con la menor distancia total y evitando duplicaciones en la propagación del mensaje.

---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)
Clases:
Grafo: Representa aldeas y conexiones.
Vertice: Modela cada aldea y sus conexiones.
MonticuloBinario: Optimiza el algoritmo de Prim.
Funciones:
prim(): Genera el Árbol de Expansión Mínima (MST).
calcular_sumas_distancias(): Calcula el costo total del mensaje.
bea_propagacion(), mostrar_aldeas_alfabeticamente(): Manejan la propagación del mensaje y visualización de aldeas.

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
.

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
