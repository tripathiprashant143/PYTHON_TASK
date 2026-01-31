num=int(input('enter the number :-'))
i=1
count=0
while(num>0):
    count+=1
    num//=10
x=count
while(i<=x):
    print(i+1,end=",")
    print(i,end=",")
    i+=2
    
