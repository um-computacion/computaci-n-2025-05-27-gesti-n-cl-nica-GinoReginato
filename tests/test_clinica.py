import unittest
from clases.clinica import Clinica
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from datetime import datetime

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Carlos", "Lopez", "22222222", "Av San Martin 123")
        self.especialidad = Especialidad("Dermatología")
        self.medico = Medico("Lucía", "Mendez", "M123", [self.especialidad], ["Lunes"])
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_turno_exitoso(self):
        fecha = datetime(2025, 6, 16, 10, 0)
        self.clinica.agendar_turno("22222222", "M123", self.especialidad, fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)
