import unittest
from clases.receta import Receta
from datetime import date

class TestReceta(unittest.TestCase):
    def test_receta_valida(self):
        receta = Receta("Paracetamol", "Cada 12 horas", date(2025, 6, 10))
        self.assertEqual(receta.medicamento, "Paracetamol")
