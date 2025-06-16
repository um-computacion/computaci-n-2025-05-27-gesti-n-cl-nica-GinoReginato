import unittest
from clases.historiaclinica import HistoriaClinica
from clases.receta import Receta
from datetime import date

class TestHistoriaClinica(unittest.TestCase):
    def test_historial_vacio(self):
        hc = HistoriaClinica("Paciente123")
        self.assertEqual(hc.obtener_historial(), [])

    def test_agregar_receta(self):
        hc = HistoriaClinica("Paciente123")
        receta = Receta("Ibuprofeno", "1 cada 8 horas", date.today())
        hc.agregar_receta(receta)
        self.assertEqual(len(hc.obtener_historial()), 1)
