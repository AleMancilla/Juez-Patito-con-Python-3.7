#   Problem E: Cambio de numero
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 364  Resuelto: 204
#   [Enviar][Estado][Foro]
#   Descripción
#   Los habitantes de Letropolis estan en busca de nuevas formas de atraer turistas a su ciudad y decidieron que una de sus avenidas proncipales pasara a llamarese Av. Primos, con la particuliaridad que todas los numeros de las casas de esta avenida estan formados por solamente digitos primos, entonces te piden ayuda para cambiar los antiguos numeros de las casas por los nuevos que se piden.
#   
#   Entonces ellos te daran cuantas casas existen en la avenida, y luego el numero antiguo que estas tenia, tu tarea es devolver su nuevo numero formado solo por digitos primos:
#   
#   Por ejemplo si una casa tenia el numero 7854215 su nuevo numero sera 7525 ya que es el numero que queda al quitar todos los digitos que no son primos.
#   
#   Si no se puede hacer lo anterior responder 0
#   
#   Entrada
#   La entrada consiste en un numero entero T que sera el numero de casas de la avenida. (Casos de prueba)	
#   
#   Por cada casa se te dara un numero entero n (1≤n≤109) que es el antiguo numero de la casa
#   
#   Salida
#   La salida consiste de un numero entero por cada casa, que representa el nuevo nuero de esa casa, si la casa no puede tener un numero formado por solo digitos primos se debe imprimir 0
#   
#   Ejemplo Entrada
#   4
#   7854215
#   123456
#   14689
#   27
#   Ejemplo Salida
#   7525
#   235
#   0
#   27

n = int(input())
for i in range(n):
    c = input()
    l = len(c)
    aux = '0'
    for j in range(l):
        if(c[j] != '0' and c[j] != '1' and c[j] != '4' and c[j] != '6' and c[j] != '8' and c[j] != '9'):
            aux=aux+c[j]
    print(int(aux.strip()))