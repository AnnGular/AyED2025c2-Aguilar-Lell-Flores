import unittest
from modules.temperaturas import TemperaturasDB

class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.db = TemperaturasDB()
        self.db.guardar_temperatura(25.5, "01/01/2024")
        self.db.guardar_temperatura(30.2, "02/01/2024")
        self.db.guardar_temperatura(15.8, "03/01/2024")

    def test_guardar_y_devolver_temperatura(self):
        self.assertEqual(self.db.devolver_temperatura("02/01/2024"), 30.2)
        self.assertIsNone(self.db.devolver_temperatura("04/01/2024"))

    def test_actualizar_temperatura(self):
        self.db.guardar_temperatura(28.0, "01/01/2024")
        self.assertEqual(self.db.devolver_temperatura("01/01/2024"), 28.0)

    def test_max_temp_rango(self):
        self.assertEqual(self.db.max_temp_rango("01/01/2024", "03/01/2024"), 30.2)
        self.assertIsNone(self.db.max_temp_rango("04/01/2024", "05/01/2024"))

    def test_min_temp_rango(self):
        self.assertEqual(self.db.min_temp_rango("01/01/2024", "03/01/2024"), 15.8)
        self.assertIsNone(self.db.min_temp_rango("04/01/2024", "05/01/2024"))

    def test_temp_extremos_rango(self):
        self.assertEqual(self.db.temp_extremos_rango("01/01/2024", "03/01/2024"), (15.8, 30.2))
        self.assertEqual(self.db.temp_extremos_rango("04/01/2024", "05/01/2024"), (None, None))

    def test_borrar_temperatura(self):
        self.db.borrar_temperatura("01/01/2024")
        self.assertIsNone(self.db.devolver_temperatura("01/01/2024"))
        self.assertEqual(self.db.cantidad_muestras(), 2)

    def test_devolver_temperaturas(self):
        expected = [
            "01/01/2024: 25.5 ºC",
            "02/01/2024: 30.2 ºC",
            "03/01/2024: 15.8 ºC"
        ]
        self.assertEqual(self.db.devolver_temperaturas("01/01/2024", "03/01/2024"), expected)
        self.assertEqual(self.db.devolver_temperaturas("04/01/2024", "05/01/2024"), [])

    def test_cantidad_muestras(self):
        self.assertEqual(self.db.cantidad_muestras(), 3)

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            self.db.guardar_temperatura(20.0, "32/01/2024")

    def test_rango_invalido(self):
        with self.assertRaises(ValueError):
            self.db.max_temp_rango("03/01/2024", "01/01/2024")

if __name__ == "__main__":
    unittest.main()