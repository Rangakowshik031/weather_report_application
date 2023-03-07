n=int(input("enter any number:"))
t=n
sum=0
while n>0:
    rem=n%10
    sum+=rem*rem*rem
    n=int(n/10)
if t==sum:
    print("given number is a armstrong number")
else:
    print("given number is not a armstrong number")
