repeticiones = int(input('Ingrese el numero de veces que desea utilizar la calculadora: '))
for i in range(repeticiones):
    numero1 = input('Ingrese el primer numero: ')
    numero1 = float(numero1)

    numero2 = input('Ingrese el segundo numero: ')
    numero2 = float(numero2)

    resultado = None
    operacion = input('Ingrese la operacion: ')

    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        resultado = numero1 / numero2
    else:
        print('Operacion no valida')

    if resultado is not None:
        print(f'El resultado de la operacion es {resultado}')
