#   Problem E: Salario
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 540  Resuelto: 185
#   [Enviar][Estado][Foro]
#   Descripción
#   Obtener el sueldo neto y descuento provisional de un trabajador, conociendo su sueldo bruto. Si es un cargo administrativo se le descontará el 12% del sueldo bruto, y si es operativo se le descontará el 17%.
#   
#   Entrada
#   La primera linbea de la entrada consiste en un numero entero que representa el n umero de casos.
#   
#   Cada caso de prueba consiste de un numero entero y un numero entero que representa 1 si es administrativo y 2 si es operativo.
#   
#   Salida
#   EL salarios que es un numero flotante con dos decimales
#   
#   Ejemplo Entrada
#   2
#   5000 1
#   3200 2
#   Ejemplo Salida
#   4400.00
#   2656.00

n = int(input())
for i in range(n):
    v = input().split()
    a = int(v[0])
    b = int(v[1])
    if b == 1: #si es administrativo
        a = a - (a * 0.12) #resta el 11%
    if b == 2: #si es operativo
        a= a -(a * 0.17) #resta el 17%

    print ("%.2f" % round(a,2))