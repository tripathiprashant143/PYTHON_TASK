num=int(input('enter the value:-'))
h=0
while(num>0):
    x=num%10
    if(x>h):
        h=x
    num//=10
print(h,':-is the second heiggest value')
 