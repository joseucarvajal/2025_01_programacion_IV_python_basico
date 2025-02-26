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

    Versión 5:, vamos a utilizar todo lo visto hasta ahorita en las versiones
    anteriores:
        - Variables
        - Entrada y salida de datos
        - Estructuras de control (if, else, elif)
        - Estructuras de repetición (for, while)
        - Nuevo: Manejo de errores que son más difíciles de controlar con if, else... etc.
        Esto se hace con try, except.
        - Ejemplo:
            - Si el usuario ingresa una edad que no es un número.
            - Si el usuario ingresa una cantidad de dinero que no es un número.
'''

while True:
    try:
        es_un_evento_solo_para_adultos = int(input('Ingrese si el evento es solo para adultos (1=Si/0=No): '))
        if es_un_evento_solo_para_adultos == 1 or es_un_evento_solo_para_adultos == 0:
            break
        else:
            print('Ingresar al evento debe ser solamente 1 ó 0')
    except ValueError:
        print('La entrada debe ser un número entero')

ingresar_otra_persona = True
cuantas_personas_ingresaron = 0
total_dinero_recaudado = 0

while ingresar_otra_persona == 1:
    nombre = input('Ingrese su nombre: ')
    if nombre == '':
        print('El nombre no puede estar vacio')
    else:
        while True:
            try:
                edad = int(input('Ingrese su edad: '))
                break
            except ValueError:
                print('La edad debe ser un número entero')
        if es_un_evento_solo_para_adultos == 1:
            if edad < 18:
                print('No puede ingresar a este evento. Para ingresar debe ser mayor de 18 años')
            else:
                while True:
                    try:
                        cuanto_dinero_pago_por_la_entrada = float(input('Ingrese cuanto dinero pago por la entrada: '))
                        if cuanto_dinero_pago_por_la_entrada < 0:
                            print('La cantidad de dinero no puede ser negativa')
                        else:
                            break
                    except ValueError:
                        print('La cantidad de dinero debe ser un número')

                    cuantas_personas_ingresaron += 1
                    print(f'{nombre} ingreso al evento correctamente')
                    total_dinero_recaudado += cuanto_dinero_pago_por_la_entrada
        else:        
            while True:
                try:
                    cuanto_dinero_pago_por_la_entrada = float(input('Ingrese cuanto dinero pago por la entrada: '))
                    if cuanto_dinero_pago_por_la_entrada < 0:
                        print('La cantidad de dinero no puede ser negativa')
                    else:
                        break
                except ValueError:
                    print('La cantidad de dinero debe ser un número')
            cuantas_personas_ingresaron += 1
            print(f'{nombre} ingreso al evento correctamente')
            total_dinero_recaudado += cuanto_dinero_pago_por_la_entrada

    while True:
        try:
            ingresar_otra_persona = int(input('¿Desea ingresar otra persona? (1=Si/0=No): '))
            if ingresar_otra_persona == 1 or ingresar_otra_persona == 0:
                break
            else:
                print('Ingresar otra persona debe ser solamente 1 ó 0')
        except ValueError:
            print('Ingresar si desea ingresar otra persona debe ser un número entero')
    

print(f'El total de personas que ingresaron al evento es: {cuantas_personas_ingresaron}')
print(f'El total de dinero recaudado es: {total_dinero_recaudado}')
