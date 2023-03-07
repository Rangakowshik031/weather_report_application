class c:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        return
    def __add__(self,other):
        self.p=self.a+other.a
        self.q=self.b+other.b
        return self.p,self.q

m=int(input("enter real axis of first complex number:"))
n=int(input("enter imaginary axis of first complex number:"))
p=int(input("enter real axis of second complex number:"))
q=int(input("enter imaginary axis of second complex number:"))
x=c(m,n)
y=c(p,q)
l=[]
l=x+y
print(complex(l[0],l[1]))
