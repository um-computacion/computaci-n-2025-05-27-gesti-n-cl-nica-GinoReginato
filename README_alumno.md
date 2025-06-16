#  Sistema de Gestión de Clínica Médica

Este proyecto es un sistema de consola para la gestión de una clínica médica. Permite registrar pacientes, médicos, agendar turnos, emitir recetas y consultar la historia clínica de cada paciente.

---

##  Estructura del proyecto

```
proyecto_clinica/
│
├── clases/
│   ├── clinica.py
│   ├── paciente.py
│   ├── medico.py
│   ├── especialidad.py
│   ├── historia_clinica.py
│   ├── turno.py
│   ├── receta.py
│   └── exceptions.py
│
├── tests/
│   ├── test_clinica.py
│   ├── test_paciente.py
│   ├── test_medico.py
│   └── ...
│
├── cli.py
└── README.md
```

---

##  ¿Cómo ejecutar el sistema?

1. Asegurate de tener Python 3.10 o superior instalado.
2. No se requieren librerías externas.
3. Desde la raíz del proyecto, ejecutá:

```bash
python cli.py
```

Esto lanzará el sistema interactivo en la terminal.

---

##  ¿Cómo ejecutar las pruebas?

1. Asegurate de estar en la raíz del proyecto.
2. Ejecutá el siguiente comando:

```bash
python -m unittest discover -s tests
```

Esto buscará y correrá automáticamente todos los tests dentro de la carpeta `tests/`.

---

##  Diseño general

El sistema fue diseñado aplicando principios de **Programación Orientada a Objetos (OOP)**, dividiendo claramente responsabilidades entre modelo, interfaz y pruebas.

###  Módulo de Clases (`clases/`)

- **`Paciente`, `Medico`**: Entidades principales.
- **`Clinica`**: Clase central que gestiona la lógica del sistema.
- **`Turno`, `Receta`, `HistoriaClinica`, `Especialidad`**: Clases auxiliares que encapsulan datos y comportamientos específicos.
- **`exceptions.py`**: Contiene excepciones personalizadas para mejorar el manejo de errores.

###  Interfaz de Línea de Comandos (`cli.py`)

- Menú interactivo que permite al usuario:
  - Agregar pacientes y médicos
  - Agendar turnos
  - Emitir recetas
  - Consultar turnos y la historia clínica de los pacientes

- Manejo robusto de errores mediante excepciones personalizadas.

###  Pruebas Unitarias (`tests/`)

- Cada clase tiene sus propios tests para:
  - Casos normales (comportamiento esperado)
  - Casos de error (validaciones y excepciones)
- Usa el módulo `unittest` nativo de Python.

---

##  Recomendaciones

- Usar formatos válidos de fecha (`dd/mm/yyyy`) y hora (`HH:MM`) al ingresar turnos.
- Al ingresar especialidades y días de atención, separar los días por comas y sin tildes.
- Si el sistema lanza una excepción, leer el mensaje para entender el error (por ejemplo, turno ocupado o paciente no encontrado).

---

##  Autor

- Reginato Gino
- Legajo: 63280 
- Carrera: Ing. Informatica 