class A:
    x=10
    def m1(self):
        print("I am from class A")
        return

class B:
    def __init__(self):
        self.p=A
    def m2(self,q):
        self.q=q
        print(self.p.x+self.q)
        self.p.m1(self)
        return

d=B()
d.m2(10)
