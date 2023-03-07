
def Ispalindrome():
    s=input("enter any string:")
    b=""
    b=s[::-1]
    if s==b:
        print("given string is palindrome")
    else:
        print("given string is not palindrome") 
