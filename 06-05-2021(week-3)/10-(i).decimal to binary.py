d=int(input("enter decimal number="))
b=0
i=0
while(d!=0):
    r=d%2
    b=b+r*(10**i)
    d=d//2
    i=i+1
print(" the bninary number is ",b)


b=int(input("enter binary number="))
d=0
i=0
while(b!=0):
    r=b%10
    d=d+r*(2**i)
    b=b//10
    i=i+1
print(" the bninary number is ",d)
