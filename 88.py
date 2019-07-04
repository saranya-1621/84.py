ap1,ap2=map(int,input().split())
maxima=max(ap1,ap2)
while(1):
   if(maxima%ap1==0 and maxima%ap2==0):
         print(maxima)
         break
   maxima+=1
