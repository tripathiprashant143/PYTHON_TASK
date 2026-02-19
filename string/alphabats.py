s=input('enter the string:-')
upper_vowel='AEIOU'
lower_vowel='aeiou'
total_alphabat=0
upper_count=0
lower_count=0
space_count=0
charactor_count=0
c=0
num=0
for i in s:
    c+=1
for i in s:
    if(i>='0' and i<='9'):
        print('this is number:-',i)
        num+=1
    elif(i>='A' and i<='Z') or (i>='a' and i<='z'):
        total_alphabat+=1
        if(i>='A' and i<='Z'):
            print('this is upper alphabats:-',i)
            upper_count+=1
        elif(i>='a' and i<='z'):
            print('this is lower alphabats:-',i)
            lower_count+=1
    else:
        print("this is specieal charactors:-",i)
        charactor_count+=1
print('total length of string:-',c)
print('total length of number:-',num)
print('total length of alphabats:-',total_alphabat)
print('total length of upper alphabats:-',upper_count)
print('total length of lower alphabats:-',lower_count)
print('total length of space:-',space_count)
print('total length of speacial charactors:-',charactor_count)