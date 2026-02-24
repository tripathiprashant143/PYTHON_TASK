s=input('enter the string value:-')
rev="" 
i=len(s)-1
while(i>=0):
    rev=rev+s[i]
    i-=1
print(rev)
arm=rev
if(s==arm):
    print('thsi is a armstrong')
else:
    print('this is not armstrong')