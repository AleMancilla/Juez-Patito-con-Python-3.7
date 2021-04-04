n = int(input())

p = 2 # numero primo
c = 1 # contador de primo
d = 2 # comparador del 2 al primo
while c<=n:
    if p%d == 0:
        if p == d:
            print(p)
            c = c+1
        d = 2
        p = p+1
    else:
      d = d+1
