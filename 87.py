x1,x2=map(int,input().split())
m=1
while(m<=x1 and m<=x2):
   if(x1%m==0 and x2%m==0):
      gcd=m
   m=m+1
print(gcd)
