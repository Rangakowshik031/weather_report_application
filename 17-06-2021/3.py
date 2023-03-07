class A:
    x=100
    def m1(self,a):
        self.a=a
        g=self.a+10
        return g

class B:
    def m2(self,c):
        self.b=A()
        self.c=c
        d=self.b.x+self.c
        #print(d)
        e=self.b.m1(d)
        print(e)
        return
l=B()
l.m2(10)
