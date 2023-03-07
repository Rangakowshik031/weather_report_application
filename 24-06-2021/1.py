print("multilevel inheritance")
class A:
    def sample(self,a,b):
        self.a=a
        self.b=b
        print("I am from class A")
        return
class B(A):
    def sample(self,a,b):
        self.a=a
        self.b=b
        print("I am from class B")
        return

class C(B):
    def sample(self,a,b):
        self.a=a
        self.b=b
        #super().sample(10,20)
        print(self.a,self.b)
        print("I am from class C")
        return
x=C()
x.sample(10,20)

print("heirarchical inheritance")
class D:
    def sample1(self,a):
        self.a=a
        print(self.a)
        print("I am from class D")
        return

class E(D):
    def sample1(self,a):
        self.a=a
        print(self.a)
        print("I am from class E")
        return
class F(D):
    def sample1(self,a):
        self.a=a
        print(self.a)
        print("I am from class F")
        return
y=F()
y.sample1(30)
        
