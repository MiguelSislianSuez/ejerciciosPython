'''
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por
las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
en cuenta su sueldo base y comisiones.
'''

sueldo = int(input('Introduzca sueldo base del trabajador: '))
comision = (sueldo * 10) /100
print("Este mes el trabajador recibe en concepto de comision ", comision, "euros")

#En el caso de que sea sobre el precio de la venta por producto

sueldo = int(input("Introduzca el sueldo del trabajador: "))
venta1 = int(input("Introduzca primera venta: "))
venta2 = int(input("Introduzca segunda venta: "))
venta3 = int(input("Introduzca tercera venta: "))

com1= (venta1 * 10)/100
com2= (venta2 * 10)/100
com3= (venta3 * 10)/100
comisiones = com1+com2+com3

sueldoFinal= sueldo + comisiones

print("El sueldo a final del mes con comisiones será de ", sueldoFinal," euros")
