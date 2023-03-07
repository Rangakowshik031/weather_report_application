'''with open("p1.txt","r") as f:
    p=f.read()
    d={}
    for i in p:
        e=p.count(i)
        d[i]=e
print(d)



n=int(input("enter any number:"))
t=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=int(n/10)
if sum==t:
    print("yes")
else:
    print("no")


d=int(input("enter any number:"))
b=0
i=0
while(d!=0):
    r=d%2
    b=b+r*(10**i)
    d=d//2
    i=i+1
print(b)


d=int(input("enter any number:"))
b=0
i=0
while(d!=0):
    r=d%10
    b=b+r*(2**i)
    d=d//10
    i=i+1
print(b)'''


'''l=[1,2,3,3,3,4,7,5,5,6]
b=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            if l[i] not in b:
                b.append(l[i])
print(b)
            


def unique(l):
    b=[]
    for i in l:
        if i not in b:
            b.append(i)
    return b

l=[1,2,3,3,3,4,7,5,5,6]
print(unique(l))


    


def reverse(l):
    b=[]
    for i in range(1,len(l)+1):
       b.append(l[-i])
    return b

l=[1,2,3,4,5,6,7,8,9]
print(reverse(l))






def product(l):
    b=1
    for i in range(len(l)):
       b=b*l[i]
    return b

l=[1,2,3,4,5]
print(product(l))




s=lambda x,y:x+y
sum=0
for i in range(1,11):
    sum=sum+s(0,i)
print(sum)


def func(l):
    if l%2==0:
        return True
    else:
        return False

l=[1,2,3,4,5,6,7,8]
print(list(filter(func,l)))




def func(l):
        return l*2

l=[1,2,3,4,5,6,7,8]
print(list(map(func,l)))


fact=lambda n:1 if n==1 else n*fact(n-1)
print(fact(4))'''

'''s=lambda x,y:x**y

for i in range(1,6):
    print(s(2,i))'''







'''n=int(input("enter n th series:"))

l=[]
for i in range(1,n+1):
    p=1
    k=i
    while(k!=0):
        p=p*i
        k=k-1
    l.append(p)
print(l)

s=[]
for i in range(1,n+1):
    p=1
    while(i!=0):
        p=p*i
        i=i-1
    s.append(p)
print(s)

sum=0
for i in range(len(l)):
    sum = sum +(l[i]/s[i])
print(sum)'''







'''def func(a,b):
    a=20
    b=30
    def m1():
        print("hello")
    print(dir())

print(dir())
func(10,20)










a=10
b=20
def func():
    c=10
    global d
    d=20
    print(locals())
    

print(globals())
import builtins
print(dir())'''






'''
import datetime
class age:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def verify(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today<datetime.date(today.year,self.dob.month,self.dob.day):
            age=age-1
        print(age)

x=age("kowshik",datetime.date(2002,12,9))
x.verify()'''

'''class A:
    def __init__(self,a):
        self.a=a
        print(" i am created")
        return
    def m1(self):
        pass
    def __del__(self):
        print(" i am destroyed")
        return
x=A(10)
x.m1()
del x
x.m1()'''


'''class circle:
    radius=5
    def perimeter(self):
        self.peri=2*3.14*circle.radius
        return self.peri
    def area(self):
        self.area=3.14*circle.radius*circle.radius
        return self.area

x=circle()
print(x.perimeter())
print(x.area())'''


'''class A:
    p=10
    __q=20
    def m1(self,a):
        self.a=a
        print(" i am public")
        return
    def __m2(self,b):
        self.b=b
        print("i am private")
        return
x=A()
print(A.p)
#print(A.__q)
print(x._A__q)
print(x.m1(10))
print(x._A__m2(20))'''
        


'''class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        return
    def total(self):
        return (sum(self.marks))

x=student("kowshik",31,[99,98,100])
print(x.total())



import os
print(os.path.exists("F:\\"))'''

        
        

