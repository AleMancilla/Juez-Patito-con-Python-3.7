#   Problem B: Examen arbitrario
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 343  Resuelto: 167
#   [Enviar][Estado][Foro]
#   Descripción
#   ¡Oh no! tu auxiliar de Álgebra I es esquizofrénico y ha dejado de tomar su medicamento.
#   
#   Tu auxiliar tiene el delirio de que hay una persona que desencadenará un proceso de destrucción sobre la tierra (a esta persona, él le llama "catalizador de la maldad"), y cree que esa persona está identificada con el número 96. Es por eso que al final de la práctica, le pidió a sus alumnos que escribieran un número cualquiera dentro del rango [102,1018].
#   
#   El auxiliar de Álgebra I va a aplazar a cualquier alumno que responda con un número que contenga al 96. Tú tienes suerte, porque te haz ganado la fama de ser el mejor programador de todo el 1er semestre, así que el auxiliar te ha eximido de la pregunta con la única condición de que le ayudes, haciendo un algoritmo para identificar al "catalizador de la maldad".
#   
#   Entrada
#   Consistirá en un número n que indica el número de alumnos que entregaron la práctica. Por cada alumno, habrá un número x que indica el número que el alumno escribió para responder la última pregunta de la práctica.  (102≤x≤1018)
#   
#   
#   Salida
#   Por cada alumno que entregó la práctica, escribe "APLAZADO!" si el número que el alumno escribió, contenía algún 96. De lo contrario, escribe "TE SALVAS :D"
#   
#   Ejemplo Entrada
#   8
#   35894
#   961
#   169
#   596
#   986
#   666
#   9696
#   696
#   Ejemplo Salida
#   TE SALVAS :D
#   APLAZADO!
#   TE SALVAS :D
#   APLAZADO!
#   TE SALVAS :D
#   TE SALVAS :D
#   APLAZADO!
#   APLAZADO!

n = int(input())
for i in range(n):
    num = input()
    if('96' in num):
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")