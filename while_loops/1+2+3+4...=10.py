a=int(input('enter the value:-'))
i=1
sum=0
while(i<=a):
    print(i,end="")
    sum=sum+i
    if(i<a):
        print('+',end="") 
    i+=1
print("=",sum)