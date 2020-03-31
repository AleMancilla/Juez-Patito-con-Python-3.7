#   Problem I: El k-esimo dígito
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 1342  Resuelto: 511
#   [Enviar][Estado][Foro]
#   Descripción
#   Dado un número entero N averiguar la cantidad de dígitos que tiene esté número, y además determinar cual es su k-esimo dígito.
#   
#   Por ejemplo para N = 18421 y k = 3,  el número tiene 5 dígitos y el tercer dígito es 4.
#   
#   Entrada
#   La entrada consta de dos números N (1 <= N <= 1*10¹⁸), el número a evaluar, y K el dígito que estamos interesados en conocer, se garantiza que K siempre será menor o igual al número de dígitos de N.
#   
#   Salida
#   La salida consta de dos números separados por un espacio, la cantidad de dígitos del número N, y el k-ésimo dígito de este
#   
#   Ejemplo Entrada
#   18421 3
#   Ejemplo Salida
#   5 4

dato = input().split()
l = len(dato[0])
num = int(dato[1])
print(str(l)+" "+dato[0][num-1])
