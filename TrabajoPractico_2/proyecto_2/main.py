from modules.temperaturas import TemperaturasDB

def main():
    # Crear una instancia de la base de datos de temperaturas
    db = TemperaturasDB()

    # Guardar algunas temperaturas
    db.guardar_temperatura(25.5, "01/01/2024")
    db.guardar_temperatura(30.2, "02/01/2024")
    db.guardar_temperatura(15.8, "03/01/2024")
    db.guardar_temperatura(20.0, "04/01/2024")
    db.guardar_temperatura(28.3, "05/01/2024")
    db.guardar_temperatura(22.1, "06/01/2024")
    db.guardar_temperatura(31.0, "07/01/2024")
    db.guardar_temperatura(10.5, "08/01/2024")
    db.guardar_temperatura(29.4, "09/01/2024")
    db.guardar_temperatura(35.6, "10/01/2024")

    # Devolver la temperatura de una fecha específica
    print("Temperatura del 03/01/2024:", db.devolver_temperatura("03/01/2024"))

    # Obtener la temperatura máxima en un rango
    print("Temperatura máxima del 01/01/2024 al 10/01/2024:", db.max_temp_rango("01/01/2024", "10/01/2024"))

    # Obtener la temperatura mínima en un rango
    print("Temperatura mínima del 01/01/2024 al 10/01/2024:", db.min_temp_rango("01/01/2024", "10/01/2024"))

    # Obtener temperaturas extremas en un rango
    min_temp, max_temp = db.temp_extremos_rango("01/01/2024", "10/01/2024")
    print("Temperatura mínima y máxima del 01/01/2024 al 10/01/2024:", min_temp, "ºC,", max_temp, "ºC")

    # Devolver todas las temperaturas en un rango
    print("Temperaturas del 01/01/2024 al 10/01/2024:")
    temperaturas = db.devolver_temperaturas("01/01/2024", "10/01/2024")
    for temp in temperaturas:
        print(temp)

    # Obtener la cantidad de muestras almacenadas
    print("Cantidad de muestras almacenadas:", db.cantidad_muestras())

    # Borrar una temperatura
    db.borrar_temperatura("05/01/2024")
    print("Cantidad de muestras tras borrar 05/01/2024:", db.cantidad_muestras())

    # Comprobar la temperatura después de borrar
    print("Temperatura del 05/01/2024 tras borrar:", db.devolver_temperatura("05/01/2024"))

if __name__ == "__main__":
    main()
