#   Problem A: Contar subcadenas
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 21  Resuelto: 13
#   [Enviar][Estado][Foro]
#   Descripción
#   El problema trata de contar todas las ocurrencias de una cadena en otra. Por ejemplo la cadena xy existe 3 veces en axybxyzxy.
#   
#   Entrada
#   La entrada consiste en varios casos de prueba. Cada caso de prueba consiste de dos líneas. La primera línea tiene la cadena. La segunda contiene la subcadena que queremos contar
#   
#   Salida
#   Por cada caso de entrada imprima en una linea un numero con la cantidad de veces que ocurre la segunda cadena.
#   
#   Ejemplo Entrada
#   2
#   lacasacasa
#   ca
#   estoesunproblema
#   e

n = int(input())
for i in range(n):
    pal = input()
    l = len(pal)
    parte = input()
    lpart = len(parte)
    contador = 0
    j=0
    while j < l:
        var = pal[j:j+lpart]
        if (var == parte):
            contador +=1
            j = j+lpart-1
        j+=1
    print(contador)
    