class matrix:
    def __init__(self,a):
        self.a=a
        return
    def __add__(self,other):
        sum=0
        l2=[]
        for i in range(len(self.a)):
            sum=0
            sum=sum+(self.a[i]+other.a[i])
            l2.append(sum)
        return l2

l=[]
p=[]
r=int(input("enter number of elements in list l:"))
for i in range(r):
    a=int(input("enter number:"))
    l.append(a)

r=int(input("enter number of elements in list p:"))
for i in range(r):
    a=int(input("enter number:"))
    p.append(a)

print(l,p)
x=matrix(l)
y=matrix(p)
if len(p)==len(l):
    print(x+y)
else:
    print("cannot be added")
