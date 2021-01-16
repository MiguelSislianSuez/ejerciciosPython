'''
Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuanto deberá pagar finalmente por su compra.
'''

producto = int(input('Introduzca el precio del prodcuto'))
descuento = (producto * 15) /100
precioFinal = producto - descuento
print('El precio final del producto será ', precioFinal, 'euros')