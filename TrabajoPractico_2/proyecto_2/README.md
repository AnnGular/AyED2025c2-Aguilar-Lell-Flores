# 🐍 Algoritmos TP

Breve descripción del proyecto:

Este proyecto consiste en el diseño de una base de datos para almacenar mediciones de temperatura asociadas a fechas, utilizando un Árbol AVL. Esta estructura jerárquica garantiza que los datos se mantengan ordenados y balanceados, lo que permite realizar búsquedas y consultas por rangos de manera eficiente.

---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)
Clases:

AVL: Implementa el árbol AVL para mantener datos ordenados y balanceados.
Nodo: Representa cada nodo con una fecha y una temperatura.
Funciones:
guardar_temperatura(), devolver_temperatura(), borrar_temperatura(): Manejan inserciones, búsquedas y eliminaciones.
max_temp_rango(), min_temp_rango(), temp_extremos_rango(): Consultas de temperaturas en rangos.
devolver_temperaturas(), cantidad_muestras(): Listados y conteos de mediciones.

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
