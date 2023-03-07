m=int(input("enter any number="))
l=[]
for i in range(1,m+1):
    b=1
    while(i!=0):
        b=b*i
        i=i-1
    l.append(b)
print("factorial terms=",l)


s=[]
for i in range(1,m+1):
    c=1
    d=i
    while(d!=0):
        c=c*i
        d=d-1
    s.append(c)
print("exponent terms",s)

sum=0
for i in range(len(l)):
    sum = sum + (s[i]/l[i])
print("sum of the series=",sum)
        
