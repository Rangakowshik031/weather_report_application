a=input("enter your name")
b=int(input("enter your age:"))
try:
    if b<18:
        raise(Exception)
except Exception:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
