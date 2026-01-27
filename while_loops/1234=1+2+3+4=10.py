num=int(input('enter the value :-'))
rev=0
sum=0
while(num>0):
    x=num%10
    rev=rev*10+x
    num//=10
while(rev>0):
    z=rev%10
    sum=sum+z
    print(z,end="")
    rev//=10
    if(rev>0):
        print("+",end="")
print("=",sum)