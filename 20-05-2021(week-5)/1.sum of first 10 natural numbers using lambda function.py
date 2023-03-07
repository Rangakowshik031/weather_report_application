s=lambda x,y:x+y
n=10
sum=0
i=1
for num in range(1,6):
    j=i+1
    sum+=s(i,j)
    i=i+2
print("sum of first 10 natural numbers=",sum)
