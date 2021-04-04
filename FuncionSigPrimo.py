def sigPrimo(num):
    p = num+1 # numero primo
    # c = 1 # contador de primo
    d = 2 # comparador del 2 al primo
    estado = True
    while estado:
        if p%d == 0:
            if p == d:
                # print(p)
                estado = False
                # c = c+1
            d = 2
            p = p+1
        else:
            d = d+1
    return p -1
n = int(input())
x = sigPrimo(n)
print(x)

