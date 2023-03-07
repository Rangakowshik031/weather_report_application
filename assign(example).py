print("/////WELCOME TO LUCKY RESTAURANT/////")
print("--------------------------------------")
print("AVAILABLE FOOD ITEMS")
print("BEVERAGES")
print("STARTERS")
print("NON-VEG MAIN COURSE")
print("VEG MAIN COURSE")
print("CHOCOLATE ICE-CREAM")
print("SWEETS")
p=int()
c=[]
l=[]
v=[]
for i in range(1,7):
    print("IF YOU WANT ORDER PRESS 1 ELSE PRESS 0")
    p=int(input("ENTER RESPONSE:"))
    if p==1:
        s=input("ENTER FOOD ITEM:")
        if s=='BEVERAGES':
            a=int(input("ENTER QUANTITY:"))
            price=300*a
            l.append(s)
            c.append(price)
            v.append(a)
        elif s=='STARTERS':
            a=int(input("ENTER QUANTITY:"))
            price=700*a
            l.append(s)
            c.append(price)
            v.append(a)
        elif s=='NON-VEG MAIN COURSE':
            a=int(input("ENTER QUANTITY:"))
            price=1000*a
            l.append(s)
            c.append(price)
            v.append(a)
        elif s=='VEG MAIN COURSE':
            a=int(input("ENTER QUANTITY:"))
            price=600*a
            l.append(s)
            c.append(price)
            v.append(a)
        elif s=='CHOCOLATE ICE-CREAM':
            a=int(input("ENTER QUANTITY:"))
            price=100*a
            l.append(s)
            c.append(price)
            v.append(a)
        elif s=='SWEETS':
            a=int(input("ENTER QUANTITY:"))
            price=200*a
            l.append(s)
            c.append(price)
            v.append(a)
        else:
            print("SORRY ITEM IS NOT AVAILAVLE")
    else:
       sum=0
       print("\n")
       print("I HOPE YOU STATISFIED WITH OUR DISHES")
       print("HERE IS YOUR BILL")
       print("----------------------------")
       for i in range(len(l)):
           print("FOOD ITEM :",l[i])
           print("QUANTITY:",v[i])
           print("PRICE: ",c[i])
           print("----------------------------")
           sum+=c[i]
       a=3*sum
       su= sum + a/100
       print("TOTAL BILL(+3% GST) :",su)
       break
print("THANK YOU SIR")
