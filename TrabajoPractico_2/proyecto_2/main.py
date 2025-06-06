from modules.temperaturas import TemperaturasDB

def main():
    """Prueba las operaciones de TemperaturasDB con un conjunto de mediciones."""
    # Crear base de datos
    db = TemperaturasDB()

    # Insertar mediciones
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

    # Consultar temperatura específica
    print("Temperatura del 03/01/2024:", db.devolver_temperatura("03/01/2024"))

    # Consultar máximas y mínimas en rango
    print("Temperatura máxima del 01/01/2024 al 10/01/2024:", db.max_temp_rango("01/01/2024", "10/01/2024"))
    print("Temperatura mínima del 01/01/2024 al 10/01/2024:", db.min_temp_rango("01/01/2024", "10/01/2024"))

    # Consultar extremos en rango
    min_temp, max_temp = db.temp_extremos_rango("01/01/2024", "10/01/2024")
    print("Extremos del 01/01/2024 al 10/01/2024:", min_temp, "ºC,", max_temp, "ºC")

    # Listar temperaturas en rango
    print("Temperaturas del 01/01/2024 al 10/01/2024:")
    for temp in db.devolver_temperaturas("01/01/2024", "10/01/2024"):
        print(temp)

    # Consultar cantidad de muestras
    print("Cantidad de muestras:", db.cantidad_muestras())

    # Borrar una temperatura y verificar
    db.borrar_temperatura("05/01/2024")
    print("Muestras tras borrar 05/01/2024:", db.cantidad_muestras())
    print("Temperatura del 05/01/2024 tras borrar:", db.devolver_temperatura("05/01/2024"))

if __name__ == "__main__":
    main()