'''import re
pat=r"[\w.-]+@[\w.-]+"
s="kowshikranga@gmail.com kowshik.com  kowshik@yahoo.com"
l=re.findall(pat,s)
print(l)

import re
pat=r"\b[0-9]+[\s][\w]{1,}"
s="123 jygyu"
if(re.search(pat,s)):
    print("match")
else:
    print("non match")













class book:
    def __init__(self):
        self.title=""
        self.author=""
        self.price=0
    def read(self):
        self.title=input("enter book name:")
        self.author=input("enter author name:")
        self.price=int(input("enter book price:"))
        return
    def display(self):
        print("book name:",self.title)
        print("author name:",self.author)
        print("price:",self.price)
        return

my_books=[]
for i in range(100):
    print("1.Add books")
    print("2.Display books")
    m=int(input("enter choice:"))
    if m==1:
        b=book()
        b.read()
        my_books.append(b)
    elif m==2:
        for i in my_books:
            i.display()
    else:
        break
    









with open("a1.txt","w") as file:
    file.write(" cbit gandipet rangareddy")

file1=open("a1.txt","r")
s=file1.read()
d={}
for i in s:
    e=s.count(i)
    d[i]=e
print(d)'''



'''class A:
    def __init__(self,amount):
        self.amount=amount
        return
    def deposit(self,deposit_amount):
        #print("BALANCE:",self.amount)
        self.deposit_amount=deposit_amount
        self.amount=self.deposit_amount+self.amount
        self.balance()
        return
    def withdraw(self,withdraw_amount):
        self.withdraw_amount=withdraw_amount
        if(self.withdraw_amount>self.amount):
            print("get out")
        else:
            self.amount=self.amount-self.withdraw_amount
            self.balance()
        return
    def balance(self):
        print("BALANCE:",self.amount)

print("////WELCOME TO SBI BANK////")
x=A(100000)
for i in range(1,100):
    print("1.TO DEPOSIT")
    print("2.WITHDRAW")
    m=int(input("enter choice:"))
    if m==1:
        n=int(input("enter amount:"))
        x.deposit(n)
    elif m==2:
        n=int(input("enter amount:"))
        x.withdraw(n)
    else:
        break

'''


    
'''d=int(input("enter decimal number:"))
b=0
i=0
while(d!=0):
    r=d%2
    b=b+r*(10**i)
    d=d//2
    i=i+1
print(b)


d=int(input("enter binary number:"))
b=0
i=0
while(d!=0):
    r=d%10
    b=b+r*(2**i)
    d=d//10
    i=i+1
print(b)'''
        
'''a=10
b=2.3
c="hello"
d=True
e=2+3j

print(a,b,c,d,e)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''



'''a=10
print(type(a))
c=str(a)
print(type(c))

a=20
print(type(a))
c=float(a)
print(type(c))


a=2
print(type(a))
c=complex(a)
print(type(c))


a="10"
print(type(a))
c=float(a)
print(type(c))

