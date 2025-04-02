'''
Vamos a crear un sistema para controlar el ingreso de personas a un evento.

Los eventos tienen:
    - hora de inicio
    - si es solo para adultos
    - costo por persona
    - nombre del evento

Versión 5:
    - Se utiliza polimorfismo para calcular el costo total de los eventos. Siendo estos eventos de distintos tipos:
        - EventoNormal: Evento normal.
        - EventoCaridad: Evento de caridad.
        - EventoDeportivo: Evento deportivo.

    todos los eventos anteriores tienen un comportamiento diferente en cuanto a la forma de calcular el costo total.

    Todos los eventos anteriores heredan de la clase EventoConCosto, pero cada evento tiene un comportamiento diferente 
    en cuanto a la forma de calcular el costo total.
        - EventoNormal: Evento normal. El costo total de este evento es el valor de la boleta por persona.
        - EventoCaridad: Evento de caridad. El costo total de este evento es el valor de la boleta por persona, pero con un incremento del 50%.
        - EventoDeportivo: Evento deportivo. El costo total de este evento es el valor de la boleta por persona, pero con un descuento del 30%.
'''


from abc import abstractmethod


class EventoConCosto:
    @abstractmethod #Es un metodo abstracto, porque esta clase no sabe como calcular el costo por persona.
    def calcular_costo_por_persona(self):
        pass

#Se lee: "Evento es una clase que hereda de EventoConCosto"
class EventoNormal(EventoConCosto):
    _hora_inicio = -1
    _es_solo_para_adultos = False
    _costo_por_persona = 0
    _nombre_del_evento = ""

    def calcular_costo_por_persona(self):
        costo_total = self._costo_por_persona
        print(f"Calculando el costo por persona para el evento {self._nombre_del_evento}: {costo_total}")
        return costo_total

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
    
    def __init__(self, hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento):

        self.hora_inicio = hora_inicio
        self.es_solo_para_adultos = es_solo_para_adultos
        self.costo_por_persona = costo_por_persona
        self.nombre_del_evento = nombre_del_evento

class EventoCaridad(EventoNormal):
    _es_caridad = False
    @property
    def es_caridad(self):
        return self._es_caridad

    @es_caridad.setter
    def es_caridad(self, valor):
        if valor not in [True, False]:
            raise ValueError("El evento debe ser de caridad o no")
        self._es_caridad = valor

    def __init__(self, hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento):
        super().__init__(hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento)
        self.es_caridad = True

    def calcular_costo_por_persona(self):
        costo_total = self._costo_por_persona * 1.5
        print(f"Calculando el costo por persona para el evento {self._nombre_del_evento}: {costo_total}")
        return costo_total

class EventoDeportivo(EventoNormal):

    def __init__(self, hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento):
        super().__init__(hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento)

    def calcular_costo_por_persona(self):
        costo_total = self._costo_por_persona * 0.7
        print(f"Calculando el costo por persona para el evento {self._nombre_del_evento}: {costo_total}")
        return costo_total


evento_normal = EventoNormal(1000, False, 10000, "Concerto de Rock")
evento_caridad = EventoCaridad(1300, False, 10000, "Almuerzo de caridad")
evento_deportivo = EventoDeportivo(1800, True, 10000, "Lucha libre")


#Aqui viene el polimorfismo, vamos a crear una lista de eventos y vamos a recorrerla para calcular el costo total de los eventos.
eventos = [evento_normal, evento_caridad, evento_deportivo]

costo_total = 0
for evento in eventos:
    costo_total += evento.calcular_costo_por_persona()

print(f"El costo total de los eventos es: {costo_total}")
