class proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datosActividades = {}

    def agregarDatosProyecto(self, nombre_actividad, datos_actividad):
        self.actividades[nombre_actividad] = datos_actividad
