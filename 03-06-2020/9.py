def bank(m):
    if m==1:
        print("you selected withdraw option")
        print("Available money in your bank account is :",p)
        r=int(input("enter money to withdraw:"))
        if r>p:
            print("sorry insufficient balance")
        else:
            a=p-r
            print("balance=",a)
    else:
        q=int(input("enter money to deposit:"))
        print("money deposited now:",q)
        print("Total balnce",p+q)



print("Welcome to SBI bank")
print("For withdraw enter 1 ")
print("For deposit enter 0 ")
p=200000
m=int(input("select option:"))
bank(m)
