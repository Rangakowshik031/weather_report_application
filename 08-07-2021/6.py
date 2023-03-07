import re
s="hello cse4"
p="he"
if(re.match(p,s)):
    print("match is found")
else:
    print("non match")

s="inheritance is the one of the most important concept of OOP"
p="OOP"
if(re.search(p,s)):
    print("match is found")
else:
    print("non match")


s="inheritance is the one of the most important concept of OOP"
p="h"
s1=re.findall(p,s)
print(s1)
print("Number of time",p,"is repeated:",len(s1))


s="To create abstract classes we need to import ABC,@abstractmethod from abc module"
p="ABC"
text=re.finditer(p,s)
#print(text)
for text1 in text:
    print("pattern starts at:",text1.start())
    print("pattern ends at:",text1.end())
    print("Range in which pattern is present:",text1.span())


s="OOP- object oral programming"
p="oral"
p1="oriented"
s1=re.sub(p,p1,s)
print(s1)


s="OOP- object oral programming"
p="-"
s1=re.split(p,s)
print(s1)
