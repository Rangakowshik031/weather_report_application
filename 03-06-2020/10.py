class store:
    d={1:["rice",3500],2:["chips",70],3:["chocolates",50],4:["ice creams",30]}
    l1=[]
    l2=[]
    l=[]
    def select(self):
        m=int(input("ENTER THE CODE OF THE PRODUCT:"))
        n=int(input("ENTER QUANTITY OF THE PRODUCT:"))
        l3=[]
        l3=store.d[m]
        store.l2.append(m)
        store.l1.append(l3)
        store.l.append(n)
    def bill(self):
        print("------------BILL--------------")
        print(store.l1)
        print(store.l)
        su=0
        for i in range(len(store.l1)):
            print("-------------------------------")
            print("CODE PRODUCT:",store.l2[i])
            print("NAME OF THE ITEM:",store.l1[i][0])
            print("PRICE OF THE PRODUCT:",store.l1[i][1])
            print("QUANTITY OF THE PRODUCT:",store.l[i])
            s=store.l1[i][1]*store.l[i]
            print("TOTAL PRICE:",s)
            su=su+s
            print("--------------------------------")
        print("---------TOTAL BILL-----------")
        print(su)
            

a=store()
print("WELCOME TO DMART")
print("AVAILABLE FOOD ITEMS")
print(store.d)
print("--------------------------")
print("SELECT OPTION 1 FOR SHOP")
print("SELECT OPTION 0 FOR EXIT")
print("--------------------------")
for i in range(1,100):
    m=int(input("ENTER RESPONSE:"))
    if m==1:
        a.select()
    else:
        a.bill()
        break
        

