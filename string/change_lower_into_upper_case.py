string =input('enter the string :-')
x=""
for i in string:
    if(i>='a' and i<='z'):
        x+=chr(ord(i)-32)
    else:
        x+=i
print(x)