a="True"
print(type(a))
c=bool(a)
print(type(c))
'''





'''x1=int(input("enter X distance of point 1:"))
y1=int(input("enter Y distance of point 1:"))
x2=int(input("enter X distance of point 2:"))
y2=int(input("enter Y distance of point 2:"))
dist=(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
distance=dist**0.5
print("distance between two points:",distance)'''
    

'''a="CSE"
b="AI&ML"
print(a+b)
print(a*3)
s="Inheritance provides resuability of code"
print(s[2])
print(s[2:8])
print(s[::-1])
print(len(s))
print(max(s))
print(min(s))
print(s.upper())
print(s.lower())
print(s.split(" "))
print(s.isdigit())
'''









'''l=[1,2,[1,2,4],7,["hello",2+3j]]
for i in range(len(l[2])):
    print(l[2][i])
print(l[4][0])
print(l[4][1])
'''
'''
s="Class used to create user defined datatypes"
l=[1,2,3,4,5]
t=(10,20,30,40)
print(s[2:4])
print(l[1:4])
print(t[1:3])
print(s[-1])
print(l[-1])
print(t[-1])
print(s[2])
print(l[2])
print(t[2])
print(s[4]*5)'''

'''l=[1,222,38,44,50,3,90,12,45]
t=(10,2,30,4,67,98,345,11)
print(len(l))
print(max(l))
print(min(l))
print(sorted(l))
print(len(t))
print(max(t))
print(min(t))
print(sorted(t))
'''
'''s="There are five types of inheritance"
d={}
for i in s:
    e=s.count(i)
    d[i]=e
print(d)
'''
'''s=input("enter a character:")
if(s.isupper()):
    print(s.lower())
elif(s.islower()):
    print(s.upper())'''

'''l=['a','e','i','o','u']
s=input("enter a character:")
if s not in l:
    print("Not a vowel")
else:
    print('vowel')
a=int(input("enter any number between 1 and 7"))
if a==1:
    print("Sunday")
elif a==2:
    print('Monday')
elif a==3:
    print('tuesday')
elif a==4:
    print('wednesday')
elif a==5:
    print('thursday')
elif a==6:
    print('friay')
else:
    print("saturday")'''

'''l=[]
for i in range(6):
    x=int(input("Enter student marks:"))
    l.append(x)
print(l)
sum=0
for i in range(len(l)):
    sum=sum+l[i]

t=len(l)
average=sum/t
print(sum,average)
if average>=90 and average<=100:
    print("A Grade")
elif average>=80 and average<=90:
    print("B garde")'''
    
'''m=int(input('Enter starting term of the series:'))
n=int(input('Enter end term of the series:'))
sum=0
for i in range(m,n+1):
    sum=sum+i
print("sum of the numbers from",m,"to",n,":",sum)'''

'''m=int(input("enter any number:"))
sum=0
t=m
while(m>0):
    r=m%10
    sum=sum+r*r*r
    m=int(m/10)
if t==sum:
    print("yes")
else:
    print("no")'''

'''d=int(input("enter decimal number:"))
b=0
i=0
while(d!=0):
    r=d%2
    b=b+r*(10**i)
    d=d//2
    i=i+1
print(b)

d=int(input("enter binary number:"))
b=0
i=0
while(d!=0):
    r=d%10
    b=b+r*(2**i)
    d=d//10
    i=i+1
print(b)
'''
'''m=int(input("enter a number:"))
while(m>=0):
    print(m)
    m=m-1
'''
'''m=int(input("enter any number:"))
sum=0
for i in range(1,m+1):
    sum=sum +(1/i)
print("sum of the series:",sum)'''
'''m=int(input("enter any number:"))
ans=1
for i in range(1,m+1):
    ans=ans*i
print("factorial of the number:",ans)'''

'''m=int(input("enter number of rows:"))
for i in range(1,m+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

m=int(input("enter number of rows:"))
for i in range(1,m+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
'''n=int(input("enter number of rows:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''n=int(input("enter number of rows:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
'''

'''for i in range(1,10):
    print(i)
    if i==5:
        break

for i in range(1,10):
    #
    print(i)
    if i==5:
        continue
    print(i)
for i in range(1,10):
    pass

'''
'''def duplicate(l):
    d=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[i]==l[j]):
                if l[i] not in d:
                    d.append(l[i])
    return(d)

l=[1,2,3,4,2,4,9,8,7,99,2,1]
print(duplicate(l))'''


'''def unique(l):
    d=[]
    for i in l:
        if i not in d:
            d.append(i)
    return d
l=[1,2,3,4,2,4,9,8,7,99,2,1]
print(unique(l))
'''
'''def reverse(l):
    d=[]
    for i in range(1,len(l)+1):
        d.append(l[-i])
    return d
l=[1,2,3,4,5,6,7,8,9]
print(reverse(l))'''


'''def product(l):
    d=1
    for i in l:
        d=d*i
    return d
l=[1,2,3,4,5]
print(product(l))'''



'''def evenorodd(n):
    if n%2==0:
        print("even number")
    else:
        print("odd number")
def ispalindrome(n):
    t=n
    sum=0
    while(n!=0):
        r=n%10
        sum=sum*10+r
        n=int(n/10)
    if t==sum:
        print("palindrome")
    else:
        print("not palindrome")

def isarmstrong(n):
    t=n
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r*r*r
        n=int(n/10)
    if t==sum:
        print("armstrong")
    else:
        print("not armstrong")

n=int(input("enter any number:"))
evenorodd(n)
ispalindrome(n)
isarmstrong(n)'''


'''def func(a,b):
    print(a,b)

func(10,20)


def func(a,b):
    print(a)
    print(b)

c=20
d=10
func(b=d,a=c)


def func(a,b,c=10):
    print(a,b,c)

func(30,20,100)
func(30,47)

def func(*l):
    for i in l:
        print(i)

func(1,2,3,4,5)
'''

'''s=lambda x,y:x+y
sum=0
for i in range(1,11):
    sum=sum + s(0,i)

print(sum)'''


'''fact=lambda n:1 if n==1 else n*fact(n-1)
print(fact(6))'''
'''def func(l):
        if l%2==0:
            return True
        else:
            return False
l=[1,2,3,4,5,6]
print(list(filter(func,l)))'''

'''s=lambda x: 2**x
for i in range(1,6):
    print("2^",i,"=",s(i))
'''

'''m=int(input("enter ending term of the given series:"))
l=[]
for i in range(1,m+1):
    t=i
    ans=1
    while(t!=0):
        ans=ans*i
        t=t-1
    l.append(ans)
print(l)
s=[]
for i in range(1,m+1):
    ans=1
    while(i!=0):
        ans=ans*i
        i=i-1
    s.append(ans)
print(s)

sum=0
for i in range(len(l)):
    sum=sum+(l[i]/s[i])
print(sum)'''
'''class Rectangle:
    #length=int(input("enter length:"))
    #readth=int(input("enter breadth:"))
    def area(self):
        Rectangle.length=int(input("enter length:"))
        Rectangle.breadth=int(input("enter breadth:"))
        self.area=Rectangle.length*Rectangle.breadth
        return self.area
x=Rectangle()
print(x.area())
y=Rectangle()
print(y.area())
'''
'''import datetime
class Person:
    def __init__(self,dob):
        self.dob=dob
        return
    def verify(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today<datetime.date(today.year,self.dob.month,self.dob.day):
            age=age-1
        print(age)

x=Person(datetime.date(2002,12,9))
x.verify()'''
'''class Employee:
    cout=0
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        Employee.cout+=1
        return
    def display(self):
        print("Name:",self.name)
        print("Designation:",self.designation)
        print("salary:",self.salary)
        return
    def numberofemployee(self):
        print("Number of employees:",Employee.cout)

x=Employee("k","ceo",250000)
y=Employee("ki","ceo",25000000)
z=Employee("kiwi","ceo",250000000)
y.display()
z.numberofemployee()'''
    
'''class Students:
    def __init__(self):
        self.name=input("enter student name:")
        self.rollno=int(input("enter student roll number:"))
        self.marks=[]
        for i in range(3):
            self.mark=int(input("enter student marks:"))
            self.marks.append(self.mark)
        return
    def disp(self):
        print("Name:",self.name)
        print("Roll Number:",self.rollno)
        print("Marks:",self.total())
    def total(self):
        return sum(self.marks)

x=Students()
x.disp()'''
'''class bank:
    def __init__(self,amount):
        self.amount=amount
        return
    def withdraw(self,w):
        self.w=w
        if self.w>self.amount:
            print("Insufficient Balance")
        else:
            self.amount=self.amount-self.w
        self.balance()
    def deposit(self,d):
        self.d=d
        self.amount=self.amount+self.d
        self.balance()
    def balance(self):
        print("New Balance:",self.amount)

x=bank(100000)
for i in range(100):
    print("1.Withdraw")
    print("2.Deposit")
    m=int(input("Enter choice:"))
    if m==1:
        n=int(input("enter amount:"))
        x.withdraw(n)
    elif m==2:
        n=int(input("enter amount:"))
        x.deposit(n)
    else:
        break
'''
'''class book:
    def read(self):
        self.bookname=input("enter book name:")
        self.author=input("enter author name:")
        self.price=int(input("enter book price:"))
        return
    def dispay(self):
        print("title:",self.bookname)
        print("Author:",self.author)
        print("Price:",self.price)
        return
print("///////WELCOME TO LIBRARY//////")
b=[]
for i in range(100):
    print("1.Add book")
    print("2.Display Book")
    m=int(input("Enter choice:"))
    if m==1:
        x=book()
        x.read()
        b.append(x)
    elif m==2:
        for i in b:
            i.dispay()
    else:
        break
'''
'''class bill:
    d={1:["rice",3000],2:["meat",1000],3:["ice cream",100]}
    l=[]
    l1=[]
    l2=[]
    su=0
    def select(self):
        m=int(input("enter code of the product:"))
        n=int(input("enter quantity of the product:"))
        l3=[]
        l3=bill.d[m]
        bill.l1.append(l3)
        bill.l.append(m)
        bill.l2.append(n)
        return
    def bill(self):
        print("---------------BILL--------------")
        #print("---------------------------------")
        for i in range(len(bill.l1)):
            print("---------------------------------")
            print("code of the product:",bill.l[i])
            print("name of the product:",bill.l1[i][0])
            print("price of the product:",bill.l1[i][1])
            print("quantity of the product:",bill.l2[i])
            s=bill.l1[i][1]*bill.l2[i]
            bill.su=bill.su+s
            print("---------------------------------")
        print("total bill")
        print(bill.su)

class cash(bill):
    def pay(self):
        print("you have selected cash option")
        print("thank you for paying :",bill.su)
class cheque(bill):
    def pay(self):
        print("you have selected cheque option")
        print("thank you for paying :",bill.su)
    



x=bill()
print("AVAILABLE ITEMS:")
print(bill.d)
for i in range(100):
    print("1.order")
    print("2.exit")
    m=int(input("Enter choice:"))
    if m==1:
       x.select()
    elif m==2:
        x.bill()
        print("1.cash 2.cheque")
        n=int(input("Enter choice:"))
        if n==1:
            c=cash()
            c.pay()
        else:
            c=cheque()
            c.pay()
            break'''

'''class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        return
    def __add__(self,other):
        self.c=self.a+other.a
        self.d=self.b+other.b
        return(complex(self.c,self.d))

x=A(10,20)
y=A(10,20)
z=x+y
#p=complex(z[0],z[1])
#print(p)
print(z)'''
'''class A:
    def __init__(self,a):
        self.a=a
        return
    def __add__(self,other):
        return(self.a+other.a)

x=A(10)
y=A(20)
print(x+y)'''


'''class A:
    def __init__(self,a):
        self.a=a
        return
    def __isub__(self,other):
        self.a=self.a-other.a
        return(self.a)

x=A(10)
y=A(20)
x-=y
print(x)'''

'''import datetime
class A:
    def __init__(self,a):
        self.a=a
        return
    def __gt__(self,other):
        return(self.a>other.a)
    def __lt__(self,other):
        return(self.a<other.a)
    def __eq__(self,other):
        return(self.a==other.a)
x=A(datetime.date(2021,9,8))
y=A(datetime.date(2021,9,1))
print("x>y",x>y)
print("x<y",x<y)
print("x==y",x==y)'''




'''class sec:
    def __init__(self,sec):
        self.sec=sec
        return
    def display(self):
        print("Time in seconds:",self.sec)
        return


class hours:
    def __init__(self,minutes):
        self.hours=minutes
        return
    def display(self):
        print("Time in seconds:",self.hours)
        return

def hour(t):
    x=t.sec/60
    return x/60
def second(t):
    x=t.hours*60
    return x*60

a=sec(3600)
a.display()
print("Time in hours:",hour(a))

b=hours(2)
b.display()
print("Time in seconds:",second(b))'''

'''f=open("o1.txt","w")
f.write("seiou")
f.close()



f=open("o1.txt","r")
s=f.read()
s1=s.lower()
l=['a','e','i','o','u']
vowels=consonants=0
for i in s1:
    if i in l:
        vowels+=1
    else:
       consonants+=1

print(vowels)
print(consonants)
print((vowels/len(s))*100)
print((consonants/len(s))*100)'''
'''    
f=open("o1.txt","w")
f.write("seiou \t kjrgkj\n ukygrfirue  jgyuykj\t h")
f.close()


f=open("o1.txt","r")
s=f.read()
spaces=tabs=newline=0
for i in s:
    if i=='\t' :
        tabs+=1
    elif i==' ':
       spaces+=1
    elif i=='\n':
        newline+=1
    else:
        pass
print(tabs,spaces,newline)
'''
'''
import random
class randerror(Exception):
    pass
try:
    num=random.randint(-10,10)
    if num<0:
        raise randerror
except randerror:
    print("error generated")
else:
    print(num)
finally:
    print(num)'''

'''import random
s=random.randint(1,10)
try:
    m=int(input("enter guessing number:"))
except ValueError:
    print("Program Terminated.....")
else:
    if m>s:
        print("Too Large")
    elif m<s:
        print("Too small")
    else:
        print("Exactly")'''
'''import re
pat="[\w.-]+@[\w.-]+"
s="kowshik@gmail.com bvrsthg@cbit.ac.in bvrsthg@cbit.ac kopihyuhj"
l=re.findall(pat,s)
print(l)



import re
pat=r"\b[789]{1}[0-9]{9}"
s="9908517699 45664654654654 8074311341 4098798758"
l=re.findall(pat,s)
print(l)



import re
pat=r"\b[aeiou][\w]+[aeiou]\b"
s="aditya orange mexhanoic kjhkj surya mahesh apple"
l=re.findall(pat,s)
print(l)


import re
pat=r"\b[A-Z][\w]+"
s="There are five types of Iheritance"
l=re.findall(pat,s)
print(l)



import re
pat=r"\d{2}-\d{2}-\d{4}"
s="India got independance on 15-08-1947"
l=re.findall(pat,s)
print(l)




import re
pat=r"TS[0-9]{2}[A-Z]{2}[0-9]{1,4}"
s="TS08EM3444 AP29JH5666 TS09TH2"
l=re.findall(pat,s)
print(l)


import re
pat="-"
s="1601-20-748-031"
replace=""
l=re.sub(pat,replace,s)
print(l)

import re
pat="[,;:]"
s="ther are 5 types of inheritance,they are: single;multiple"
sub=" "
l=re.sub(pat,sub,s)
print(l)


import re
pat=r"[0-9]+ .*"
s="123 khjkbjnk"
l=re.findall(pat,s)
print(l)
'''




'''from tkinter import *
m=Tk()
m.title("Calculator")
m.geometry('350x500')
m.resizable(0,0)
def display(n):
    global num
    num=num+str(n)
    l1['text']=num
def clear():
    global num
    num=''
    l1['text']=num
def compute():
    global num
    result=str(eval(num))
    l1['text']=result
    num=''
num=''
var=StringVar()
frame1=Frame(m)
frame1.pack(expand=TRUE,fill=BOTH)
frame2=Frame(m)
frame2.pack(expand=TRUE,fill=BOTH)
frame3=Frame(m)
frame3.pack(expand=TRUE,fill=BOTH)
frame4=Frame(m)
frame4.pack(expand=TRUE,fill=BOTH)
frame5=Frame(m)
frame5.pack(expand=TRUE,fill=BOTH)
l1=Label(frame1,text="")
l1.pack(expand=TRUE,fill=BOTH)
b1=Button(frame1,text='1',command=lambda : display(1))
b1.pack(expand=TRUE,fill=BOTH,side=LEFT)
b2=Button(frame1,text='2',command=lambda : display(2))
b2.pack(expand=TRUE,fill=BOTH,side=LEFT)
b3=Button(frame1,text='3',command=lambda : display(3))
b3.pack(expand=TRUE,fill=BOTH,side=LEFT)
b4=Button(frame1,text='+',command=lambda : display('+'))
b4.pack(expand=TRUE,fill=BOTH,side=LEFT)
b5=Button(frame2,text='4',command=lambda : display(4))
b5.pack(expand=TRUE,fill=BOTH,side=LEFT)
b6=Button(frame2,text='5',command=lambda : display(5))
b6.pack(expand=TRUE,fill=BOTH,side=LEFT)
b7=Button(frame2,text='6',command=lambda : display(6))
b7.pack(expand=TRUE,fill=BOTH,side=LEFT)
b8=Button(frame2,text='-',command=lambda : display('-'))
b8.pack(expand=TRUE,fill=BOTH,side=LEFT)
b9=Button(frame3,text='7',command=lambda : display(7))
b9.pack(expand=TRUE,fill=BOTH,side=LEFT)
b10=Button(frame3,text='8',command=lambda : display(8))
b10.pack(expand=TRUE,fill=BOTH,side=LEFT)
b11=Button(frame3,text='9',command=lambda : display(9))
b11.pack(expand=TRUE,fill=BOTH,side=LEFT)
b12=Button(frame3,text='*',command=lambda : display('*'))
b12.pack(expand=TRUE,fill=BOTH,side=LEFT)
b13=Button(frame4,text='/',command=lambda : display('/'))
b13.pack(expand=TRUE,fill=BOTH,side=LEFT)
b16=Button(frame4,text='%',command=lambda : display('%'))
b16.pack(expand=TRUE,fill=BOTH,side=LEFT)
b14=Button(frame4,text='C',command=clear)
b14.pack(expand=TRUE,fill=BOTH,side=LEFT)
b15=Button(frame4,text='=',command=compute)
b15.pack(expand=TRUE,fill=BOTH,side=LEFT)

'''


'''from tkinter import *
m=Tk()
m.title("Registration Form")
m.geometry("400x400")
def display():
    print("Name:",x.get())
    print("EMAIL:",y.get())
    print("age:",z.get())
    print("number:",w.get())
    print("passsword:",k.get())
    if(t.get()==1):
        print("male")
    else:
        print("Female")
    print("registered successfully....")

x=StringVar()
y=StringVar()
z=StringVar()
w=StringVar()
k=StringVar()
t=IntVar()


b1=Label(m,text="name").grid(row=2,column=2)
a1=Entry(m,text=x)
a1.grid(row=2,column=4)

b2=Label(m,text="email").grid(row=3,column=2)
a2=Entry(m,text=y)
a2.grid(row=3,column=4)

b3=Label(m,text="age").grid(row=4,column=2)
a3=Entry(m,text=z)
a3.grid(row=4,column=4)

b4=Label(m,text="number").grid(row=5,column=2)
a4=Entry(m,text=w)
a4.grid(row=5,column=4)

b5=Label(m,text="password").grid(row=6,column=2)
a5=Entry(m,text=k)
a5.grid(row=6,column=4)

b6=Radiobutton(m,text='Male',variable=t,value=1).grid(row=7,column=2)
b6=Radiobutton(m,text='female',variable=t,value=2).grid(row=7,column=4)


b7=Button(m,text="submit",command=display)
b7.grid(row=9,column=4)'''

'''import turtle
m=turtle.Turtle()
def samp():
    for i in range(4):
        m.forward(100)
        m.left(90)

colors=['red','orange','green','yellow']
for i in range(1,5):
    m.color(colors[i-1])
    m.left(36)
    samp()
'''

'''import turtle,random
m=turtle.Turtle()
colors=['red','orange','green','yellow']
for i in range(0,360,36):
    m.color(random.choice(colors))
    m.seth(i)
    m.circle(100)
'''
'''from matplotlib import pyplot

d={'c++':20,'c':90,'java':50,'python':200}
x=list(d.keys())
y=list(d.values())
pyplot.bar(x,y)
pyplot.xlabel("courses offered")
pyplot.ylabel("students enrolled")
pyplot.show()
'''

'''import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=a+b
print("sum:",sum)'''
'''n=int(input("enter number of rows:"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()'''
'''class R:
    def __init__(self,s):
        self.s=s
        return
    def coutb(self):
        v=c=s=u=l=0
        for i in self.s:
            if i in ['a','e','i','o','u']:
                v=v+1
            elif i ==' ':
                s=s+1
            else:
                c=c+1
            if(i.islower()):
                l=l+1
            elif(i.upper()):
                u=u+1
        print(v,c,s,l,u)

s=input("enter string:")
x=R(s)
x.coutb()'''
'''class distance:
    def __init__(self,km,m,home):
        self.km=km
        self.m=m
        self.home=home
        print("home location:",self.home)
        print("distance of school from home in kms:",self.km)
        print("distance of school from home in ms:",self.m)
        return
class school(distance):
    def __init__(self,name,location,home,km,m):
        self.name=name
        self.location=location
        print("---distance from school---")
        print("name:",self.name)
        print("location:",self.location)
        distance.__init__(self,km,m,home)

class office(distance):
    def __init__(self,name,location,home,km,m):
        self.name=name
        self.location=location
        print("---distance from school---")
        print("name:",self.name)
        print("location:",self.location)
        distance.__init__(self,km,m,home)

d=school("bhashyam","panama","vansthalipuram",3,3000)
d1=office("amazon","gachibowli","vansthalipuram",30,30000)'''

'''class time_in_hrs:
    def __init__(self,hr):
        self.hr=hr
    def disp(self):
        print("time in hours:",self.hr)

class time_in_seconds:
    def __init__(self,sec):
        self.sec=sec
    def disp(self):
        print("time in seconds:",self.sec)

def seconds(t):
    x=t.hr*60
    return x*60

def hours(t1):
    x=t1.sec/60
    return x/60

x=time_in_hrs(5)
x.disp()
print("time in seconds:",seconds(x))

y=time_in_seconds(3600)
y.disp()
print("time in hours:",hours(y))'''

'''
f1=open("u1.txt","w")
f1.write("160120748031 9908517699 @gmail.com")
f1.close()




import re
pat=r"\b[A-Z][\w]+"
s="There are five types of Iheritance"
#l=re.search(pat,s,flags=2).group()
l=re.findall(pat,s)
print(l)
print(l)'''
'''import turtle
import random
m=turtle.Turtle()
colours=["green","yellow","orange"]
for i in range(0,360,36):
    m.color(random.choice(colours))
    m.seth(i)
    m.circle(100)

'''

'''import turtle,random
m=turtle.Turtle()
colours=["green","yellow","orange"]
def samp(t,s):
    m.color(random.choice(colours))
    for i in range(4):
        t.forward(100)
        t.right(90)

for i in range(50):
    m.left(18)
    samp(m,100)
'''


'''def fibb(n):
    if n==0 or n==1:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)

for i in range(10):
    print(fibb(i))



def gcd(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return gcd(b,rem)
print(gcd(10,20))



def expo(x,y):
    if y==0:
        return 1
    else:
        return x*expo(x,y-1)

print(expo(2,3))
import turtle
t=turtle.Turtle()
colours=["green","yellow","orange"]
while(True):
    for i in range(6):
        for colous in colours:
            t.color(colous)
            t.circle(100)
            t.left(20)
            t.hideturtle()
    '''
    



'''class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
m=complex(input("en"))
n=complex(input("en"))
k=int(input("en"))
l=int(input("en"))
x=A(m+k)
y=A(n+l)
print(x+y)'''


'''class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        return
    def __add__(self,other):
        self.c=self.a+other.a
        self.d=self.b+other.b
        return(complex(self.c,self.d))

x=A(10,20)
y=A(10,20)
z=x+y
#p=complex(z[0],z[1])
#print(p)
print(z)



class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        self.c=[]
        for i in range(3):
            d=[]
            for j in range(3):
                s=self.a[i][j]+other.a[i][j]
                d.append(s)
            self.c.append(d)
        return self.c

x=A([[1,2,3],[1,2,3],[1,2,3]])
y=A([[1,2,3],[1,2,3],[1,2,3]])
print(x+y)'''
import re
def decryptPassword(s):
    # Write your code here
    s1=list(s)
    l=len(s)
    pat='[1-9]'
    for i in range(len(s1)):
        if s1[i].islower() and s1[i+1].isupper():
            temp=s1[i]
            s1[i]=s1[i+1]
            s1[i+1]=temp
            s1.insert(i+2,'*')
        elif re.search(pat,s1[i]):
            t=s1[i]
            s1[i]='0'
            s1.insert(0,t)
    return s1
s="43Ah*ck0rr0nk"
l1=decryptPassword(s)
print(str(l1))
#print(list(s))
#print(s.isnum())



































