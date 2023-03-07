'''class A:
    def m1(self):
        print("I am from class A")
        return

class B:
    def m2(self):
        self.a=A
        self.a.m1(self)

x=B()
x.m2()'''



''''class  A():
    def m1(self,b):
        self.b=b
        print("I am from class A")
        print(self.b)
        return
class B(A):
    def m1(self,b):
        self.b=b
        print("I am from class B")
        print(self.b)
        return

class C(B):
    def m1(self,b):
        self.b=b
        print("I am from class C")
        print(self.b)
        return

x=C()
x.m1(10)
y=B()
y.m1(20)'''
'''class A:
    def m1(self,b):
        self.b=b
        print("I am from class A")
        print(self.b)
        return

class B(A):
    def m1(self,b):
        self.b=b
        print("I am from class B")
        print(self.b)
        return

class C(A):
    def m1(self,b):
        self.b=b
        print("I am from class C")
        print(self.b)
        return

x=C()
x.m1(10)
y=B()
y.m1(20)
'''
'''class A:
    def __init__(self,a):
        self.a=a
        return

    def __add__(self,other):
        return (self.a+other.a)

x=A(10)
y=A(20)
print(x+y)'''


'''class complexx:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        return
    def __add__(self,other):
        self.c1=self.a+other.a
        self.c2=self.b+other.b
        return(self.c1,self.c2)

x=complexx(10,20)
y=complexx(10,20)
print(x+y)
l=list(x+y)
print(complex(l[0],l[1]))'''


'''class matrix:
    def __init__(self,a):
        self.a=a
        return
    def __add__(self,other):
        c=[]
        for i in range(3):
            l=[]
            for j in range(3):
                e=self.a[i][j]+other.a[i][j]
                l.append(e)
            c.append(l)
        return(c)



m=int(input("enter number of rows="))
n=int(input("enter number of columns="))
r=[]
for i in range(m):
    l=[]
    for j in range(n):
        p=int(input("enter number:"))
        l.append(p)
    r.append(l)

print(r)

x=matrix(r)

m=int(input("enter number of rows="))
n=int(input("enter number of columns="))
r=[]
for i in range(m):
    l=[]
    for j in range(n):
        p=int(input("enter number:"))
        l.append(p)
    r.append(l)

print(r)

y=matrix(r)

print(x+y)  '''





'''import datetime
class A:
    def __init__(self,a):
        self.a=a
        return
    def __isub__(self,other):
        self.a=self.a-other.a
        return(self.a)

x=A(10)
y=A(5)
x-=y
print(x)'''


'''import datetime
class A:
    def __init__(self,a):
        self.a=a
        return
    def __gt__(self,other):
        return(self.a>other.a)

x=A(datetime.date(2020,9,14))
y=A(datetime.date(2020,9,13))
print(x>y) '''               




'''file=open("r1.txt","w")
print(file.name)
print(file.mode)
print(file.closed)'''


'''import os
print(os.path.exists("F:\\"))'''


'''a=input("enter name:")
b=int(input("enter age"))
try:
    if b<18:
        raise Exception
except Exception:
    print("you are not eligible to vote")'''




'''for i in range(100):
    try:
        if i>20:
            raise StopIteration
    except StopIteration:
        break
    print(i)'''


    

'''class A(Exception):
    pass

import random
s=random.randint(-5,5)
print(s)
try:
    if s<0:
        raise A(s)
except A:
    print("hello")'''

'''class invalid_name(Exception):
    pass
class invalid_age(Exception):
    pass



try:
    m=input("enter name:")
    if len(m)==0:
        raise invalid_name
    n=int(input("enter age:"))
    if n<18:
        raise invalid_age
except invalid_name:
    print("enter a valid name")
except invalid_age:
    print("you are not eligible not vote")'''

'''import random
s=random.randint(100,200)
for i in range(5):
    try:
        m=int(input("enter any number:"))
    except Exception:
        print("enter a number")
    else:
        if m>s:
            print("Too large")
        elif m<s:
            print("Too small")
        else:
            print("correct")'''
