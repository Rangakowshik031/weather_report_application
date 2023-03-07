'''import turtle
import time
m=turtle.Turtle()
for i in range(4):
    m.forward(100)
    m.right(90)


for i in range(3):
    m.forward(100)
    m.left(120)'''

'''m.circle(100)'''
'''m.shape("square")
m.forward(50)
time.sleep(2)
m.backward(20)'''



#turtle.done()

'''import matplotlib
from matplotlib import pyplot as pt
pt.plot([1,2],[3,4])
pt.show()'''


'''class A:
    x=1
    y=2
    @classmethod
    def method1(cls,x,y):
        cls.x=x
        cls.y=y
    def method2(cls,x,y):
        cls.x=x
        cls.y=y




a1=A()



A.method2(a1,10,20)
print(A.x,A.y,a1.x,a1.y)



a1.method2(30,40)
print(A.x,A.y,a1.x,a1.y)



A.method1(50,60)
print(A.x,A.y,a1.x,a1.y)



A.method2(a1,70,80)
print(A.x,A.y,a1.x,a1.y)



class A:
    def __init__(self,a):
        self.a=a

    def __getitem__(self,i):
        return(self.a[i])

l=[1,2,3]
x=A(l)
print(x[1])
'''





'''def func(l):
    if l<=0:
        return 0
    if l==1:
        return 1
    else:
        return func(l-1)+func(l-2)






for i in range(10):
    print(func(i))




def func(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return func(b,rem)

l=func(5,3)
print(l)





def func(x,y):
    if y<=0:
        return 1
    else:
        return x*func(x,y-1)

l=func(3,2)
print(l)





s=lambda x,y:x+y
print(s(1,2))


s=lambda n:1 if n==0 else n*s(n-1)
print(s(5))


n=int(input("enter any number:"))
t=n
sum=0
while n>0:
    rem = n%10
    sum =sum + rem*rem*rem
    n=int(n/10)
    
if t==sum:
    print("yes")
else:
    print("no")


n=int(input("enter any number:"))
t=n
sum=0
while n>0:
    rem = n%10
    sum = sum *10 +rem
    n=int(n/10)

print(sum)'''

'''n=int(input("enter any number:"))
t=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum= sum +i

if sum==t:
    print("yes")
else:
    print("no")


try:
    a=int(input("enter any number:"))
    b=int(input("enter any number:"))
    c=a/b
except ZeroDivisionError:
    print("not possible")'''
'''import tkinter
m=tkinter.Tk()
a=tkinter.Label(m,text="hello")
a.grid(row=0,column=0)
b=tkinter.Button(m,text="click",bg="yellow")
b.grid(row=1,column=1)
c=tkinter.Radiobutton(m,text="button")
c.grid(row=2,column=1)
d=tkinter.Checkbutton(m,text="button")
d.grid(row=3,column=1)
m.mainloop()'''









'''import turtle
m=turtle.Turtle()
for i in range(0,360,30):
    m.seth(i)
    m.circle(100)'''







'''import matplotlib
from matplotlib import pyplot
x=[1,2,3]
y=[1,2,3]
pyplot.bar(x,y)
pyplot.show()'''

'''def func(l):
    if l%2==0:
        return True
    else:
        return False

l=[2,3,4,5,6,7,8]
s=list(filter(func,l))
print(s)



def func(l):
    return l+1

l=[2,3,4,5,6,7,8]
s=list(map(func,l))
print(s)


import functools
def func(a,b):
    return a+b

l=[1,2,3,4,5]
print(functools.reduce(func,l))
    







import package
from package import hello


hello.func()





class A:
    def __init__(self,a):
        self.a=a
    def __getitem__(self,other):
        return self.a[other]
    def __setitem__(self,other,v):
        self.a[other]=v
    def __call__(self,other):
        return self.a*other
    def display(self):
        print(self.a)
    

l=[1,2,3,4]
x=A(l)
print(x[1])
x[2]=10
x.display()
y=A(2)
print(y(2))

import re
pat=r"\b[aeiou][\w]{1,}[aeiou]\b"
s="there is a lion ate aditya"
s=re.findall(pat,s)
print(s)


import re
pat=r"\b[789]{1}[0-9]{9}\b"
s="123456789 8074311341 529879896869565"
s=re.findall(pat,s)
print(s)



import re
pat=r"[\w.]+@[\w]+[\.][a-z]{2,3}"
s="kowshikranga12@gmail.com rthdnjhty#gmail.com "
s=re.findall(pat,s)
print(s)




import re
pat=r"\b[aeiou][\w]{1,}[aeiou]\b"
s="there is a lion ate aditya"
s=re.finditer(pat,s)
for i in s:
    print(i.start())
    print(i.end())
    print(i.span())
print(s)'''

    





