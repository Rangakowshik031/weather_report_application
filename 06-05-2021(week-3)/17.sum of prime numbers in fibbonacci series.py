l=[]
t1=0
t2=1
t3=0
i=0
sum=0
l.append(t1)
l.append(t2)
while t3<=2000000:
    t3=t1+t2
    l.append(t3)
    t1=t2
    t2=t3
print(l)
d=len(l)
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        #print(i)
        sum=sum+i
print("sum of prime numbers in fibbonacci series=",sum)
