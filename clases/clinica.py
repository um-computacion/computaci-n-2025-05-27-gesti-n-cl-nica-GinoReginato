from datetime import datetime
from clases.exceptions import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)
from clases.historiaclinica import HistoriaClinica
from clases.turno import Turno
from clases.receta import Receta


class Clinica:
    def __init__(self):
        self.__pacientes__ = {}
        self.__medicos__ = {}
        self.__turnos__ = []
        self.__historias_clinicas__ = {}

    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise ValueError("Paciente ya registrado")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise ValueError("Médico ya registrado")
        self.__medicos__[matricula] = medico

    def obtener_pacientes(self):
        return list(self.__pacientes__.values())

    def obtener_medicos(self):
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado")
        return self.__medicos__[matricula]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora: datetime):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException()

        medico = self.__medicos__[matricula]
        dia = self.obtener_dia_semana_en_espanol(fecha_hora)
        if not self.validar_especialidad_en_dia(medico, especialidad, dia):
            raise MedicoNoDisponibleException("El médico no atiende esa especialidad ese día")

        self.validar_turno_no_duplicado(matricula, fecha_hora)

        turno = Turno(self.__pacientes__[dni], medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException()
        if not medicamentos:
            raise RecetaInvalidaException()

        receta = Receta(self.__pacientes__[dni], self.__medicos__[matricula], medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni):
        if dni not in self.__historias_clinicas__:
            raise PacienteNoEncontradoException()
        return self.__historias_clinicas__[dni]

    def obtener_turnos(self):
        return list(self.__turnos__)

    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        for turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException()

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia):
        for esp in medico._Medico__especialidades__:
            if esp.obtener_especialidad().lower() == especialidad_solicitada.lower() and esp.verificar_dia(dia):
                return True
        return False
