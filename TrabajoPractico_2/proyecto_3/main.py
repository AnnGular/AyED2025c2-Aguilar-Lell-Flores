from modules.grafo import cargar_grafo
from modules.algoritmo_prim import prim, calcular_sumas_distancias

def mostrar_aldeas_alfabeticamente(grafo):
    """Muestra las aldeas del grafo en orden alfabético."""
    aldeas_ordenadas = sorted(grafo._vertices.keys())
    print("Lista de aldeas:")
    print(", ".join(aldeas_ordenadas))

def bea_propagacion(grafo, mst, inicio):
    """Muestra el flujo de mensajes en el MST, indicando quién recibe y envía mensajes."""
    hijos = {aldea: [] for aldea in mst}
    for aldea, predecesor in mst.items():
        if predecesor and aldea != inicio:
            hijos[predecesor.obtener_nombre()].append(aldea)
    
    if not hijos[inicio]:
        raise ValueError("Error: Peligros no envía a ninguna aldea. El MST puede ser incorrecto.")
    
    print("\nRutas de mensajes:")
    for aldea in sorted(mst.keys()):
        predecesor = "Ninguna" if aldea == inicio else mst[aldea].obtener_nombre() if mst[aldea] else "No conectada"
        print(f"{aldea}: Recibe de: {predecesor}, Envía a: {hijos[aldea]}")

def main():
    """Carga el grafo, calcula el MST, y muestra las aldeas, distancias y rutas de mensajes."""
    try:
        grafo = cargar_grafo("data/aldeas.txt")
        mostrar_aldeas_alfabeticamente(grafo)
        aldea_inicio = "Peligros"
        mst = prim(grafo, aldea_inicio)
        suma_distancias, total_suma = calcular_sumas_distancias(grafo, mst)
        print(f"\nDistancia total recorrida por palomas: {total_suma} leguas")
        bea_propagacion(grafo, mst, aldea_inicio)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()