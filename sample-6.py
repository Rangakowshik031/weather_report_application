'''l=[1,2,3,7,5]
n=12

for i in range(len(l)):
    sum=0
    for j in range(i,len(l)):
        sum = sum + l[j]
        if sum == n:
            print(i+1,j)
            break'''

'''l=[1,5,3,2]
c=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        sum=0
        sum=sum+l[i]+l[j]
        if sum == l[2]:
            c=c+1
            print(sum)
k=0
for i in range(1,len(l)+1):
    for j in range(i+1,len(l)+1):
        sum=0
        sum=sum+l[-i]+l[-j]
        if sum == l[-2]:
            k=k+1
            print(sum)

print(c+k)'''
'''x="abcd"
y="bbb"
z="yaxx"
a=str(sorted(z))
print(a)
for i in range(0,2):
    if z[i]==z[i+1]:
        print(i,i+1)'''
'''class A:
    def __init__(self,l):
        self.l=l
        return
    def __len__(self):
        return(len(self.l))

l=[1,2,3,4,5]
x=A(l)
print(len(x))


class A:
    def __init__(self,l):
        self.l=l
        return
    def __getitem__(self,other):
        return(self.l[other])

l=[1,2,3,4,5]
x=A(l)
print(x[2])

class A:
    def __init__(self,l):
        self.l=l
        return
    def __setitem__(self,other,val):
        self.l[other]=val
        return
    def display(self):
        print(self.l)

l=[1,2,3,4,5]
x=A(l)
x[2]=7
x.display()

class A:
    def __init__(self,l):
        self.l=l
        return
    def __contains__(self,other):
        if other in self.l:
            return True
        else:
            False

l=[1,2,3,4,5]
x=A(l)
if 9 in x:
    print("yes")
else:
    print("no")


class A:
    def __init__(self,l):
        self.l=l
        return
    def __call__(self,other):
        return self.l*other

x=A(10)
print(x(100))'''
        


'''def is_leap(year):
    leap = False
    if(year%4==0):
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    return leap

year = int(input())
print(is_leap(year))'''






'''n=int(input())
sum=0
j=0
for i in range(n,0,-1):
    sum=sum+i*(10**j)
    print(sum)
    j=j+1
print(sum)'''


'''
l=[1,2,3,4,0]
print(sum(l))
print(sorted(l))





def sortedSum(a):
    s=[]
    l=[]
    for i in range(len(a)):
        l.append(a[i])
        if(len(l)==1):
            s.append(l[0])
        else:
            z=sorted(l)
            print(z)
            su=0
            for i in range(len(z)):
                su=su+(i+1)*z[i]
            s.append(su)
    print(s)
    d=sum(s)
    e=10**9+7
    return d%e


a=[4,3,2,1]
v=sortedSum(a)
print(v)


print(10&8)'''



'''
def countPairs(arr):
    c=0
    m=range(100)
    s=[]
    d=[]
    for i in range(20):
        x=2**i
        d.append(x)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            s1=arr[i]&arr[j]
            if s1 in d:
                c=c+1
    return c

arr=[1,2,1,3]
s=countPairs(arr)
print(s)


m=range(100)
if 2 in m:
    print(m)

'''


'''def countPairs(arr):
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            s=arr[i]&arr[j]
            for k in range(100):
                if s==2**k:
                    c=c+1
    return c'''
        
'''def countPairs(arr):
    c=0
    m=range(100)
    s=[]
    d=[]
    for i in range(20):
        x=2**i
        d.append(x)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            s1=arr[i]&arr[j]
            s.append(s1)
    for i in range(len(s)):
        for j in range(100):
            if s[i]==2**j:
                c=c+1
    return c'''




'''s1=[6,8,0,1,3]
d=[]

def pop(a,l):
    print(a,l)
    l1=[]
    for i in l:
        if a<i:
            l1.append(i)
            s=l1[0]
            break
    if len(l1)==0:
        s=-1
    print(s)
    return s
for i in range(len(s1)-1):
    l=s1[i+1:]
    print(l)
    p=pop(s1[i],l)
    d.append(p)
d.append(-1)
print(d)
'''
        
'''s1=[6,8,0,1,3]
top=-1
s=[]
for i in range(len(s1)-1):
    s.append(s1[i])
    top=top+1
    if s[top]>s1[i+1]:
        s.append(s1[i])
        top=top+1
    else:
        s.append(-1)
    

print(s)
'''



import re
s="i.like.this"
a=s.split(".")
print(a)




























