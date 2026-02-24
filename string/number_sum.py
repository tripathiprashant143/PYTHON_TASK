s=input('inter the value:-')
sum=0
for i in s:
    print(i,end="")
    sum+=int(i)
    if(i<s):
        print('+',end="")
print('=',sum)