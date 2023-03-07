'''from tkinter import *
root=Tk()
root.geometry("350x500")
root.title("calculator")
root.resizable(0,0)
def display(n):
    global num
    num=num+str(n)
    l1['text']=num
def clear():
    global num
    num=""
    l1['text']=num
def compute():
    global num
    result=str(eval(num))
    l1['text']=result
    num=''
num=''
var=StringVar()
frame1=Frame(root)
frame1.pack(expand=TRUE,fill=BOTH)
frame2=Frame(root)
frame2.pack(expand=TRUE,fill=BOTH)
frame3=Frame(root)
frame3.pack(expand=TRUE,fill=BOTH)
frame4=Frame(root)
frame4.pack(expand=TRUE,fill=BOTH)
frame5=Frame(root)
frame5.pack(expand=TRUE,fill=BOTH)
l1=Label(frame1,text="")
l1.pack(expand=TRUE,fill=BOTH)
b1=Button(frame1,text='1',border=0,command=lambda:display(1))
b1.pack(expand=TRUE,fill=BOTH,side=LEFT)
b2=Button(frame1,text='2',command=lambda:display(2))
b2.pack(expand=TRUE,fill=BOTH,side=LEFT)
b3=Button(frame1,text='3',command=lambda:display(3))
b3.pack(expand=TRUE,fill=BOTH,side=LEFT)
b4=Button(frame1,text='+',command=lambda:display('+'))
b4.pack(expand=TRUE,fill=BOTH,side=LEFT)
b5=Button(frame2,text='4',command=lambda:display(4))
b5.pack(expand=TRUE,fill=BOTH,side=LEFT)
b6=Button(frame2,text='5',command=lambda:display(5))
b6.pack(expand=TRUE,fill=BOTH,side=LEFT)
b7=Button(frame2,text='6',command=lambda:display(6))
b7.pack(expand=TRUE,fill=BOTH,side=LEFT)
b8=Button(frame2,text='*',command=lambda:display('*'))
b8.pack(expand=TRUE,fill=BOTH,side=LEFT)
b9=Button(frame3,text='7',command=lambda:display(7))
b9.pack(expand=TRUE,fill=BOTH,side=LEFT)
b10=Button(frame3,text='8',command=lambda:display(8))
b10.pack(expand=TRUE,fill=BOTH,side=LEFT)
b11=Button(frame3,text='9',command=lambda:display(9))
b11.pack(expand=TRUE,fill=BOTH,side=LEFT)
b12=Button(frame3,text='/',command=lambda:display('/'))
b12.pack(expand=TRUE,fill=BOTH,side=LEFT)
b13=Button(frame4,text='C',command=clear)
b13.pack(expand=TRUE,fill=BOTH,side=LEFT)
button_equal=Button(frame4,text='=',command=compute)
button_equal.pack(expand=TRUE,fill=BOTH,side=LEFT)
'''   




'''l=['1','4','9']
d=[]
s=0
for i in range(100,200):
    d1=[]
    c=0
    while(i):
        rem=i%10
        d1.append(rem)
        i=int(i/10)
    #print(d1)
    #print(i)
    for j in range(len(d1)):
        if d1[j]==1 or d1[j]==4 or d1[j]==9:
            c=c+1
    if c==3:
        s=s+1
        
print(s)'''
        
'''n=int(input("enter:"))
m=int(input("enter:"))
for i in range(1,n):
    for j in range(1,n):
        c=4*i+j*2
        if c==m and m%2==0 and i+j==n :
            print(i,j)
            break'''



'''n=int(input("enter:"))
for i in range(1,n):
    s=0
    for j in range(i+1,n):
        if i+j==n and j==i+1 :
            print(i,j)'''


'''n=int(input("enter:"))
l=[0,0]
d={}
for i in range(1,n+1):
    #r=i%4
    x=10
    for j in range(10):
        if i==1+4*j:
            l[0]+=i*x
            x=x+10
            d[i]=l
            print(d[i])
            break
        elif i==2+4*j:
            l[1]+=i*x
            x=x+10
            d[i]=l
            print(d[i])
            break
        elif i==3+4*j:
            l[0]-=i*x
            x=x+10
            d[i]=l
            print(d[i])
            break
        elif i==4+4*j:
            l[1]-=i*x
            x=x+10
            d[i]=l
            print(d[i])
            break

print(d[n])'''

'''l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        n=int(input("enter:"))
        l1.append(n)
    l.append(l1)
print(l)
s=[]
for i in range(3):
    l1=[]
    for j in range(3):
        l1.append(l[j][i])
    s.append(l1)
print(s)
f=[]
for i in range(3):
    l1=[]
    s1=0
    for j in range(3):
        s1=s1+l[i][j] 
    f.append(s1)
print(f)

if min(f)>70:
    print("all are fit")


maxi=max(f)

for i in range(3):
    if maxi==f[i]:
        print(i+1)
        '''





'''n=int(input("enter:"))
#p=int(input("enter number of students:"))
d={}
for i in range(n):
    p=int(input("enter number of students:"))
    l=[]
    s=[]
    k1=[]
    for j in range(p):
        pi=int(input("enter:"))
        s.append(pi)
    for k in range(p):
         pi=int(input("enter:"))
         k1.append(pi)
    l.append(s)
    l.append(k1)
    d[i]=l
print(d)
print(d[0][1])

for i in range(n):
    if d[i][i][i]==d[i][i+1][i]:
        p=p+1
    else:
        j=0
        q=d[i][j][j+1]-d[i][j][j]
        if q== d[i][j+1][j+1]:
            p=p+1
        j=j+1
        if j==2:
            break'''

'''n=int(input("enter:"))
p=int(input("enter:"))
r=int(input("enter size:"))
l=[]
for i in range(r):
    d=int(input('enter element:'))
    l.append(d)
c=n*p
sum=0
for i in range(r):
    sum=sum+l[i]
    if sum>=c:
        print(i+1)
        break'''


print(1&0)
    





































