import unittest
from clases.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_paciente(self):
        paciente = Paciente("Gino", "Reginato", "12345678", "paso de los patos 1137")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(paciente.nombre, "Gino")
