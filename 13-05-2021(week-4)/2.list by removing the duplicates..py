def unique(b):
    c=[]
    for num in b:
        if num not in c:
            c.append(num)
    return c
     
a=[]
l=int(input("enter number of elements:"))
for i in range(l):
    p=int(input("enter items:"))
    a.append(p)
#print(a)
s=unique(a)
print(s)

