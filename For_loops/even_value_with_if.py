sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
for i in range(sp,ep+1,2):
    if(sp%2==0 and ep%2==0):
        print(i)

