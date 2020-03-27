#   Problem G: Sucesion de Farey
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 451  Resuelto: 292
#   [Enviar][Estado][Foro]
#   Descripción
#   La Sucesión de Farey es una de esas curiosidades matemáticas a la vez llenas de belleza y fáciles de entender que casualmente descubrió un no-matemático, John Farey, en 1928.
#   
#   La idea es tomar un número natural (ej. n = 3 ) y empiezar a definir la serie Farey(3) como una serie de fracciones que tienen como numerador y denominador los números entre 1 y n. En el caso de Farey(3) escribiendo todas estas fracciones serían
#   
#   11,12,13,21,22,23,31,32,33
#   
#   Esta serie tiene propiedades muy interesantes, pero antes de ello. ¿Podras mostrar la sucesion descrita arriba?
#   
#   Entrada
#   La entrada consiste en un numero entero 1<=n<=100 que representa el numero para el que quieres calcular Farey(n)
#   
#   Salida
#   La salida consiste en la serie descrita anteriormente, la impresion sera de un termino por linea.
#   
#   Ejemplo Entrada
#   3
#   Ejemplo Salida
#   1/1
#   1/2
#   1/3
#   2/1
#   2/2
#   2/3
#   3/1
#   3/2
#   3/3
#   Ayuda
#    OK

n = int(input())
for i in range(n):
    for j in range(n):
        print(str(i+1)+"/"+str(j+1))