def cumulative_product(l):
    a=1
    l1=len(l)
    for i in range(l1):
        a=a*l[i]
    return a

l=[]
p=int(input("enter number of elements in list:"))
for i in range(p):
    a=int(input("enter number:"))
    l.append(a)
print("entered list =",l)
c=cumulative_product(l)
print("product of list of numbers=",c)

