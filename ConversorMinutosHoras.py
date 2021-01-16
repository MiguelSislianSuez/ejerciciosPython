'''
Realiza un programa que reciba una cantidad de minutos
y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
'''

tiempo = int(input("Introduzca minutos a convertir: "))

horas = tiempo // 60
minutos = tiempo % 60

print(tiempo, " minutos, equivalen a ", horas, "horas y ", minutos, "minutos")
