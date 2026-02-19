s=input('enter the string :-')
x=""
for i in s:
    if(i>='A' and i<="Z"):
        x+=chr(ord(i)+32)
    else:
        x+=i
print(x)