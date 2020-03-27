#   Problem F: Ordenando Numeros
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 163  Resuelto: 93
#   [Enviar][Estado][Foro]
#   Descripción
#   El siguiente problema es muy sencillo.
#   
#   Solo necesita de un buen estudiante con ganas de aprender y pensar un poco
#   
#   Dado un numero X se le pide ordenar el el mismo de forma ascendente
#   
#   Entrada
#   La entrada conciste de varios casos de prueba
#   
#   Cada caso de prueba contiene un numero X (1 <= x <= x ^ 18)
#   
#   Salida
#   Se le pide imprimir el numero ordenado
#   
#   Ejemplo Entrada
#   54321
#   4824584
#   78523154
#   3
#   10
#   Ejemplo Salida
#   12345
#   2444588
#   12345578
#   3
#   01

import sys

for datos in sys.stdin:
    num = int(datos)
    l = len(str(num))
    v=[]
    for i in range(l):
        v.append(int(num%10))
        num = num/10
    v = sorted(v)
    numt =''
    for i in range(l):
        numt = numt+str(v[i])
    print(numt.strip())
