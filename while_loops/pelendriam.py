a=int(input("enter the number:-"))
reverse=0
y=a
while(a>0):
    x=a%10
    reverse=reverse*10+x
    a//=10
print(reverse)  
if(y==reverse):
    print("this is pelendriam number!!!!") 
else:
    print("this is not pelindream number!!")