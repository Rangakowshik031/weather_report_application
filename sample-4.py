'''class student:
    marks=[]
    def __init__(self):
        self.name=input("enter name:")
        self.rollno=int(input("enter roll no:"))
        self.marks=[]
        for i in range(3):
            a=int(input("enter marks:"))
            self.marks.append(a)
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)


a=student()
b=student()
a.display()
b.display()'''


'''s="abcd"
a="abcd"
print(s,a,sep="@",end=".com")'''

'''class string:
    def __init__(self,s):
        vowels=cons=upper=lower=spaces=0
        self.s=s
        for i in self.s:
            if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
                vowels=vowels+1
            elif i==' ':
                spaces=spaces+1
            else:
                cons=cons+1
            if(i.isupper()):
                upper=upper+1
            else:
                lower=lower+1
        print("vowels:{}".format(vowels))

a=string("abeioy iukj")'''



'''import sys

t1=10
print(sys.getrefcount(t1))'''


def s1(x):
    if x%2==0:
        return 1
s=list(filter(s1,[1,2,3,4,5]))
print(s)


def s1(x):
        return x*2
s=map(s1,[1,2,3,4,5])
print(list(s))


import functools

def s1(x,y):
    return x+y

s=functools.reduce(s1,[1,2,3,4,5])
print(s)  
def s(a,b):
    print(a,b)
    return a+b

print(s(4,5))


def s(a,b):
    print(a,b)

c=4
d=5
s(b=d,a=c)


def s(a,b=3):
    print(a,b)

s(4)


def s(*l):
    print(l)

s(1,2,3,4)
class a:
    def __init__(self,b):
        self.b=b
        return

x=a(10)
print(a.__name__)
print(a.__dict__)
print(a.__doc__)
print(a.__base__)
print(a.__module__)


class s:
    a=70
    b=100
    def add(self):
        self.c=s.a+s.b
        print(self.c)

x=s()
print(getattr(x,"a"))


class s:
    a=70
    b=100
    def add(self):
        self.c=s.a+s.b
        print(self.c)

x=s()
print(hasattr(x,"a"))


class s:
    a=70
    b=100
    def add(self):
        self.c=s.a+s.b
        print(self.c)

x=s()
setattr(x,"d",50)
print(dir(x))

class s:
    a=70
    b=100
    def add(self):
        self.c=s.a+s.b
        print(self.c)

x=s()
x.add()
delattr(x,"c")
print(x.a)
class a:
    def __init__(self,x):
        self.x=x
        print(self.x)
        return
    def add(self,y):
        self.y=y
        print(self.y)
        return


class b:
    def __init__(self,x):
        self.x=x
        print(self.x)
        self.c=a
        self.c.add(self,10)
        self.c.__init__(self,20)
        return

p=b(10)



class a:
    def __init__(self,x):
        self.x=x
        print(self.x)
        return
    def add(self,y):
        self.y=y
        print(self.y)
        return


class b(a):
    def __init__(self,x):
        self.x=x
        print(self.x)
        #.__init__(self,20)
        super().__init__(30)
        return

p=b(10)

class A:
    p=10
    def sample1(self,a):
        print("hello")
        self.a=a
        print(self.a)
        self.sample2(30)
    def sample2(self,b):
        print("hi")

x=A()
x.sample1(20)
print(dir(x))

class A:
    @classmethod
    def sample1(cls,a):
        cls.a=30
        cls.b=40
    @classmethod
    def sample2(cls,b):
        cls.c=30
        cls.d=40
        x.f=10
    @staticmethod
    def sample3():
        y=10
        z=20
    def sample4():
        y=10
        z=20

x=A()
x.sample1(20)
x.sample2(20)
x.sample3()
print(dir(A))
print(dir(x))





























































































































































