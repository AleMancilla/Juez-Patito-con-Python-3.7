#   Problem D: Perversa Potencia (Difícil)
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 181  Resuelto: 153
#   [Enviar][Estado][Foro]
#   Descripción
#    Roger es un malvado profesor de matemáticas, lo llaman el Profesor Incorrecto porque sin importar que tanto te esfuerces para un examen suyo; tus respuestas serán incorrectas.
#   
#   En esta ocasión Roger está enseñando potenciación a sus alumnos. Como Roger está loco, les da una potencia de potencia de potencia de potencia. . . (6 potencias agrupadas) a sus alumnos para que resuelvan, y les indica que por cada digito de la potencia que acierten les dará un punto extra. Esta potencia es ridı́culamente grande! Una vez haces una potencia, el resultado debes elevarlo nuevamente, y este nuevo resultado debes elevarlo de nuevo! ¡NO ES POSIBLE ROGER!
#   Al pobre Rolando le falta un punto para aprobar la materia, solo necesita averiguar un digito de esta horrible potencia. Rolando cree que el digito más indicado para lograr conseguir un punto es el último digito del resultado, ósea el digito de las unidades.
#   Debes ayudar a Rolando a aprobar, dile el digito de las unidades correspondiente al resultado
#   de la potencia.
#   Entrada
#     Se te darán 2 lı́neas de entrada. En la primera lı́nea ira un numero entero positivo B, representando la base de la potencia agrupada.
#   
#   En la segunda lı́nea habrá 6 números enteros positivos N, las respectivas potencias en orden de
#   aparición
#   Lı́mites
#   (1 ≤ B ≤ 500) (1 ≤ N ≤ 10^10 )
#   SUBTAREAS: (60 puntos) Lı́mites originales
#   Salida
#    Debes imprimir el digito de las unidades del resultado de esta enorme potencia.
#   Ejemplo Entrada
#   2
#   1 2 1 2 2 3 
#   
#   13
#   12 34 15 60 10 2 
#   Ejemplo Salida
#   6 
#   
#   1
#   Ayuda
#   Explicación primer caso: ((2 1 ) 2 ) 1 ) 2 ) 2 ) 3 = 16777216 Donde podemos ver que el digito de las unidades es el numero 6.

import sys

# lo hacemos con una formula de combinatoria

if __name__ == "__main__":
    for datos in sys.stdin:
        datos2 = int(datos)

        pot = []
        pot = input().split()

        total = int(pot[0])*int(pot[1])*int(pot[2])*int(pot[3])*int(pot[4])*int(pot[5])

        b = total%4
        if(b == 0):
            b=4

        num = datos2**b

        print(num%10)

