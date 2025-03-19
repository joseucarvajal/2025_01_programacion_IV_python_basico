'''
    Sistema para controlar el ingreso de personas a un evento en particular.
    Ejemplo:
         - Conciertos
         - Peliculas
         - Shows de Comedy
         - etc.
    Las personas que ingresan al evento deben pagar una cantidad de dinero.
    Hay algunos eventos con restricciones de edad.
    Ejemplo:
        - Eventos infantiles (0-12 años)
        - Eventos juveniles (13-18 años)
        - Eventos adultos (mayor a 18 años)

    Versión 4:, vamos a utilizar todo lo visto hasta ahorita en las versiones
    anteriores:
        - Variables
        - Entrada y salida de datos
        - Estructuras de control (if, else, elif)
        - Estructuras de repetición (for, while)
'''

es_un_evento_solo_para_adultos = int(input('Ingrese si el evento es solo para adultos (1=Si/0=No): '))

ingresar_otra_persona = True
cuantas_personas_ingresaron = 0
total_dinero_recaudado = 0

while ingresar_otra_persona == 1:
    nombre = input('Ingrese su nombre: ')
    if nombre == '':
        print('El nombre no puede estar vacio')
    else:
        edad = int(input('Ingrese su edad: '))
        if es_un_evento_solo_para_adultos == 1:
            if edad < 18:
                print('No puede ingresar a este evento. Para ingresar debe ser mayor de 18 años')
            else:
                cuanto_dinero_pago_por_la_entrada = float(input('Ingrese cuanto dinero pago por la entrada: '))
                if cuanto_dinero_pago_por_la_entrada < 0:
                    print('La cantidad de dinero no puede ser negativa')
                else:
                    cuantas_personas_ingresaron += 1
                    print(f'{nombre} ingreso al evento correctamente')
                    total_dinero_recaudado += cuanto_dinero_pago_por_la_entrada
        else:        
            cuanto_dinero_pago_por_la_entrada = float(input('Ingrese cuanto dinero pago por la entrada: '))
            if cuanto_dinero_pago_por_la_entrada < 0:
                print('La cantidad de dinero no puede ser negativa')
            else:
                cuantas_personas_ingresaron += 1
                print(f'{nombre} ingreso al evento correctamente')
                total_dinero_recaudado += cuanto_dinero_pago_por_la_entrada

    ingresar_otra_persona = int(input('¿Desea ingresar otra persona? (1=Si/0=No): '))
    

print(f'El total de personas que ingresaron al evento es: {cuantas_personas_ingresaron}')
print(f'El total de dinero recaudado es: {total_dinero_recaudado}')
