#   Problem C: Más esquizofrenia!
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 299  Resuelto: 100
#   [Enviar][Estado][Foro]
#   Descripción
#   Tu auxiliar de Álgebra I, ahora cree que vendrán varias personas que salvarán al mundo del caos. A estas personas les llama catalizadores de la bondad, y cree que están asociadas con los números que siguen este patrón:
#   
#   Para todo dígito del número, el dígito de la izquierda es más grande que el dígito de la derecha.
#   
#   Por ejemplo: si tenemos el numero 941, este sigue el patron dado ya que 9 es mayor a 4, y 4 es mayor a 1
#   
#   Te pidió que hagas un algoritmo para identificar a las personas que son catalizadoras de la bondad. Al igual que en Examen arbitrario, los alumnos escribiran un numero al final de su practica con el que podremos saber si son catilizadores de la bondad.
#   
#   Entrada
#   La entrada consiste en un numero entero n que representa la cantidad de practicas que recogio tu auxiliar, seguido de n numeros x (102≤x≤1018)
#   
#   Salida
#   Tu algoritmo deberá decir "SÍ!" si esta persona es considerada catalizadora de la bondad de lo contrario imprimir  "NO!".
#   
#   Ejemplo Entrada
#   5
#   6540
#   6549
#   1234
#   855
#   950
#   Ejemplo Salida
#   SI!
#   NO!
#   NO!
#   NO!
#   SI!

n = int(input())
for i in range(n):
    num= int(input())
    l = len(str(num))
    boolean = "SI!"
    for j in range(l-1):
        aux = num%10
        num = num/10
        if(int(num%10) <= aux):
            boolean = "NO!"
    print(boolean)
