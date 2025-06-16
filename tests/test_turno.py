import unittest
from clases.turno import Turno
from clases.paciente import Paciente
from clases.medico import Medico
from clases.especialidad import Especialidad
from datetime import datetime

class TestTurno(unittest.TestCase):
    def test_turno_correcto(self):
        paciente = Paciente("Laura", "Martinez", "88888888", "Pasaje Falso 55")
        especialidad = Especialidad("Neurología")
        medico = Medico("Jorge", "Diaz", "B333", [especialidad], ["Martes"])
        fecha = datetime(2025, 6, 17, 14, 0)
        turno = Turno(paciente, medico, fecha, especialidad)
        self.assertEqual(turno.especialidad.nombre, "Neurología")
