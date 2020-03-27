#   Problem A: Tomaco
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 128  Resuelto: 41
#   [Enviar][Estado][Foro]
#   Descripción
#   Mientras el Jefe Gorgory y su hijo Rapha pasaban por la carretera vieron a un puesto de venta de Tomaco como ambos no sabían que era un tomaco fueron a preguntar que era. Homero les dio una probada entonces ambos se volvieron locos por comer mas tomaco. Sin embargo, después de comprar una canaste de tomacos querían repartir los tomacos por igual necesitamos tu ayuda para ello por ejemplo si tenemos 8 tomacos podemos repartirlos por igual 4 para Rapha y 4 para Gorgory, por otro lado si tenemos 5 tomacos no hay forma de que ambos se repartan los tomacos por igual.
#   
#   
#   
#   Entrada
#   La entrada consiste de un único numero entero t (0<=t<=1000), que sera la cantidad de tomacos que compraron.
#   
#   Salida
#   Imprima “SI”, si es que ambos pueden dividir los tomacos en la mitad cada uno con un numero par de tomacos, y “NO” en otros casos.
#   
#   Ejemplo Entrada
#   8
#   Ejemplo Salida
#   SI
#   Ayuda

num = int(input()) # entrada de datos
if(num>3 and num%2==0): #la condicion indica que cada uno debe tener un numero par caso contrario no se pueda dividir
    print("SI")
else:
    print("NO")