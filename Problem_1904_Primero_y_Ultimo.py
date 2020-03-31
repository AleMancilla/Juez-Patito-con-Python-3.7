#   Problem C: Primero y Ultimo
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 18  Resuelto: 16
#   [Enviar][Estado][Foro]
#   Descripción
#   Dada una cadena imprima los primeros tres caracteres y los tres últimos
#   
#   Entrada
#   La entrada consiste en varios casos de prueba. La primera linea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea de texto.
#   
#   Salida
#   Por cada caso de entrada imprima los tres primeros caracteres y los tres últimos.
#   
#   Ejemplo Entrada
#   3
#   abcdefghi
#   123456789
#   la casa de Juan Jose
#   Ejemplo Salida
#   abc ghi
#   123 789
#   la  ose

n = int(input())
for i in range(n):
    pal = input()
    print(pal[:3]+" "+pal[-3:])
    
    