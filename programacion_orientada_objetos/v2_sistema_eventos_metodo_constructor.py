'''
Vamos a crear un sistema para controlar el ingreso de personas a un evento.

Los eventos tienen:
    - hora de inicio
    - si es solo para adultos
    - costo por persona
    - nombre del evento

Versión 2:
    - Crear metodos para inicializar los atributos de los objetos.

Problemas:
    - Se pueden poner valores a los atributos de los eventos que no sean correctos.

    Solución:
        - Versión 3:
            - Encapsamiento
'''

class Evento:
    hora_inicio = -1
    es_solo_para_adultos = False
    costo_por_persona = 0
    nombre_del_evento = ""

    def __init__(self, hora_inicio, es_solo_para_adultos, costo_por_persona, nombre_del_evento):

        if hora_inicio < 0 or hora_inicio > 2359:
            raise ValueError("La hora de inicio debe ser un numero entre 0 y 2359")
        
        self.hora_inicio = hora_inicio

        if es_solo_para_adultos not in [True, False]:
            raise ValueError("El evento debe ser solo para adultos o no")

        self.es_solo_para_adultos = es_solo_para_adultos

        if costo_por_persona < 0:
            raise ValueError("El costo por persona debe ser un numero positivo")

        self.costo_por_persona = costo_por_persona

        if nombre_del_evento == "":
            raise ValueError("El nombre del evento no puede estar vacio")

        self.nombre_del_evento = nombre_del_evento


evento_1 = Evento(1000, False, 10000, "Concerto de Rock")
evento_1.hora_inicio = -800

evento_2 = Evento(1800, True, 20000, "Exhibición de Arte")

evento_3 = Evento(1900, False, 30000, "Competencia de Natación")


costo_total = evento_1.costo_por_persona + evento_2.costo_por_persona + evento_3.costo_por_persona

print(f"El costo total del evento es: {costo_total}")



