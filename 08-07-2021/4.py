import random
for i in range(5):
    s=random.randint(20,60)
    print("Random number:",s)
    try:
        m=int(input("enter any number:"))
    except ValueError:
        print("You have not entered number")
    else:
        if m>s:
            print("Too large")
        elif m<s:
            print("Too small")
        else:
            print("Equal")
        

#s=int(input("enter:"))
    
    
