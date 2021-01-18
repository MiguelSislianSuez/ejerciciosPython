'''Pide un número por pantalla y que nos diga si es negativo, positivo o igual a cero'''
numero = int(input("Introduza número a comprobar"))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es igual a cero")
else:
    print("El número es negativo")


