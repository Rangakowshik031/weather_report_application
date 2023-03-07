s=str(input("enter any string:"))
i=0
c=0
for i in s:
    c=c+1
print(c)
dic={}
for j in s:
    dic[j]=s.count(j)
print(dic)
