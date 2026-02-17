sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
if(sp%2!=0):
    for i in range(sp,ep+1,2):
        print(i)