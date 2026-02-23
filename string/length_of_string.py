s=input('enter the string value:-')
c=0
dl=0
al=0
cl=0
sl=0
uv=0
uc=0
lv=0
lc=0
sc=0
for i in s:
    print(i,end="")
    c+=1
print('\nthe total length is:-',c)
for i in s:
    if(i>='0' and i<='9'):
        print('this is the digit:-',i)
        dl+=1
    elif(i>='A' and i<='Z') or (i>='a' and i<='z'):
        al=0
        if('this is capital latter:-',i):
            cl+=1
        else:
            print('this is a small latter:-',i)
            sl+=1
        match(i):
            case 'A'|'E'|'I'|'O'|'U':
                print('this is the upper_vowel:-',i)
                uv+=1
            case __:
                print('this is Upper consonant:-',i)
                uc+=1
        match(i):
            case 'a'|'e'|'i'|'o'|'u':
                print('this is the lower vowel :-',i)
                lv+=1
            case __:
                print('this is lower consonant:-',i)
                lc+=1
else:
    print('this is the speacal charactor:-',i)
    sc+=1
print('the length of digit is:-',dl)
print('the length alphabats is:-',al)
print('the length of capital latter is:-',cl)
print('the length of small latter is:-',sl)
print('the length of upper vowel  is:-',uv)
print('the length of upper consonant is:-',uc)
print('the length of lower vowel  is:-',lv)
print('the length of lower consonant is:-',lc)
print('the length of speacial charactor is:-',sc)