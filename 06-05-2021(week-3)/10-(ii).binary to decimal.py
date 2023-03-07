b=int(input("enter binary number"))
d=0
i=0
while(b!=0):
    r=b%10
    d=d+r*(2**i)
    b=b//10
    i=i+1
print(" the bninary number is ",d)
