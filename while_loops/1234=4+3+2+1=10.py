num=int(input('enter the value:-'))
rev=0
sum=0
while(num>0):
    x=num%10
    rev=rev*10+x
    num//=10
    print(x,end='')
    sum=sum+x
    if(num>0):
        print("+",end="")
print("=",sum)