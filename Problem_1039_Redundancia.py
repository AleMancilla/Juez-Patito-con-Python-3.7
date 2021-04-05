# Descripción
# Escriba un programa que permita eliminar a todos los duplicados de una secuencia de números enteros e
# imprima a los números enteros únicos junto con el número de ocurrencias de cada uno.

# Entrada
# El archivo de entrada contiene una secuencia de números enteros (positivos, negativos y/o cero). El archivo
# de entrada puede ser bastante grande.

# Salida
# La salida de este programa será una secuencia de pares ordenados, separados por saltos de línea. El primer
# elemento del par debe ser el primer entero del archivo de entrada. El segundo elemento debe ser el número
# de veces que este número aparece en el archivo de entrada. Cada par debe estar separado por un espacio. Los
# números enteros aparecen en el orden en que se encuentran en el archivo de entrada.

# Ejemplo Entrada
# 3 1 2 2 1 3 5 3 3 2
# Ejemplo Salida
# 3 4
# 1 2
# 2 3
# 5 1
# Ayuda
# Utilice TreeMap o un vector para contar  y linked list para mantener el orden

pal = input()
pal = pal.replace(' ', '')
palabra = ''.join([j for i,j in enumerate(pal) if j not in pal[:i]])
for item in palabra:
    cant = pal.count(item)
    print(item + ' '+ str(cant))
