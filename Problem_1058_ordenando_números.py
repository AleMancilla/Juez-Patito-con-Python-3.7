# Descripción
# Te diré varios números, y quiero que los imprimas ordenados ascendentemente. (el menor se imprime primero, y el mayor se imprime último).

# Entrada
# En una línea, se te dará un número entero 1≤n≤50 indicando la cantidad de casos de prueba.

# En la siguiente línea, se te dará un número entero 1≤a≤50, indicando cuántos números existen en la lista de números que debes ``ordenar''.

# En la siguiente línea, y separados entre sí por un espacio, se te darán a números enteros dentro del rango [−103,103]
# Salida
# Por cada caso de entrada, debes imprimir una línea con los a números enteros que se te dieron de entrada ordenados ascendentemente, imprime un espacio despues de cada numero y un salto de linea despues de imprimir todos los numeros con su respectivo espacio.

# Ejemplo Entrada
# 3
# 10
# 1 9 4 8 7 6 3 2 5 0
# 5
# 5 4 3 2 1
# 2
# 100 1
# Ejemplo Salida
# 0 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 
# 1 100 
# Ayuda
# Codigo
# r00th

# n = int(input())
# for i in range(n):
#     x = int(input())
#     num = input().split(' ')
#     vec = []
#     # num.sort()
#     for item in num:
#         try:
#             vec.append(int(item))   
#         except NameError:
#             print("An exception occurred")
#     vec.sort()
#     final = ''
#     for item in vec:
#         final = final + str(item) + " "
#     final = final[:-1]
#     print(final)


n = int(input())
for i in range(n):
    x = int(input())
    num = input().split(' ')
    vec = []
    # num.sort()
    for item in num:
        vec.append(int(item))  
    vec.sort()
    final = ''
    for item in vec:
        final = final + str(item) + " "
    final = final[:-1]
    print(final)
