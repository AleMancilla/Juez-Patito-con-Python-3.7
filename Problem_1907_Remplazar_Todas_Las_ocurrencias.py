#   Problem F: Remplazar todas las ocurrencia
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 15  Resuelto: 10
#   [Enviar][Estado][Foro]
#   Descripción
#   El problema trata de remplazar todas las ocurrencias de caracteres de una cadena por otra.
#   
#   Por ejemplo cambiar los caracteres ca de lacasacasa por xyz para tener laxyzsaxyzsa.
#   
#   Entrada
#   La entrada consiste en varios casos de prueba. Cada caso de prueba consiste de dos lineas. La primera línea tiene la cadena en la que queremos cambiar caracteres y la segunda línea contiene dos cadenas separadas por un espacio. La primera cadena contiene los caracteres a buscar y la segunda los caracteres que remplazar.
#   
#   Salida
#   Por cada caso de entrada imprima la cadena original modificada
#   
#   Ejemplo Entrada
#   2
#   lacasacasa
#   ca xyz
#   estoesunproblema
#   e x
#   Ejemplo Salida
#   laxyzsaxyzsa
#   xstoxsunproblxma

n = int(input())
for i in range(n):
    pal = input()
    v = input().split()
    parte = v[0]
    rem = v[1]
    pal = pal.replace(parte,rem)
    print(pal)