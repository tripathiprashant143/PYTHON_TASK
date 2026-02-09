sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
sum=0
for i in range(sp,ep+1,1):
    print(i,end="")
    if(i<ep):
        print("+",end="")
    sum=sum+i
print("=",sum)