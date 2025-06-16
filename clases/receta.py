from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str]):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = datetime.now()

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos__)
        return f"Receta de {self.__medico__} para {self.__paciente__} el {self.__fecha__.strftime('%d/%m/%Y')}:\n  Medicamentos: {meds}"
