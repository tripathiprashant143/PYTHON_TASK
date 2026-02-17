sp=int(input('enter the starting point:-'))
ep=int(input('enyer the ending point:-'))
for i in range(sp,ep+1,1):
    j=1
    while(j<=10):
        print(i,"*",j,"=",i*j)
        j+=1
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')