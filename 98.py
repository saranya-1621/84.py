an=int(input())
las=list(map(int,input().split()))
for i in range (len(las)):
  if(las[i]>ls[i+1]):
    break
print(i)
