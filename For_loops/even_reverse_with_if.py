sp=int(input('enter the statring point:-'))
ep=int(input('enter the ending point:-'))
for i in range(ep,sp-1,-2):
    if(ep%2==0 and sp%2==0):
        print(i)
