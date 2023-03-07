n=int(input("enter any number:"))
t1=0
t2=1
t3=0
sum=0
while t3<=n:
    t3=t1+t2
    if t3%2==0:
        sum+=t3
    t1=t2
    t2=t3
print(sum)    
