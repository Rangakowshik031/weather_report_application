def Evenorodd(n):
    if n%2==0:
        print("even number")
    else:
        print("odd number")


def Isarmstrong(p):
    t=p
    sum=0
    while p>0:
        rem=p%10
        sum=sum+rem*rem*rem
        p=int(p/10)
    if sum==t:
        print("given number is armstrong number")
    else:
        print("given number is not armstrong number")

def Ispalindrome(s):
    b=""
    b=s[::-1]
    if s==b:
        print("given string is palindrome")
    else:
        print("given string is not palindrome")
    

m=int(input("enter any number to check whether it is even or odd="))
Evenorodd(m)
a=int(input("enter any number to check whether it is armstrong or not="))
Isarmstrong(a)
s=input("enter any string=")
Ispalindrome(s)
