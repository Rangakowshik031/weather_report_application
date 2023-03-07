class A:
    def __init__(self,a):
        self.a=a
    def __iadd__(self,other):
        self.a += other.a
        return(self.a)
    def __isub__(self,other):
        self.a -= other.a
        return(self.a)
    def __imul__(self,other):
        self.a *= other.a
        return(self.a)
    def __idiv__(self,other):
        self.a /= other.a
        return(self.a)
    def __ipow__(self,other):
        self.a **= other.a
        return(self.a)
    def __imod__(self,other):
        self.a %= other.a
        return(self.a)


print("-----------ASSIGNMENT OPERATORS------------")
for i  in range(100):
    print("--------------------------")
    print("MENU")
    print("1.ASSIGNING TWO NUMBERS WITH '+=' ")
    print("2.ASSIGNING TWO NUMBERS WITH '-='")
    print("3.ASSIGNING TWO NUMBERS WITH '*='")
    print("4.ASSIGNING TWO NUMBERS WITH '/='")
    print("5.ASSIGNING TWO NUMBERS WITH '**='")
    print("6.ASSIGNING TWO NUMBERS WITH '%='")
    print("7.EXIT")
    print("--------------------------")
    p=int(input("enter any code:"))
    if p==1:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        x+=y
        print("ASSIGNING TWO NUMBERS WITH '+=' :",x)
    elif p==2:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        x-=y
        print("ASSIGNING TWO NUMBERS WITH '-=' :",x)
    elif p==3:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        x*=y
        print("ASSIGNING TWO NUMBERS WITH '*=' :",x)
    elif p==4:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        x/=y
        print("ASSIGNING TWO NUMBERS WITH '/=':",x)
    elif p==5:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        x**=y
        print("ASSIGNING TWO NUMBERS WITH '**=':",x)
    elif p==6:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        x%=y
        print("ASSIGNING TWO NUMBERS WITH '!=':",x)
    elif p==7:
        break
    else:
        print("invalid code")
