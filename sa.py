'''class x:
    def m1(self):
        print("iam from x")
        return
    def m2(self):
        print("iam from x class")  #functional overloading
        return

class y:
    def m2(self):
        self.a=x()
        self.a.m1()
        self.a.m2()
        print("iam from y")
        return
    
a=y()
#a.m3()
a.m2()'''

'''class a:
    def m1(self):
        self.a=100
        a.s=1000
        print(self.a+a.s)
        return
x=a()
x.m1()
print(a.__dict__)'''


'''class a:
    @classmethod
    def m1(cls):
        print("i am from class methods")
        a.s=10
        return
a.m1()
p=a()
p.m1()
print(a.__dict__)'''


'''class a:
    @staticmethod
    def m1():
        c=10
        b=100
        print("hello")
        a.s=2
        print(locals())
        return

a.m1()
z=a()
a.m1()'''
class a:
    def __init__(self,b):
        self.b=b
        return
    def __cmp__(self,other):
        return self.b-other.b

x=a(10)
y=a(30)
z=x.__cmp__(y)
if z==0:
    print("equal")
else:
    print("not equal")












