class A:
    p=10
    def m1(self,a):
        self.a=a
        print(self.a)
        print(A.p)
        return

x=A()
x.m1(20)
x.b=200
print(x.a)
print(A.p)
print(x.__dict__)
print(A.__dict__)
print(A.__name__)
print(A.__bases__)
print(A.__module__)
print(A.__doc__)

class A:
    p=10
    def m1(self,a):
        self.a=a
        print(self.a)
        print(A.p)
        print("I am from m1 method")
        self.m2(self.a)
        return
    def m2(self,a):
        self.a=a
        print(self.a)
        print("I am from m2 method")
        return
x=A()
x.m1(20)
print(hasattr(x,'a'))
print(getattr(x,'a'))
setattr(x,'a',25)
print(x.a)


'''class A:
    @classmethod
    def m1(cls,a,b):
        cls.a=10
        cls.b=20
        return
    @staticmethod
    def m2():
        a=20
        b=30
        print(a,b)
        return

x=A()
A.m1(10,20)
x.m2()
print(A.__dict__)



class A:
    def m1(self):
        print("I am from class A")
        return
class B(A):
    def m2(self):
        print("I am from class B")
        return
x=B()
x.m2()
x.m1()
print(B.__mro__)
'''


















f1=open("p1.txt","w")
f1.write("CBIT GANDIPET")
f1.close()


f1=open("p1.txt","r")
f2=open("p2.txt","w")
p=f1.read()
r=p[::-1]
f2.write(r)
f1.close()
f2.close()


class student:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        return
    def display(self):
        print("student name:",self.a)
        print("student roll number:",self.b)
        print("student branch:",self.c)
        print("student attendance percentage:",self.d)
        return

x=student("kowshik","031","cse","98.97")
x.display()







def func(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return func(b,rem)

a=func(3,5)
print(a)


def func(l):
    if l%2==0:
        return True
    else:
        return False
l=[2,3,4,5,6]
print(list(filter(func,l)))

def func(l):
    return l*2

l=[1,2,3,4,5,6]
print(list(map(func,l)))


import functools
def func(a,b):
    return a+b
l=[1,2,3,4,5]
print(functools.reduce(func,l))








class A:
    def m1(self,a):
        self.a=a
        print(self.a)
        print("i am from class A")
        return

class B:
    def m2(self,b):
        self.b=b
        self.c=A()
        self.c.m1(self.b)
        return

x=B()
x.m2(200)


'''for i in range(2,20):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)

l=[1,2,33,4]
l.pop(2)
print(l)
print(l.index(4))

c=[]
for i in range(3):
    l=[]
    for j in range(3):
        n=int(input("enter any number:"))
        l.append(n)
    c.append(l)
print(c)


d=[]
for i in range(3):
    l=[]
    for j in range(3):
        n=int(input("enter any number:"))
        l.append(n)
    d.append(l)
print(d)

e=[]
for i in range(3):
    l=[]
    for j in range(3):
        x=c[i][j]+d[i][j]
        l.append(x)
    e.append(l)
print(e)'''














def func(a,b):
    print(a,b)
    return
func(10,20)


def func(a,b):
    print(a)
    print(b)
    return

c=10
d=20
func(b=d,a=c)


def func(*a):
    for i in a:
        print(i)

func(10,20,304,90)



def func(a,b=90):
    print(a,b)
    return

func(20)






a=20
def func(b):
    print(b)
    c=20
    print(c)
    global a
    a=a+10
    print(a)

func(10)
print(a)



c=2+3*3/ 2 -90 %2

print(c)










x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)
x=y
print(x is y)


x=[1,2,3,4]
print(2 in x)

a=2+3j
print(a)
print(type(a))






import sys
print(sys.getsizeof(4))








with open("p1.txt","r") as f:
    p=f.read()
    d={}
    for i in p:
        e=p.count(i)
        d[i]=e
print(d)


import turtle
m=turtle.Turtle()
for i in range(5):
    m.forward(100)
    m.right(144)

from matplotlib import pyplot
x=[1,2,3]
y=[1,2,3]
pyplot.plot(x,y)
pyplot.xlabel("x axis")
pyplot.ylabel("y axis")
pyplot.show()


x=["organes","mangoes","apples"]
y=[2,3,4]
pyplot.bar(x,y)
pyplot.show()





class A:
    def __init__(self):
        print("object is created")

    def __del__(self):
        print("object is destroyed")

x=A()
y=x
z=x
print("Set obj1 to None...")
x = None
print("Set obj2 to None...")
y = None
print("Set obj3 to None...")
z = None










































