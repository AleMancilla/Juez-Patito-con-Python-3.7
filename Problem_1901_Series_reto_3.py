n = int(input())
for i in range(n):
    txt = input().split()
    k = int(txt[1])
    x = int(txt[0])
    aux=0
    auxi=1
    for j in range(x):
        if(j%k==0 and j!=0):
            auxi+=2
        print(auxi,end=" ")
    print('')