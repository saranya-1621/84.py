an=int(input())
la=[int(i) for i in input().split()]
for i in range(1,len(la)-1):
    if(la[i-1]>la[i])or(la[i]>la[i+1]):
        print(la.index(la[i]))
        break
