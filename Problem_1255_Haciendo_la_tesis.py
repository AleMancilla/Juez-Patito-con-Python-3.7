#   Problem G: Haciendo la tesis
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 73  Resuelto: 44
#   [Enviar][Estado][Foro]
#   Descripción
#   Jose se encuentra haciendo su tesis, algo que le consume mucho tiempo.
#   
#   Jose puede quedarse horas haciendo su tesis, puede comenzar por la mañanas y terminar en la noche o viceversa, pero nunca mas de 24 horas, perdiendo la nocion del tiempo, por ello pide tu ayuda para saber cuanto tiempo se encuentra haciendo su tesis.
#   
#   Jose anota dos numero cada vez que comienza a hacer su tesis, h1 y m1, que son la hora y los minutos de inicio respectivamente.
#   
#   Asimismo anota dos numero cada vez que deja de hacer su tesis, h2 y m2, que son la hora y los minutos de fin respectivamente.
#   
#   h1 y h2 son enteros entre 0 y 23
#   
#   m1 y m2 son enteros entre 0 y 59.
#   
#   Entrada
#   Se le daran varios casos de prueba, en cada linea se dan 4 enteros.
#   
#   h1, m1, h2, m2 separados por un espacio.
#   
#   Salida
#   Por cada caso de prueba se le pide mostrar cuantas horas y cuantos minutos Jose se encuentra haciendo su tesis.
#   
#   Ejemplo Entrada
#   11 45 12 0
#   9 53 13 0
#   23 45 00 10
#   0 0 23 59
#   Ejemplo Salida
#   0 15
#   3 7
#   0 25
#   23 59

import sys

for datos in sys.stdin:
    datos = datos.split()
    h1 = int(datos[0])
    m1 = int(datos[1])
    h2 = int(datos[2])
    m2 = int(datos[3])

    if( m1 > m2 ):
        m2 = m2 +60 
        h1 = h1+1
    
    hora = h2 - h1
    minutos = m2 -m1

    if (hora <0):
        hora = hora*-1

    if hora == 24 :
        hora =0
    print(str(hora) + " "+ str(minutos))