#fibbonacci series
def fibbo(n):
    if n==1 or n==0:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)



m=int(input("enter number of terms="))
i=0
while i<m:
    print(fibbo(i))
    i=i+1


#exponent
def exponent(x,y):
    if y<1:
        return 1
    else:
        return x*exponent(x,y-1)



m=int(input("enter base="))
p=int(input("enter power="))
a=exponent(m,p)
print(a)


#gcd
def gcd(m,n):
    rem=m%n
    if rem==0:
        return n
    else:
        return gcd(n,rem)

m=int(input("enter any number="))
n=int(input("enter any number="))
print(gcd(m,n))

