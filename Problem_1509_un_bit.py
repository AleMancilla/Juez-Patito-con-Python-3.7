#   Problem C: Un bit
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 667  Resuelto: 299
#   [Enviar][Estado][Foro]
#   Descripción
#    Para este problema te pedimos que imprimas el i-esimo numero natural que en su representación binaria tiene exactamente un bit encendido.
#   
#   Entrada
#    La primera linea viene un numero t (1≤t≤60) que indica el numero de casos de prueba a procesar.
#   
#   A continuación t lineas, en cada linea un numero x (1≤x≤60), que indica que debes imprimir el x-esimo numero natural que en su representación binaria tiene exactamente un bit encendido.
#   
#   Salida
#    Por cada numero x, imprimir en una linea(sin espacios adicionales) el x-esimo numero natural que tiene exactamente un solo bit encendido en su representación binaria.
#   
#   Ejemplo Entrada
#   3
#   1
#   8
#   3
#   Ejemplo Salida
#   1
#   128
#   4

n = int(input())
for i in range(n):
    x = int(input())
    numb = "1"
    for j in range(x-1):
        numb = numb + "0"
    print(int(str(numb),2))