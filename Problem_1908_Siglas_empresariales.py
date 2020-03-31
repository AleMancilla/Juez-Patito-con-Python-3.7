#   Problem G: Siglas Empresariales
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 20  Resuelto: 16
#   [Enviar][Estado][Foro]
#   Descripción
#   Las siglas empresariales son generalmente la primera letra de cada una de las palabras escritas en mayúsculas
#   
#   Entrada
#   La entrada consiste en varios casos de prueba. La primera linea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea de texto.
#   
#   Salida
#   Por cada caso de entrada imprima imprima la sigla de la empresa como se muestra en el ejemplo
#   Ejemplo Entrada
#   3
#   Banco Mercantil Santa Cruz
#   la cascada sociedad anonima
#   chocolates el Ceibo
#   Ejemplo Salida
#   BMSC
#   LCSA
#   CEC

n = int(input())
for i in range(n):
    pals = input().split()
    res =''
    for pal in pals:
        res += pal[0].upper()
    print(res)