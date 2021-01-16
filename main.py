'''
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
Formula: hipotenusa = raíz cuadrada de cateto1 al cuadrado + cateto2 al cuadrado
'''
import math

cateto1 = int(input('Introduzca cateto1: '))
cateto2 = int(input('Introduzca cateto2: '))

#Para calcular raices cuadarads usaremos la funcion Math y el metodo sqrt
hipotenusa = math.sqrt(cateto1 **2 + cateto1 **2)
print('La hipotenusa es: ', hipotenusa)

#En caso de no querer tantos decimales usaremos comodin %d y los decimales que queramos
print("la hipotenusa es: %.2f" % hipotenusa)
#Se encargara de redondear los decimales