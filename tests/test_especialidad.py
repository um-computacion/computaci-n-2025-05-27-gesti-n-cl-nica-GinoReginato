import unittest
from clases.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_especialidad_valida(self):
        esp = Especialidad("Pediatría")
        self.assertEqual(esp.nombre, "Pediatría")
