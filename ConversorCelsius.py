'''Escribir un programa que convierta un valor
dado en grados Fahrenheit a grados Celsius.
Recordar que la fórmula para la conversión es: C = (F-32)*5/9'''

import math

farenheit = int(input('Introduzca grados Farenheit a convertir: '))
celsius = (farenheit-32) *5/9

print('Los grados Celsius son: %.2f' % celsius)