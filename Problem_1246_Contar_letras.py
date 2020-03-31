#   Problem H: Contar letras
#   Time Limit: 1 Sec  Memory Limit: 128 MB
#   Enviar: 451  Resuelto: 291
#   [Enviar][Estado][Foro]
#   Descripción
#   Escriba un programa que lea una letra y una frase y cuente cuantas veces se repite la letra en la frase.
#   
#   Entrada
#   La entrada consiste de dos lineas. La primera linea contiene el caracter a contar. La segunda linea contiene la frase toda en minusculas.
#   
#   Salida
#   En la salida escriba la cantidad de veces que el caracter aparece en la frase.
#   
#   Ejemplo Entrada
#   i
#   universidad mayor de san andres
#   Ejemplo Salida
#   2

let = input()
pal = input()
print(pal.count(let))