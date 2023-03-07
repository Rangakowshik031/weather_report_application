

'''x="hello hi "
y=" "
import re
z="@"
i=re.sub(y,z,x)
print(i)'''



'''x="hello,have,nice good , better..."
y=" "
y1="."
y2=","
import re
z=":"
i=re.sub(y,z,x,2)
j=re.sub(y1,z,i,2)
k=re.sub(y2,z,j,2)
print(k)
'''


'''x=r"ahjjkkb"
y="ajhkll"
pat="a.*?b$"
import re
i=re.search(pat,y)
if(i):print("yes")
else:print("no")'''



'''x="AaSsvv"
pat="[A-Z]"
pat1="[a-z]"
import re
c=0
for i in range(len(x)):
    r=i%2
    if r==0:
        j=re.search(pat,x[i])
        if(j):
            #print("yes")
            c=c+1
        else:
            #print("no")
            c=0
            break
    else:
        j=re.search(pat1,x[i])
        if(j):
            #print("yes")
            c=c+1
        else:
            #print("no")
            c=0
            break

if(c==0):print("non match")
else:print("match")'''


'''x="ab{2,3}"
y="abbbbbbbbbbbbbbbbb"
import re
#z="@"
i=re.search(x,y)
if(i):print("match")
else:print("non match")'''

'''pat="43{2}5"
if(re.search(pat,"435")):print("match")
else:print("non match")'''


'''a=10
b=0
try:
    rem=a//b
except Exception:
    print("false")
else:
    print("hi")
finally:
    print("byr")'''

a=[[1,2],[3,4]]
print(len(a))












