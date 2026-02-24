s=input('inter the value:-')
l=0
ap=0
u_l=0
u_c=0
l_l=0
l_c=0
u_v=0
l_v=0
d_l=0
sp_l=0
x='A'|'E'|'I'|'O'|'U'
y='a'|'e'|'i'|'o'|'u'
for i in s:
    l+=1
for i in s:
    if(i>='A' and i<='Z') or (i>='a' and i<='z'):
        ap+=1
        if(i>='A' and i<='Z'):
            print(i,':-is a alphabat')
            u_l+=1
            if(x==i):
                print(i,':-is a upper vowel')
                u_v+=1
            else:
                print(i,':- is a upper consonant')
                u_c+=1
        else:
            print(i,":- is lowel alphabat")
            l_l+=1
            if(y==i):
                print(i,':-is a lower vowel')
                l_v=0
            else:
                print(i,':- is lower consonant')
                l_c+=1
    elif(i>='0' and i<='9'):
        print(i,':- is a digit')
        d_l+=1
    else:
        print(i,':-is a spacial charactor')
        sp_l+=1
print('total length of string:-',l)
print('total length of alphabates:-',ap)
print('total length of upper alphabates:-',u_l)
print('total length of upper vowel:-',u_v)
print('total length of upper conconant:-',u_c)
print('total length of lower alphabates :-',l_l)
print('total length of lower vowel:-',l_v)
print('total length of lower conconant:-',l_c)
print('total length of digit:-',d_l)
print('total length of spacial charactors:-',sp_l)