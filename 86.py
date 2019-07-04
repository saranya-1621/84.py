a=list(input())
s=[]
for i in a:
   if i not in s:
      s.append(i)
if a==s:
   print("Yes")
else:
   print("No")
