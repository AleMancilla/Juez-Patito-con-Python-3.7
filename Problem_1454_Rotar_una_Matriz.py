# Descripción
# La entrada consiste de matrices cuadradas y el propósito es el de rotar la matriz 90, 180, 270 grados. La rotación de una matriz en 360 grados volvería a la matriz original.

# Por ejemplo: si tenemos la matriz:
# ⎡⎣⎢147258369⎤⎦⎥

# el resultado después de rotar 90 grados es:

# ⎡⎣⎢789456123⎤⎦⎥

# Entrada
# La primera línea de la entrada consisten en el tamaño N≤30 de la matriz y los grados que hay que rotar(90,180,270). Luego siguen  N filas con N números enteros separados por un espació.

# Salida
# En la salida escriba la matriz rotada la cantidad de grados solicitado.

# Ejemplo Entrada
# 4 90
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Ejemplo Salida
# 13 9 5 1
# 14 10 6 2
# 15 11 7 3
# 16 12 8 4
# Ayuda
# Codigo

def llenarMatriz(n):
    matriz = []
    num = 1
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(num)
            num +=1
    return matriz


def llenarMatrizInput(n):
    matriz = []
    # num = 1
    for i in range(n):
        matriz.append(input().split(' '))
        # for j in range(n):
        #     matriz[i].append(num)
        #     num +=1
    return matriz



def printMatriz(matriz):
    for item in matriz:
        print(item)

def printMatrizSinNada(matriz):
    for item in matriz:
        pal = ''
        for i in item:
            pal = pal + i + ' '
        print(pal[:-1])

def rotar90grados(matriz):
    n = len(matriz)
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(matriz[n-1-j][i])
            # print('__'+str(matriz[n-1-j][i])) 
    return mat



def rotarMatriz(matriz, grados):
    mat = matriz
    if(grados == 90):
        mat = rotar90grados(mat)
    elif (grados == 180):
        mat = rotar90grados(mat)
        mat = rotar90grados(mat)
    elif (grados == 270):
        mat = rotar90grados(mat)
        mat = rotar90grados(mat)
        mat = rotar90grados(mat)
    return mat

a, b = input().split()
n = int(a)
grad = int(b)
matriz = llenarMatrizInput(n)
matriz = rotarMatriz(matriz, grad)
printMatrizSinNada(matriz)
