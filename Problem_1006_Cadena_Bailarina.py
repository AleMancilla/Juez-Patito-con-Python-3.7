# Descripción
# Una cadena se llama bailarina si y solo si la primera letra es mayúscula y cada una de las demás letras es lo opuesto a la anterior letra (mayúscula, minúscula, mayúscula, minúscula, ..., etc.).

# Por ejemplo AbCd es una cadena bailarina, la primera letra es A mayúscula, la segunda letra es b minúscula, la siguiente letra es C mayúscula y por ultimo d es minúscula.

# Entrada
# La entrada consiste en un entero T numero de casos de prueba, seguido por T lineas, cada una contiene una cadena, puede ser que este vacia.

# Salida
# Imprimir T+1 lineas que contienen las cadenas bailarinas.

# Ejemplo Entrada
# 6
# o
# aaaabbbbaaaa
# Retweeted
# Like si resolviste el problema
# A
# s d ffd aa sds

# Ejemplo Salida
# O
# AaAaBbBbAaAa
# ReTwEeTeD
# LiKe Si ReSoLvIsTe El PrObLeMa
# A
# S d FfD aA sDs
# Ayuda
#  funciones toLowerCase() o toUpperCase() podrian ayudarte 

# tambien Ascci de 'a' -> 97 y de 'A' -> 65 osea existe 32 de diferencia en termino de valor de caracteres

n = int(input())
for i in range(n):
    x = input()
    palFinal = ''
    cont = 0
    for item in x:
        var = ' '
        if(item != ' '):
            if(cont % 2 ==0):
                var = item.upper()
            else:
                var = item.lower()
            cont += 1
        palFinal = palFinal + var
    print(palFinal)