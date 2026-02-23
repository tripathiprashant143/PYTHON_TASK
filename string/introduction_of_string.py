#Represent group of charactors.String are inclosed in double quort or single quort.The str data type represent a string .
#we can write the defrent type of string :-
#1).SINGLE QUORT:-Ex-
s='hello'
print(type(s))
print(s)

#2).DOUBLE QUORT:-Ex-
s="hello"
print(type(s))
print(s)

#3).TRIPLE SINGLE QUORT":-Ex-
s='''hello'''
print(type(s))
print(s)

#4).TRIPLE DOUBLE QUORT:-Ex-
s="""hello how are you"""
print(type(s))
print(s)

#5).DOUBLE QUORT IN SIDE SINGLE QUORT:-Ex-
s='hello my name is "python" and how are you'
print(type(s))
print(s)

#6).SINGLE QUORT IN SIDE DOUBLE QUORT:-Ex-
s="hello my name is 'python' and how are you"
print(type(s))
print(s)

#7).USING ESCAPE CHARACTORS:-Ex-
s="hello \n i am python"
print(type(s))
print(s)

#8).RAW STRING:-Ex-
s=r"hello \n i am python"
print(type(s))
print(s)

#NOTE:-If 
s1='Hello'
s2='Hello'
print(id(s1))
print(id(s2))
#Adress will be same but....
s1='Hello'
s2='hello'
print(id(s1))
print(id(s2))
#Adress will not same.

#INDEXING:-
#how can we get the string values from indexing.
#possitive-
s="hello"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
#negative-
print("")
s="hello"
print(s[-5])
print(s[-4])
print(s[-3])
print(s[-2])
print(s[-1])

#SYNTEXT OF STRING:-
#NOTE:-We are represent of string from 'str'.
#From while_loops:- Using indexing-
s='hello'
i=0
L=len(s)
while(i<L):
    print(s[i],end="")
    i+=1

#From for_loos:- 1)Using indexing(range)-
s='hello'
L=len(s)
for i in range(0,L,1):
    print(s[i],end="")

#2)withut using indexing(in)-
s='hello'
for i in s:
    print(i,end="")
