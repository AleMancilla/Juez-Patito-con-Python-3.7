#   Problem B: Preguntar si una subcadena existe
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 14  Resuelto: 14
#   [Enviar][Estado][Foro]
#   Descripción
#   El problema trata de averiguar si una subcadena existe en otra cadena
#   
#   Entrada
#   La entrada consiste en varios casos de prueba. La primera linea de cada caso de prueba contiene la primera cadena y la segunda la subcadena.
#   
#   Salida
#   Por cada caso de entrada imprima la entrada imprima si existe o no existe la subcadena en la cadena como se muestra en el ejemplo.
#   
#   Ejemplo Entrada
#   2
#   lagrancasadelpisco
#   casa
#   clasesconeljuezpatito
#   pases
#   Ejemplo Salida
#   si
#   no


n = int(input())
for i in range(n):
    pal = input()
    parte = input()
    contador = 0
    var="no"
    if(parte in pal):
        var="si"
    print(var)
    