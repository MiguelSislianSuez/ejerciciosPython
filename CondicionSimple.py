'''Algoritmo que pida dos números e indique si el primero es mayor que el segundo o viceversa'''

numero1 = int(input("Introduzca el priemr número: "))
numero2 = int(input("Introduzca el segundo número: "))

if numero1 > numero2 :
    print("El número", numero1, " es mayor que el número ", numero2)
else:
    print("El número", numero2, " es mayor que el número ", numero1)
