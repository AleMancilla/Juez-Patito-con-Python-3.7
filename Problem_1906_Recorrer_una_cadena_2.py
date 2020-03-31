#   Problem E: Recorrer una cadena 2
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 23  Resuelto: 15
#   [Enviar][Estado][Foro]
#   Descripción
#   El problema trata de recorrer una cadena y imprimir sus caracteres de acuerdo al formato mostrado.
#   
#   Entrada
#   La entrada consiste en varios casos de prueba. La primera linea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea de texto.
#   
#   Salida
#   Por cada caso de entrada imprima la entrada como se muestra en el ejemplo.
#   
#   Ejemplo Entrada
#   1
#   abcdefghi
#   Ejemplo Salida
#   a,b,c,d,e,f,g,h,i

n = int(input())
for i in range(n):
    pal = input()
    fin = ''
    for i in pal:
        fin+=i+","
    print(fin[:-1])