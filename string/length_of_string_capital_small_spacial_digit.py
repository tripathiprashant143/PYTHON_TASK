s=input('enter the string value:-')
c=0
ap=0
cl=0
sl=0
num=0
sc=0
sp=0
for i in s:
    print(i,end="")
    c+=1
for i in s:
    if(65<=ord(i)<=90) or (97<=ord(i)<=122):
        print('\nthis is the alphabats',i)
        ap+=1
        if(65<=ord(i)<=90):
            print('this is the capital latter:-',i)
            cl+=1
        elif(97<=ord(i)<=122):
            print('this is the small latter:-',i)
            sl+=1
    elif(48<=ord(i)<=56):
        print('this is the number :-',i)
        num+=1
    elif(33<=ord(i)<=47) or (58<=ord(i)<=64):
        print('this is the speacal charactor:-',i)
        sc+=1
    elif(32==ord(i)):
        print('this is the space charactor:-',i)
        sp+=1
print('total length of string is:-',c)
print('total length of alphabats is :-',ap)
print('total length of capical latter is:-',cl)
print('total length of small latter is :-',sl)
print('total length of number is:-',num)
print('total length of speacal charactor is :-',sc)
print('total length of space charactor is :-',sp)                