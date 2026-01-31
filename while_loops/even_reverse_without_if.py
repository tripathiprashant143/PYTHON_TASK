sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point :-'))
if(ep%2==0):
    while(ep>=sp):
        print(ep,end=",")
        ep-=2
else:
    while(ep>sp):
        print(ep-1,end=",")
        ep-=2