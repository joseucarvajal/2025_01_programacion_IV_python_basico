'''
Vamos a crear un sistema para controlar el ingreso de personas a un evento.

Los eventos tienen:
    - hora de inicio
    - si es solo para adultos
    - costo por persona
    - nombre del evento

Versión 3:
    - Crear metodos para inicializar los atributos de los objetos.
    - Si es un evento de caridad, el costo por persona tiene un descuento del 50%

Problemas:
    - Se agregaron demasiados atributos a la clase. Lo cual complica su mantenimiento, su legibilidad y su testeo.

    Solución:
        - Versión 4:
            - Herencia
'''


class Evento:
    _hora_inicio = -1
    _es_solo_para_adultos = False
    _costo_por_persona = 0
    _nombre_del_evento = ""
    _es_caridad = False

    @property
    def hora_inicio(self):
        return self._hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, valor):
        if valor < 0 or valor > 2359:
            raise ValueError(
                "La hora de inicio debe ser un numero entre 0 y 2359")

        self._hora_inicio = valor

    @property
    def nombre_del_evento(self):
        return self._nombre_del_evento

    @nombre_del_evento.setter
    def nombre_del_evento(self, valor):
        if valor == "":
            raise ValueError("El nombre del evento no puede estar vacio")
        self._nombre_del_evento = valor

    @property
    def es_solo_para_adultos(self):
        return self._es_solo_para_adultos

    @es_solo_para_adultos.setter
    def es_solo_para_adultos(self, valor):
        if valor not in [True, False]:
            raise ValueError("El evento debe ser solo para adultos o no")
        self._es_solo_para_adultos = valor

    @property
    def costo_por_persona(self):
        return self._costo_por_persona

    @costo_por_persona.setter
    def costo_por_persona(self, valor):
        if valor < 0:
            raise ValueError("El costo por persona debe ser un numero positivo")
        self._costo_por_persona = valor
    

    @property
    def es_caridad(self):
        return self._es_caridad

    @es_caridad.setter
    def es_caridad(self, valor):
        if valor not in [True, False]:
            raise ValueError("El evento debe ser de caridad o no")
        self._es_caridad = valor
        if valor is True:
            self._costo_por_persona = self._costo_por_persona * 0.5

    def __init__(self, hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento, es_caridad):

        self.hora_inicio = hora_inicio
        self.es_solo_para_adultos = es_solo_para_adultos
        self.costo_por_persona = costo_por_persona
        self.nombre_del_evento = nombre_del_evento
        self.es_caridad = es_caridad

evento_1 = Evento(1000, False, 10000, "Concerto de Rock", False)
evento_1.hora_inicio = 800

evento_2 = Evento(1800, True, 20000, "Exhibición de Arte", True)
evento_3 = Evento(1900, False, 30000, "Competencia de Natación", False)


costo_total = evento_1.costo_por_persona + \
    evento_2.costo_por_persona + evento_3.costo_por_persona

print(f"El costo total del evento es: {costo_total}")
