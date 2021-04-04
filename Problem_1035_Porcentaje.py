# 1035: Porcentaje
# Time Limit: 1 Sec  Memory Limit: 32 MB
# Enviar: 310  Resuelto: 186
# [Enviar][Estado][Foro]
# Descripción
# Los identificadores uniformes denominados URI son cadenas como  http://icpc.baylor.edu/icpc/, mailto://foo@bar.org, ftp://127.0.0.1/pub/linux, o solo readme.txt que son utilizadas para identificar un recurso, usualmente en el internet o en una  computadora local.

# Algunos caracteres son reservados en los identificadores, en estos casos debe ser codificado por con un código denominado  percent-encoded remplazándolo por un símbolo de porcentaje seguido de dos dígitos hexadecimales que representan el código ascii del caracter en hexadecimal.

# A continuación se muestra una tabla con los siete caracteres reservados y su codificación:

# Caracter	Codificación
 
# " " (space)	%20
# "!" (exclamation point)	%21
# "$" (dollar sign)	%24
# "%" (percent sign)	%25
# "(" (left parenthesis)	%28
# ")" (right parenthesis)	%29
# "*" (asterisk)	%2a
# Su trabajo es realizar un programa que pueda codificar una cadena de caracteres.

# Entrada
# La entrada consiste de una o más cadenas, cada una con con 1 a 79 caracteres de longitud en una sola linea seguidos por el símbolo "#" que indica el final de los datos de entrada. Una cadena puede contener espacios, pero no al principio o al final y nunca deben existir más de dos espacios consecutivos.

# Salida
# Para cada cadena en los datos de entrada, remplace cada ocurrencia de los caracteres reservados en la tabla por su codificación, tal como se muestra, y luego imprima la cadena resultante en una linea. Tome en cuenta que la codificación para un asterisco es  \%2a con "a" en minúsculas.

# Ejemplo Entrada
# Happy Joy Joy!
# http://icpc.baylor.edu/icpc/
# plain_vanilla
# (**)
# ?
# the 7% solution
# #
# Ejemplo Salida
# Happy%20Joy%20Joy%21
# http://icpc.baylor.edu/icpc/
# plain_vanilla
# %28%2a%2a%29
# ?
# the%207%25%20solution
# Ayuda
# la funcion replace() seria de utilidad 

vector = [" ","!","$","%","(",")","*"]
vectorIndex = ["%20","%21","%24","%25","%28","%29","%2a"]

palabra = input()
while palabra != "#":
    textoFinal = ''
    for item in palabra:
    #  print(item)
        if item in vector:
            textoFinal = textoFinal + vectorIndex[vector.index(item)]
        else:
            textoFinal = textoFinal + item
    print(textoFinal)
    palabra = input()