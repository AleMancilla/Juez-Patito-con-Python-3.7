# Problem A: Rumores
# Time Limit: 1 Sec  Memory Limit: 128 MB
# Enviar: 573  Resuelto: 159
# [Enviar][Estado][Foro]
# Descripción
# Tenemos N personas que tienen relaciones de amistad entre si, resulta que si una persona tiene un rumor lo puede decir a todos sus amigos, al día siguiente sus amigos pasaran el rumor a sus amigos y así sucesivamente. Queremos saber si le llega el rumor de la persona X a la persona Y, ¿nos ayudas? ![image](http://200.7.160.55/judge/fckeditor/editor/images/smiley/msn/wink_smile.gif)
# Entrada
# La entrada consiste en un numero T casos de prueba, cada caso consiste en un numero N (2≤N≤100) el numero de personas numeradas de 1...N y M relaciones de amistad, seguido de M lineas que contienen pares de datos u, v esto quiere decir que u es amigo de v, por ultimo dos números X, Y.
# Salida
# La respuesta al problema en una linea por cada caso, si el rumor de X le llega a Y imprimir SI, imprimir NO si no es posible.
# Ejemplo Entrada
# 1
# 4 3
# 1 2   
# 2 3   
# 3 4   
# 1 4
# Ejemplo Salida
# SI
# Ayuda
# Considerar que la cantidad de personas que interactuaran es igual a N y M indica la cantidad de chismes que habrán osea lineas que introduzcan u, v de la sig forma. T
# 
# N M u, v ... u', v' x, y Union-Find

def funcion_buscar(lis,x,y):
    txt = "NO"
    for i in l:
        if(i[0]==x):
            x=i[1]
            if(x==y):
                txt = "SI"            
        
    print(txt)
  
t = int(input())
for i in range(t):
    var = input()
    a ,b = var.split()
    n=int(a)
    m=int(b)
    l = []
    for j in range(m):
        var = input()
        a ,b = var.split()
        u=int(a)
        v=int(b)
        l.append((u,v))
    var = input()
    a ,b = var.split()
    x=int(a)
    y=int(b)
    funcion_buscar(l,x,y)
