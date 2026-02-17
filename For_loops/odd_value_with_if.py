sp=int(input('enter the statring point:-'))
ep=int(input('enter the ending point:-'))
for i in range(sp,ep+2,2):
    if(sp%2!=0 and ep%2!=0):
        print(i)