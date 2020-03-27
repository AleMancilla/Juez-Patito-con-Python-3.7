if __name__ == "__main__":
    datos = input().split()
    n = int(datos[0])
    m = int(datos[1])
    vector=[]
    for i in range(2,n//2):
        if(m%i==0 and n%i==0):
            vector.append(i)
    if(m%n==0):
        vector.append(n)
    q = int(input())
    for i in range(q):
        datos2 = input().split()
        aux = 1
        a = int(datos2[0])
        b = int(datos2[1])
        for j in range(a,b):
            if j in vector:
                print(j)
                aux = 0
        if aux == 1:
            print("-1")


