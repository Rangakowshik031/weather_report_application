import datetime
from datetime import timedelta

print("--------MENU-------")
print("1.Magazines")
print("2.Books")
n=int(input("Enter your choice :"))
if(n==1):
    print("Magazines are not issued to students but students can read in library")
elif(n==2):
    print("Books can be issued to students")
    
else:
    print("Invalid choice")

    
class s:
    st={}
    book=[]
    def inf(self,a,b,c1,d1,e1,f1):
        self.a=a  #name
        self.b=b  #roll number
        self.c1=c1 #semester
        self.d1=d1  #branch
        self.e1=e1   #cards
        self.f1=f1
        c=[]
        c.append(self.a)
        c.append(self.c1)
        c.append(self.d1)
        c.append(self.e1)
        c.append(self.f1)
        s.st[self.b]=c
        return
x=s()
x.inf("kowshik",106,2,"cse",2,[["BS GREWAL ENGINEERING MATHS",datetime.date(2021,6,1)],["VERBAL COMMNUNICATION",datetime.date(2021,6,1)]])

print("---------WELCOME TO CBIT LIBRARY-----------")
print("-----------------MENU-----------------")
print("1.ADD STUDENT")
print("2.ISSUE BOOKS")
print("3.RETURN BOOKS")
print("4.DISPLAY STUDENT INFORMATION")
print("5.EXIT")
for i in range(100):
    print("---------------------------------------------------")
    qa=int(input("Enter code:"))
    if qa==1:
        x=s()
        a=int(input("Enter student Roll number:"))
        if a not in list(s.st.keys()):
            b=input("Enter student name:")
            c=int(input("Enter semseter perceiving:"))
            d=input("Enter branch:")
            e=[b,c,d,0,[]]
            s.st[a]=e
        else:
            print("Already registered")
        #print("Present data:",s.st)
    elif qa==2:
        d={1:"BS GREWAL ENGINEERING MATHS",2:"PYTHON PROGRAMMING BY REENA THAREJE",3:"S CHAND ENGINEERING CHEMISTRY",4:"CAD",5:"VERBAL COMMUNICATION"}
        a=int(input("Enter your roll no:"))
        #print(s.st.keys())
        x=list(s.st.keys())
        #print(x)
        if a in x:
            if (s.st[a][3]>=4):
                print("You have used your all cards")
            else:
                print("You have",4-s.st[a][3],"cards available")
                for i in range(4-s.st[a][3]):
                    print("1.Select books")
                    print("2.Exit")
                    m=int(input("Enter response:"))
                    if m==1:
                        print("Available books:")
                        print(d)
                        n=int(input("Enter code of the book:"))
                        if n in (list(d.keys())):
                            print("You have selected :",d[n])
                            print("Return date=",datetime.date.today()+timedelta(days=30))
                            s.st[a][3]+=1
                            l=[]
                            l.append(d[n])
                            l.append(datetime.date.today())
                            s.st[a][4].append(l)
                        else:
                            print("Invalid code")
                    else:
                        break
                else:
                    print("U have used all your cards")
        else:
            print("U need to register")
            
    elif qa==3:
        a=int(input("Enter your roll no:"))
        if a in list(s.st.keys()):
            print("PLEASE SUBMIT THE BOOK HERE")
            print("SCANNING THE QR CODE")
            m=input("Enter Book name:")
            for i in range(len(s.st[a][4])):
                if (s.st[a][4][i][0]==m):
                    print("Issued on:",s.st[a][4][i][1])
                    print("Return date:",s.st[a][4][i][1]+timedelta(days=30))
                    d=input("Enter the date of Return (YY-MM-DD)=")
                    year,month,day=map(int,d.split('-'))
                    d=datetime.date(year,month,day)
                    print("Returned on:",d)
                    aq=s.st[a][4][i][1]+timedelta(days=30)
                    s.st[a][3]=s.st[a][3]-1
                    #print("number of cards used :",s.st[a][3])
                    asss=aq +timedelta(days=5)
                    if(asss<d):
                        assss=d-asss
                        print("You need to pay:",assss.days,"Rupees")
                        print("Number of cards available :",4-s.st[a][3])
                        s.st[a][4].pop(i)
                        break
                    else:
                        print("Number of cards available :",4-s.st[a][3])
                        print("Thank you")
                        break
        else:
            print("invalid roll no")
    elif qa==4:
        a=int(input("enter your roll no:"))
        if a in list(s.st.keys()):
            print("Student name:",s.st[a][0])
            print("Student current perceiving semester:",s.st[a][1])
            print("Student branch:",s.st[a][2])
            print("Number of cards used :",s.st[a][3])
            print("Number of cards unused :",4-s.st[a][3])
        else:
            print("No such student")
        
    elif qa==5:
        print("-----THANK YOU-----")
        break
    else:
        print("Invalid code")
    print("---------------------------------------------------")

#print(s.st)


