def printMatrixDiagonal(mat, n):
    a, b = 1,1
    contador = 1
    i = 0
    j = 0
    k = 0
    validador = True
  
    while k<n * n: 
        if validador: 
            while i >= 0 and j<n : 
                if contador == a:
                    contador = 1
                    a, b = b, a+b
                    mat[i][j] = mat[i][j] +1 
                else:
                    contador = contador+1
                # print(str(mat[i][j]), end = " ")
                k += 1
                j += 1
                i -= 1
  
            if i < 0 and j <= n - 1: 
                i = 0
            if j == n: 
                i = i + 2
                j -= 1
  
        else: 
            while j >= 0 and i<n : 
                if contador == a:
                    contador = 1
                    a, b = b, a+b
                    mat[i][j] = mat[i][j] +1 
                else:
                    contador = contador+1
                # print(mat[i][j], end = " ") 
                k += 1
                i += 1
                j -= 1
   
            if j < 0 and i <= n - 1: 
                j = 0
            if i == n: 
                j = j + 2
                i -= 1
             
        validador = not validador 
  

mat = [[5,7,10,1,8,], 
    [4,2,16,29,3],
    [17,46,23,15,14],
    [19,23,34,12,20],
    [21,11,14,25,18]
        ] 
n = 5
printMatrixDiagonal(mat, n)

for item in mat:
    print(item)
 