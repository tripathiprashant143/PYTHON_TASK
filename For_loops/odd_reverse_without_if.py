sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
if(ep%2!=0):
    for i in range(ep,sp-1,-2):
        print(i)