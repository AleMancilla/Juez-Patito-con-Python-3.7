#   Problem I: Series Reto 02
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 9  Resuelto: 6
#   [Enviar][Estado][Foro]
#   Descripción
#   Se te pide que para un N dado generes las N elementos de la siguiente serie:
#   
#   0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, 21, 21, 34...
#   
#   Entrada
#   Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#   
#   Salida
#   Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#   
#   Ejemplo Entrada
#   4
#   10
#   6
#   7
#   1
#   Ejemplo Salida
#   0 0 1 1 1 1 2 2 3 3 
#   0 0 1 1 1 1 
#   0 0 1 1 1 1 2
#   0 
#   Ayuda

n = int(input())
for i in range(n):
    txt = ""
    x = int(input())
    aux=0
    a = -1
    b = 1
    c =a+b
    for j in range(x):
        if(j%2==0 and j !=0):
            a=b
            b=c
            c = a+b
        txt +=str(c) + " "
    print(txt)