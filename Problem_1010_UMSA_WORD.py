# Descripción
# La organización de la ICPC BOLIVIA hizo hacer letras grandes, para usarlas como publicidad en el evento.

# Mientras transportaban el paquete que almacenaba las letras este se rompió y dejo caer las letras, al caer las letras varias de estas se perdieron. Así que ellos no están seguros si con las letras restantes podrán armar las palabras que ellos quieren.

# Por ejemplo si tenemos las letras U, S, M, A, C, D, I, C, P, C y queremos armar la palabra ICPC UMSA, notaremos claramente que es posible armarla. En cambio si tuviéramos las letras U, M, S, D, G, I, I, C, P no será posible armar la palabra ICPC UMSA pues faltaría la letra “A”.

# Los organizadores piden tu ayuda. Ellos te darán las letras disponibles y quieren saber si es posible armar la palabra UMSA ICPC.

# Entrada
# La primera linea contendrá un entero N (1≤N≤20) el numero de casos de prueba. A continuación se te dara N lineas, cada una con una cadena (solo mayúsculas), donde cada carácter representa la letra disponible para armar las palabras ICPC UMSA.
# Salida
# Para cada Cadena que se te dio anteriormente, si es posible armar las palabras UMSA ICPC  imprimir **ES POSIBLE**, caso contrario **NO ES POSIBLE**.
# Ejemplo Entrada
# 3
# UMSAICPC
# ICPCUMSA
# ICPCUMSHJK
# Ejemplo Salida
# ES POSIBLE
# ES POSIBLE
# NO ES POSIBLE
# Ayuda
# 2da div. 2012 UMSA

n = int(input())
pal = "UMSAICPC"
aux = ''
for i in range(n):
    x = input()
    for item in pal:
        if(x.find(item) != -1):
            index = x.find(item)
            x = x[0:index] + x[index+1:]
            aux = aux + item
    if aux == pal:
        print('ES POSIBLE')
    else:
        print('NO ES POSIBLE')
    aux = ''
