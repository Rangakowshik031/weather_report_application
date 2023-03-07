'''f=open("e1.txt","w")
f.write("hello\n ji ijksbnioj\n jyguvhjbjk")
f.close()'''

'''f=open("e1.txt","rb")
print(f.read().decode("utf-8"))
f.close()'''


'''a="hi"
b="hello hi"
import re
i=re.match(a,b)
if(i):print("matched")
else:print("non match")'''

'''a="hi"
b="hello hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")'''

'''a="hi"
b="hello hi"
c="hoe"
import re
i=re.sub(a,c,b)
print(i)'''

'''a="hi"
b="hello hi hello hu hi  hih hi"
import re
i=re.findall(a,b)
print(i)'''

'''a=r"^hi"
b="h helo"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")


a=r"hi$"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a=r"hi."
b="h helo hiy"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a="[a-z]"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a="[^h]"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a="[u]*"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a="[u]+"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")


a="[h]?"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")


a="h{1}"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a="h{1,}"
b="h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")

a="a{1,3}"
b="h helo hhi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")


a="/da"
b="9h helo hi"
import re
i=re.search(a,b)
if(i):print("matched")
else:print("non match")'''


for i in range(2,10):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)


class A:
    def m1(self):
        print("hello")
        return

class B:
    def m2(self):
        self.a=A()
        self.a.m1()


a=B()
a.m2()

from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass
class A:
    def m1(self,a):
        self.a=a
        print("i am from m1")
        return
    def m1(self,a,b):
        self.a=a
        self.b=b
        print("i am from m1")
        return

x=A()
x.m1(1,3)

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return(self.a+other.a)

z=A(10)
y=A(20)
print(z+y)






























