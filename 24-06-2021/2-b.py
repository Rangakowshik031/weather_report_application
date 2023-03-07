class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        return(self.a > other.a)
    def __lt__(self,other):
        return(self.a < other.a)
    def __ge__(self,other):
        return(self.a >= other.a)
    def __le__(self,other):
        return(self.a <= other.a)
    def __eq__(self,other):
        return(self.a==other.a)
    def __ne__(self,other):
        return(self.a != other.a)

print("-----------REALATIONAL OPERATORS------------")
for i  in range(100):
    print("--------------------------")
    print("MENU")
    print("1.COMPARING TWO NUMBERS WITH '>' ")
    print("2.COMPARING TWO NUMBERS WITH '<'")
    print("3.COMPARING TWO NUMBERS WITH '>='")
    print("4.COMPARING TWO NUMBERS WITH '<='")
    print("5.COMPARING TWO NUMBERS WITH '=='")
    print("6.COMPARING TWO NUMBERS WITH '!='")
    print("7.EXIT")
    print("--------------------------")
    p=int(input("enter any code:"))
    if p==1:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("COMPARING TWO NUMBERS WITH '>' :",x>y)
    elif p==2:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("COMPARING TWO NUMBERS WITH '<' :",x<y)
    elif p==3:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("COMPARING TWO NUMBERS WITH '>=' :",x>=y)
    elif p==4:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("COMPARING TWO NUMBERS WITH '<=':",x<=y)
    elif p==5:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("COMPARING TWO NUMBERS WITH '==':",x==y)
    elif p==6:
        m=int(input("enter any number:"))
        n=int(input("enter any numbebr:"))
        x=A(m)
        y=A(n)
        print("COMPARING TWO NUMBERS WITH '!=':",x!=y)
    elif p==7:
        break
    else:
        print("invalid code")
