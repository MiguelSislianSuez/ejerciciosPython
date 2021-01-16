'''
Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:
•	55% del promedio de sus tres calificaciones parciales.
•	30% de la calificación del examen final.
•	15% de la calificación de un trabajo final.
'''

parcial1 = float(input('Introduzca notas del primer parcial: '))
parcial2 = float(input('Introduzca notas del segundo parcial: '))
parcial3 = float(input('Introduzca notas del tercer parcial: '))
examenFinal = float(input('Introduzca nota examen final: '))
trabajoFinal = float(input('Introduzca nota trabajo final: '))

notaParcial = parcial1 + parcial2 + parcial3
nota = (notaParcial/3) * 0.55 + examenFinal * 0.3 + trabajoFinal * 0.15

print ('La nota final del alumno será %.1f' % nota)



