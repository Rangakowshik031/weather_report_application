class A:
    def __init__(self,a):
        self.a=a
    def __lshift__(self,other):
        return(self.a << other.a)
    def __rshift__(self,other):
        return(self.a >> other.a)


print("-----------SHIFT OPERATORS------------")
for i  in range(100):
    print("--------------------------")
    print("MENU")
    print("1.LEFT SHIFT OPERATOR(<<) : ")
    print("2.RIGHT SHIFT OPERATOR(>>):")
    print("3.EXIT")
    print("--------------------------")
    p=int(input("enter any code:"))
    if p==1:
        m=int(input("enter any number:"))
        n=int(input("enter how many bits to shift:"))
        x=A(m)
        y=A(n)
        print("LEFT SHIFT OPERATOR(<<):",x<<y)
    elif p==2:
        m=int(input("enter any number:"))
        n=int(input("enter how many bits to shift:"))
        x=A(m)
        y=A(n)
        print("RIGHT SHIFT OPERATOR(>>) :",x>>y)
    elif p==3:
        break
    else:
        print("invalid code")
