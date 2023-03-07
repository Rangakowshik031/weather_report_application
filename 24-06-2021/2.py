class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a


print("-----------ARTHIMETIC OPERATORS------------")
for i  in range(100):
    print("--------------------------")
    print("MENU")
    print("1.SUM OF NUMBERS")
    print("2.DIFFERENCE BETWEEN TWO NUMBERS")
    print("3.PRODUCT OF TWO NUMBERS")
    print("4.DIVISION OF TWO NUMBERS")
    print("5.EXIT")
    print("--------------------------")
    p=int(input("enter any code:"))
    if p==1:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("SUM OF TWO NUMBERS:",x+y)
    elif p==2:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("DIFFERENCE BETWEEN TWO NUMBERS:",x-y)
    elif p==3:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("PRODUCT OF TWO NUMBERS:",x*y)
    elif p==4:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("DIVISION OF TWO NUMBERS:",x/y)
    elif p==5:
        break
    else:
        print("invalid code")
