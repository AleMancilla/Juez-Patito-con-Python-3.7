#   Problem A: Tablero
#   Time Limit: 2 Sec  Memory Limit: 128 MB
#   Enviar: 407  Resuelto: 209
#   [Enviar][Estado][Foro]
#   Descripción
#   Considere un tablero de ajedrez de r filas y c columnas. Cada casilla contiene de 0 a 9 monedas.
#   Considere que la equina superior izquierda es de color blanco. Por ejemplo un tablero con cuatro filas y cinco columnas es como sigue:
#   
#   
#   
#   Escriba un programa que calcule el numero total de monedas en las casillas blancas.
#   
#   Entrada
#   La entrada comienza con un numero que indica la cantidad de tableros existentes.
#   Luego siguen dos números separados por espacios que representan r y c respectivamente.
#   Siguen r lineas con c numeros separados por un espacio donde (0≤r,c≤100).
#   
#   Salida
#   Por cada tablero escriba una linea con el numero total de monedas en casillas blancas.
#   
#   Ejemplo Entrada
#   3
#   3 4
#   2 7 3 5
#   0 4 7 9
#   1 5 0 8
#   1 20
#   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
#   2 1
#   4
#   5
#   Ejemplo Salida
#   19
#   40
#   4

n = int(input())
for i in range(n):
    dat = input().split()
    a = int(dat[0]) # filas
    b = int(dat[1])
    
    mat = [] # vector [ "hola", "mundo", "mundial" ] 
                # mat[0] = "MARI"
                # print(mat[0])

    for j in range(a):
        mat.append([]) # vector [[] ]
        mat[j]=input().split() # vector [ ]   "hola mundo mundial".split() = "hola" "mundo"



    var = 0
    for j in range(a):
        for k in range(b):
            if(j%2==0 and k%2==0):
                var = var + int(mat[j][k])
            if(j%2==1 and k%2==1):
                var = var + int(mat[j][k])
    print(var)

    
# 1
# 2 7
# 5 1 5 1 5 1 5
# 1 5 1 5 1 5 1
# 
# 5_5_5_5
# _5_5_5_
