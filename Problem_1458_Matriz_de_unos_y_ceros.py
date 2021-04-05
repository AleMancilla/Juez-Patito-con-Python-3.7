# Descripción
# El problema es sencillo, para un N (tamaño de la matriz) generar una matriz de este tipo:

# 10101

# 01010

# 10101

# 01010

# 10101

# Esta sería la matriz para N = 5.

# Entrada
# Se le dará un  único número N (1 <= N <= 1000) el tamaño de la matriz.

# Salida
# Generar una matriz como la descrita en la entrada.

# Ejemplo Entrada
# 5
# Ejemplo Salida
# 10101
# 01010
# 10101
# 01010
# 10101

def llenarMatrizCerosUnos(n):
    matriz = []
    num = 0
    for i in range(n):
        matriz.append([])
        for j in range(n):
            if(num % 2 == 0):
                matriz[i].append((j+1)%2)
            else:
                matriz[i].append(j%2)
        num +=1
    return matriz

def printMatrizSinNada(matriz):
    for item in matriz:
        pal = ''
        for i in item:
            pal = pal + str(i)
        print(pal)


n = int(input())
mat = llenarMatrizCerosUnos(n)
printMatrizSinNada(mat)