#   Problem H: Series Reto 01
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 22  Resuelto: 8
#   [Enviar][Estado][Foro]
#   Descripción
#   Se te pide que para un N dado generes las N elementos de la siguiente serie:
#   
#   0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,...
#   
#   Entrada
#   Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#   
#   Salida
#   Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#   
#   Ejemplo Entrada
#   4
#   3
#   5
#   4
#   1
#   Ejemplo Salida
#   0 0 1 
#   0 0 1 1 2 
#   0 0 1 1 
#   0 

n = int(input())
for i in range(n):
    txt = ""
    x = int(input())
    aux=0
    for j in range(x):
        if(j%2==0 and j !=0):
            aux+=1
        txt +=str(aux) + " "
    print(txt)