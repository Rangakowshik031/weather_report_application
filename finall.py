import pandas as pd
df = pd.read_excel('k1.xlsx')
a=df.head(200)
d1=pd.DataFrame(a)
n={}
for i in range(199):
    l=[]
    s=d1.loc[i]['Column1']
    d=d1.loc[i]['Column2']
    e=d1.loc[i]['Column3']
    l.append(d)
    l.append(e)
    n[s]=l
    
    

import datetime
n1={}
for i in range(199):
    l=[]
    s=d1.loc[i]['Column1']
    n[s]=l
del n['Full Name']
del n['Si R. Srikanth']
k=n.keys()
l1=len(k)
l=sorted(k)
d33={}
for i in range(len(l)):
    p=[]
    s=l[i]
    for j in range(199):
        q=[]
        if d1.loc[j]['Column1']==l[i]:
            x=d1.loc[j]['Column2']
            y=d1.loc[j]['Column3']
            q.append(x)
            q.append(y)
            p.append(q)
    d33[s]=p
d44={}
time_str2 = ' 9:10:00 AM'
xc=datetime.datetime.strptime(time_str2," %H:%M:%S AM")
mm=[]
for i in range(l1):
    sd=[]
    tim_str3=' 0:00:00 AM'
    su=datetime.datetime.strptime(tim_str3," %H:%M:%S AM")
    for j in range(len(d33[l[i]])):
        if d33[l[i]][j][0]=='Joined':
            s=d33[l[i]][j][1]
            aw=s.split(',')
            aw.pop(0)
            t1= datetime.datetime.strptime(aw[0],' %H:%M:%S AM')
            su=t1-su
            dt1 = datetime.datetime.strptime(str(su), "%H:%M:%S")
            dt=dt1.time()
            sd.append(dt)
            su=t1
        else:
            #print(d33[l[i]][j][1])
            s=d33[l[i]][j][1]
            aw=s.split(',')
            aw.pop(0)
            t1= datetime.datetime.strptime(aw[0],' %H:%M:%S AM')
            su=t1-su
            dt1 = datetime.datetime.strptime(str(su), "%H:%M:%S")
            dt=dt1.time()
            sd.append(dt)
            su=t1
    sd.pop(0)
    t0=datetime.datetime.strptime(' 00:00:00 AM', ' %H:%M:%S AM')
    t00=t0.time() 
    for i1 in sd:
        t000=t00.hour+i1.hour+(t00.minute+i1.minute+(t00.second+i1.second)//60)//60
        t001=(t00.minute+i1.minute+(t00.second+i1.second)//60)%60
        t002=(t00.second+i1.second)%60
        t00=datetime.time(t000,t001,t002)
    p0=str(t000)
    p1=str(t001)
    p2=str(t002)
    p3=p0+':'+p1+':'+p2
    mm.append(p3)
    d44[l[i]]=p3
for i in range(l1):
    print(l[i],':',d44[l[i]])
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
l1=list(n.keys())
import pandas as pd
df1 = pd.read_excel('roll.xlsx')
a1=df1.head(100)
d=pd.DataFrame(a1)
l=[]
for i in range(66):
    s=d.loc[i]['Name of the Candidate']
    l.append(s)
l1=sorted(l1)
l=sorted(l)
cds=[]
for i in range(len(l)):
    if l[i] not in l1:
        cds.append(l[i])
n4={}
for i in range(66):
    s1=d.loc[i]['Roll No.']
    d1=d.loc[i]['Name of the Candidate']
    n4[d1]=s1
kl=list(n4.keys())
for i in cds:
    for j in kl:
        if i==j:
            print(i,n4[j])
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
