class A:
    def __init__(self,a):
        self.a=a
    def __and__(self,other):
        return(self.a & other.a)
    def __or__(self,other):
        return(self.a | other.a)
    def __xor__(self,other):
        return(self.a ^ other.a)
    def __invert__(self):
        return(~self.a)

print("-----------BITWISE OPERATORS------------")
for i  in range(100):
    print("--------------------------")
    print("MENU")
    print("1.BITWISE  AND('&') OPERATOR BETWEEN TWO NUMBERS")
    print("2.BITWISE  OR('|') OPERATOR BETWEEN TWO NUMBERS")
    print("3.BITWISE  XOR('^') OPERATOR BETWEEN TWO NUMBERS")
    print("4.BITWISE  NOT('~') OPERATOR BETWEEN TWO NUMBERS")
    print("5.EXIT")
    print("--------------------------")
    p=int(input("enter any code:"))
    if p==1:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("BITWISE  AND('&') OPERATOR BETWEEN TWO NUMBERS :",x&y)
    elif p==2:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("BITWISE  OR('|') OPERATOR BETWEEN TWO NUMBERS:",x|y)
    elif p==3:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("BITWISE  XOR('^') OPERATOR BETWEEN TWO NUMBERS:",x^y)
    elif p==4:
        m=int(input("enter any number:"))
        x=A(m)
        print("BITWISE  NOT('~') OPERATOR BETWEEN TWO NUMBERS",~x)
    elif p==5:
        break
    else:
        print("invalid code")

