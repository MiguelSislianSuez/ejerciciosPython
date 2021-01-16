'''
Pide al usuario dos números y muestra la “distancia” entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
'''
#La función abs() calcula el valor absoluto de un número que
#recibe como parámetro y retorna el valor calculado como resultado.
#Si el número que recibe no es negativo devuelve el mismo valor sin cambios.

num1 = float(input('Introduzca primer valor'))
num2 = float(input('Introduzca segundo valor'))
print("Distancia:", abs(num1 - num2))

