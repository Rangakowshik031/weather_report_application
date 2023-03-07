def func(l):
    a=[]
    l1=len(l)
    for i in range(1,l1+1):
        a.append(l[-i])
    return a

l=[]
p=int(input("enter number of elements in list:"))
for i in range(p):
    a=int(input("enter number:"))
    l.append(a)
print("entered list=",l)
c=func(l)
print("reverse list=",c)
