num=int(input())
dev=0
while num>0:
  mem=numr%10
  dev=(dev*10)+mem
  num=num//10
print(dev)
