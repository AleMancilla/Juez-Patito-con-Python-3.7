#   Problem F: Palindromes en el patito
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 862  Resuelto: 181
#   [Enviar][Estado][Foro]
#   Descripción
#   
#   En la universidad U. P.A.T.I.T.O estudiaba nuestro estudiante estrella de la carrera de informática llamado Robbie.
#   
#   Un día en la materia que se llamaba taller de programación, Robbie estaba en apuros por que tenían que participar en una competencia de programación a modo de dar su examen final y él no había escuchado al docente decir que tenían que crear sus nombres de usuario con palabras que sean palindromos (se dice palindromo a la palabra que se lee igual de izquierda a derecha que de derecha a izquierda.), pues Robbie ya había creado su cuenta de usuario y no tenía tiempo para crear otra. El juez patito le permitía cambiar solamente un carácter de su nombre de usuario así que tal vez podía haber una posibilidad de que el docente le haga valer el examen de la competencia. 
#   
#   Tu tarea es verificar si puede volver palindromo su nickname cambiando solamente un carácter. 
#   
#   
#   
#   Entrada
#   
#   La primera línea contiene el nombre de usuario s (1 ≤ |s| ≤ 15).
#   
#   
#   
#   Salida
#   Imprimir “YES” si Robbie puede cambiar exactamente un caracter para que se vuelva palindromo, de lo contrario imprimir “NO”.
#   
#   Ejemplo Entrada
#   rotador
#   robbieelpro
#   Ejemplo Salida
#   YES
#   NO

import sys


for datos in sys.stdin:
    pal1 = datos.strip()
    pal2 = datos[::-1].strip() 
    i = 0
    y = 0
    tam = len(pal1)
    if(pal1 != pal2):
        for x in pal1:
            if x!=pal2[i]:
                y=y+1
            i+=1
        if(y<=2):
            print("YES")
        else:
            print("NO")
    else:
        if(tam % 2 ==1):
            print("YES")
        else:
            print("NO")