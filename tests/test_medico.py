import unittest
from clases.medico import Medico
from clases.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_creacion_medico(self):
        esp = Especialidad("Cardiología")
        medico = Medico("Facundo", "San Martin", "F222", [esp], ["Lunes", "Miércoles"])
        self.assertIn(esp, medico.especialidades)
        self.assertEqual(medico.obtener_matricula(), "F222")
