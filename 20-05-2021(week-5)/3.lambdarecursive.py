n=int(input("enter any number:"))
f=lambda n:1 if n==0 else n*f(n-1)
print(f(n))
