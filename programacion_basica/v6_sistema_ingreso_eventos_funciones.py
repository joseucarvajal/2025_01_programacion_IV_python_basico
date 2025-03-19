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

    Problemas de la versión 5:
        - El código se vuelve cada vez más largo.
        - No se reutiliza código
        - No es fácil de mantener

    Versión 6:, vamos a utilizar todo lo visto hasta ahorita en las versiones
    anteriores:
        - Variables
        - Entrada y salida de datos
        - Estructuras de control (if, else, elif)
        - Estructuras de repetición (for, while)
        - Manejo de errores que son más difíciles de controlar con if, else... etc.
        Esto se hace con try, except.
        - Ejemplo:
            - Si el usuario ingresa una edad que no es un número.
            - Si el usuario ingresa una cantidad de dinero que no es un número.
        - Solución a los problemas de la versión 5:
            - Definir funciones
            - Llamar funciones
            - Pasar parámetros a funciones
            - Retornar valores de una función
'''

def solicitar_0_o_1(nombre_de_la_variable):
    while True:
        try:
            valor_de_la_variable = int(input(f'Ingrese si {nombre_de_la_variable} (1=Si/0=No): '))
            if valor_de_la_variable == 1 or valor_de_la_variable == 0:
                break
            else:
                print(f'{nombre_de_la_variable} debe ser solamente 1 ó 0')
        except ValueError:
            print(f'{nombre_de_la_variable} debe ser un número entero')

    return valor_de_la_variable

def solicitar_valor_positivo(nombre_de_la_variable):
    while True:
        try:
            valor_variable = float(input(f'Ingrese {nombre_de_la_variable}: '))
            if valor_variable < 0:
                print(f'{nombre_de_la_variable} no puede ser negativa')
            else:
                break
        except ValueError:
            print(f'{nombre_de_la_variable} debe ser un número')

    return valor_variable

es_un_evento_solo_para_adultos = solicitar_0_o_1('el evento es solo para adultos')

ingresar_otra_persona = True
cuantas_personas_ingresaron = 0
total_dinero_recaudado = 0

while ingresar_otra_persona == 1:
    nombre = input('Ingrese su nombre: ')
    if nombre == '':
        print('El nombre no puede estar vacio')
    else:
        edad = solicitar_valor_positivo('su edad')
        print(f'Edad: {edad}')
        if es_un_evento_solo_para_adultos == 1:
            if edad < 18:
                print('No puede ingresar a este evento. Para ingresar debe ser mayor de 18 años')
            else:
                cuanto_dinero_pago_por_la_entrada = solicitar_valor_positivo('cuanto dinero pago por la entrada')
                cuantas_personas_ingresaron += 1
                print(f'{nombre} ingreso al evento correctamente')
                total_dinero_recaudado += cuanto_dinero_pago_por_la_entrada
        else:        
            cuanto_dinero_pago_por_la_entrada = solicitar_valor_positivo('cuanto dinero pago por la entrada')
            cuantas_personas_ingresaron += 1
            print(f'{nombre} ingreso al evento correctamente')
            total_dinero_recaudado += cuanto_dinero_pago_por_la_entrada

    ingresar_otra_persona = solicitar_0_o_1('desea ingresar otra persona')
    
print(f'El total de personas que ingresaron al evento es: {cuantas_personas_ingresaron}')
print(f'El total de dinero recaudado es: {total_dinero_recaudado}')
