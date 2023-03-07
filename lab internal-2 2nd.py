class A:
    def __init__(self,a):
        self.a=a
    def __iadd__(self,other):
        self.a=self.a+other.a
        return self.a
    def __isub__(self,other):
        self.a=self.a-other.a
        return self.a
    def __imul__(self,other):
        self.a=self.a*other.a
        return self.a
    def __itruediv__(self,other):
        self.a=self.a/other.a
        return self.a
    def __imod__(self,other):
        self.a=self.a%other.a
        return self.a
    def __ipow__(self,other):
        self.a=self.a**other.a
        return self.a


print("MENU")
print("1.Addition Assignment")
print("2.Subtraction Assignment")
print("3.Multiplication Assignment")
print("4.Division Assignment")
print("5.Modulus Assignment")
print("6.Exponential Assignment")
print("7.EXIT")
for i in range(100):
    r=int(input("enter code:"))
    if r==1:
        m=int(input("enter any number:"))
        n=int(input("enter any number:"))
        x=A(m)
        y=A(n)
        x+=y
        print("Result=",x)
    elif r==2:
        m=int(input("enter any number:"))
        n=int(input("enter any number:"))
        x=A(m)
        y=A(n)
        x-=y
        print("Result=",x)
    elif r==3:
        m=int(input("enter any number:"))
        n=int(input("enter any number:"))
        x=A(m)
        y=A(n)
        x*=y
        print("Result=",x)
    elif r==4:
        m=int(input("enter any number:"))
        n=int(input("enter any number:"))
        x=A(m)
        y=A(n)
        x/=y
        print("Result=",x)
    elif r==5:
        m=int(input("enter any number:"))
        n=int(input("enter any number:"))
        x=A(m)
        y=A(n)
        x%=y
        print("Result=",x)
    elif r==6:
        m=int(input("enter any number:"))
        n=int(input("enter any number:"))
        x=A(m)
        y=A(n)
        x**=y
        print("Result=",x)
    elif r==7:
        break
    else:
        print("invalid code")
