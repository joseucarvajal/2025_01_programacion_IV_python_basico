'''
Vamos a crear un sistema para controlar el ingreso de personas a un evento.

Los eventos tienen:
    - hora de inicio
    - si es solo para adultos
    - costo por persona
    - nombre del evento

Versión 1:
    - Crear una clase para representar un evento.
    - Crear un objeto para cada evento.
    - Calcular el costo total de todos los eventos.

    Problemas:
        - Se pueden crear eventos con valores incorrectos: ejemplo: eventos sin hora de inicio
        - Se pueden crear eventos sin nombre

    Solución:
        - Versión 2:
            - Utilizar metodos constructores para inicializar los atributos de los objetos.
'''

class Evento:
    hora_inicio = -1
    es_solo_para_adultos = False
    costo_por_persona = 0
    nombre_del_evento = ""


evento_1 = Evento()
evento_1.hora_inicio = 2000
evento_1.nombre_del_evento = "Concerto de Rock"
evento_1.costo_por_persona = 10000

evento_2 = Evento()
evento_2.nombre_del_evento = "Exhibición de Arte"
evento_2.costo_por_persona = 20000

evento_3 = Evento()
evento_3.nombre_del_evento = "Competencia de Natación"
evento_3.costo_por_persona = 30000


costo_total = evento_1.costo_por_persona + evento_2.costo_por_persona + evento_3.costo_por_persona

print(f"El costo total del evento es: {costo_total}")



