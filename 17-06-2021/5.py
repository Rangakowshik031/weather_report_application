class bill:
    d={1:["rice",900],2:["starters",700],3:["roti",50],4:["ice creams",30]}
    l1=[]
    l2=[]
    l=[]
    su=0
    def select(self):
        m=int(input("ENTER THE CODE OF THE PRODUCT:"))
        n=int(input("ENTER QUANTITY OF THE PRODUCT:"))
        l3=[]
        l3=bill.d[m]
        bill.l2.append(m)
        bill.l1.append(l3)
        bill.l.append(n)
    def bill_1(self):
        print("------------BILL--------------")
        #print(store.l1)
        #print(store.l)
        #su=0
        for i in range(len(bill.l1)):
            print("-------------------------------")
            print("CODE PRODUCT:",bill.l2[i])
            print("NAME OF THE ITEM:",bill.l1[i][0])
            print("PRICE OF THE PRODUCT:",bill.l1[i][1])
            print("QUANTITY OF THE PRODUCT:",bill.l[i])
            s=bill.l1[i][1]*bill.l[i]
            print("TOTAL PRICE:",s)
            bill.su=bill.su+s
            print("--------------------------------")
        print("---------TOTAL BILL-----------")
        print(bill.su)

class CASH(bill):
    def pay(self):
        print("YOU HAVE SELECTED CASH OPTION")
        print("THANK YOU FOR PAYING THE BILL OF AMOUNT:",bill.su)
        return

class CHEQUE(bill):
    def pay(self):
        print("YOU HAVE SELECTED CHEQUE OPTION")
        print("THANK YOU FOR PAYING THE BILL OF AMOUNT:",bill.su)
        return

a=bill()
print(bill.d)
print("--------------------------")
print("SELECT OPTION 1 FOR ORDER")
print("SELECT OPTION 0 FOR EXIT")
print("--------------------------")
for i in range(1,100):
    m=int(input("ENTER RESPONSE:"))
    if m==1:
        a.select()
    else:
        a.bill_1()
        n=int(input("enter option 1 for cash option 2 for cheque"))
        if n==1:
            c=CASH()
            c.pay()
        else:
            c=CHEQUE()
            c.pay()
        break
