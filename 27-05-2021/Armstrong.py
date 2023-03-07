
def Checkarmstrong():
    p=int(input("enter any number:"))
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
