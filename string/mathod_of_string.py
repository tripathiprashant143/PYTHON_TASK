print(dir(str))                        #this is used to find for the all fuction of string.

s="hello python"                       #output:- Hello python
ns=s.capitalize()
print(ns)

s="Hello Python"                       #output:- hello python
ns=s.casefold()
print(ns)

s='Hello'                              #output:- ***Hello***
ns=s.center(11,'*')
print(ns)

s='Hello'                              #output:- 2
ns=s.count('l')
print(ns)

s='Hello'                               #output:-  True
print(s.startswith('H'))

#if 

s='Hello'                               #output:- False
print(s.startswith('Q'))

s='Hello'                               #output:- True
print(s.endswith('o'))

#if

s='Hello'                               #output:- False
print(s.endswith('H'))

s='hello'                               #output:- HELLO
print(s.upper())

s='HELLO'                               #output:- hello
print(s.lower())

s='HELLO python'                        #output:- hello PYTHON
print(s.swapcase())

s='hello python'                        #output:- Hello Python
print(s.title()) 

s='HELLO'                               #output:- True
print(s.isupper())

#if           

s='HELlo'                                #output:- False
print(s.isupper())

s='hello'                                #output:- True
print(s.islower())
4
#if

s='helLO'                                #output:-  False
print(s.islower())
 
s='Hello Python'                         #output:-  True
print(s.istitle())

#if 
s='Hello python'                         #output:- False
print(s.istitle())

s='123'                                  #output:- True
print(s.isdigit())

#if

s='123qwe'                               #output:- False
print(s.isdigit())

s='hello'                                 #output:- True
print(s.isalpha())


s='hello1'                                 #output:- True
print(s.isalnum())

#if 

s='hello'                                  #output:- True
print(s.isalnum())

s=" "                                      #output:- True
print(s.isspace())

s="  hello  "                              #output:- hello
print(s.strip())

s="  hello  "                              #output:-hello___
print(s.lstrip())

s="  hello  "                              #output:-___hello
print(s.rstrip())

s='hello python'                           #output:- hello JAVA
print(s.replace("python","JAVA"))

s='python-java-sql'                        #output:-
print(s.split('-'))

l=['python','java','sql']                  #output:-
s="-".join(l)
print(s)

s="python sql java"                        #output:-
print(s.find("sql"))

s="python sql java"                        #output:-
print(s.find("raj"))

s="python sql java"                        #output:-
print(s.index('sql'))

s="python sql java"                        #output:-
print(s.partition('sql'))

mydict={83:80}                             #output:-
txt='Hello Sam!'
print(txt.translate(mydict))

txt='Hello Sam!'                           #output:-
mytable=str.maketrans("S","P")
print(txt.translate(mytable))