'''import io
try:
    file=open("r6.txt","r")
    file1=open("r1.txt","w")
    file1.read()
except FileNotFoundError:
    print("file is not found")
except io.UnsupportedOperation:
    print("unsupported operation")
'''


    




'''import re
pat="hello"
s="hell everyone"
if (re.match(pat,s)):
    print("matched")
else:
    print("non match")

import re
pat="overridding"
s="Method overloading and method overridding are two forms of polymorphism"
i=re.finditer(pat,s)
for j in i:
    print(j.start())
    print(j.end())
    print(j.span())

pat1=" " 
s1=re.split(pat1,s)
print(s1)'''




import re
pat=r"[\w]+@[a-z]{2,}[\.]+[a-z]{2,3}"
s=" hello kowshikranga12@gmail.com"
i=re.findall(pat,s)
print(i)



pat=r"\b[6-9]{1}[0-9]{9}\b"
s="1234563456 9908517699 kjwef 79679/+6378963"
i=re.findall(pat,s)
print(i)

pat=r"\b[aeiou]+[\w]+[aeiou]\b"
s=" apple onto inevitable is"
i=re.findall(pat,s)
print(i)


pat="[A-Z]+[\w]{1,}"
s="Inheritance is important concept in Oop"
i=re.findall(pat,s)
print(i)

pat="TS[0-9]{2}[A-Z]{2}[0-9]{4}"
s="TS08EM4567  AP08DJ8548"
i=re.findall(pat,s)
print(i)


import re
pat="-"
sub=""
s="1601-20-748-031"
s1=re.sub(pat,sub,s)
print(s1)




s="hello how are you"
pat="[\w]{1,}"
i=re.findall(pat,s)
print(i)

pat=r"^[A-Za-z]{1,}"
i=re.findall(pat,s)
print(i)

pat=r"[A-Za-z]{1,}\Z"
i=re.findall(pat,s)
print(i)

s="hellohowareyou"
pat="[A-Za-z][A-Za-z]"
i=re.findall(pat,s)
print(i)



'''import turtle
m=turtle.Turtle()
colors=["orange","yellow","green"]
for i in range(3):
    m.color(colors[i])
    for j in range(4):
        m.forward(100)
        m.right(90)
    m.left(18)'''

'''import turtle,random
m=turtle.Turtle()
colors=["orange","yellow","green"]
for i in range(0,360,36):
    m.color(random.choice(colors))
    m.seth(i)
    m.circle(100)'''


'''import turtle,random
m=turtle.Turtle()
for i in range(60):
    for j in range(4):
        m.forward(100)
        m.right(90)
    m.right(9)'''




import re
pat="160120[0-9]{3}[0-9]{3}"
s="160120748031 160120748"
i=re.findall(pat,s)
print(i)



import re
pat=r"\b[A-Z][\w]{1,}"
s="Inheritance Oop"
i=re.findall(pat,s)
print(i)


import re
pat=r"\b[aeiouAEIOU][\w]{1,}[aeiouAEIOU]\b"
s="akward swamped onto exhaustive "
i=re.findall(pat,s)
print(i)

class A:
    def __init__(self,a):
        self.a=a
        return
    def __isub__(self,other):
        return(self.a>>other.a)




class invalidname(Exception):
    pass
class invalidage(Exception):
    pass

try:
    m=input("enter name:")
    if len(m)==0:
        raise invalidname
    n=int(input("enter age:"))
    if n<18:
        raise invalidage
except invalidname:
    print("enter a valid name")
except invalidage:
    print("sorry you are not eligible to vote")

pat=r"[\w]+@[\w]+[\.][\w]{2,3}"
s="kowshik@gmail.com hkjjgmail@.com"
i=re.findall(pat,s)
print(i)

import re 
pat=r"[A-Za-z][A-Za-z]" 
s="There are five types of Inheritance" 
i=re.findall(pat,s) 
print(i) 
    




































    
