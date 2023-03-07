'''class employee:
    name="abcd"
    designation="abcd"
    salaray=1582000
    cout=0
    def func(self):
        self.name=input("enter employee name:")
        self.designation=input("enter designation:")
        self.salary=int(input("enter salary:"))
    def disp(self):
        print(self.name,self.designation,self.salary)
        employee.cout+=1
    def coutb(self):
        print(employee.cout)
        
        
p=employee()
p.func()
p.disp()
q=employee()
q.func()
q.disp()
r=employee()
r.coutb()'''

'''import datetime
class student:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        a=today.year-self.dob.year
        print(a)
        print(today)
        if today < datetime.date(today.year,self.dob.month,self.dob.day):
            

p=student("k",datetime.date(2000,12,25))
p.check()'''


'''def func(l):
    l1=l.copy()
    print(l1)
    if(len(l)!=1):
        i=0
        while i<len(l):
            i=i+1
            del l[i]
        print(l,l1)
        if l1[-1]==l[-1]:
            del l[0]
        return func(l)
    elif len(l)==1:
        return l
            
        

l=[1,2,3,4,5,6,7,8,9,10]
c=func(l)
print(c)
'''
'''def func(l):
    l1=l.copy()
    if(len(l)!=1):
        i=1
        while(i<len(l)):
            l.pop(i)
            i=i+1
        if l1[-1]==l[-1]:
            l.pop(0)
        return func(l)
    elif len(l)==1:
        return l
n=int(input("enter number of soldiers:"))
lw=range(1,n+1)
l=list(lw)
c=func(l)
print("Last soldier who is alive:",c[0])'''


'''import csv
f=open("AttendanceList_20102021.csv","rb")
file1 = csv.DictReader(f)
file1 =file1.replace('\x00','?')
for col in file1:
    print('Month:',col['Full Name'] )'''





'''import xlrd

# Open the Workbook
workbook = xlrd.open_workbook("AttendanceList_20102021.xlsx")

# Open the worksheet
worksheet = workbook.sheet_by_index(0)

# Iterate the rows and columns
for i in range(0, 5):
    for j in range(0, 3):
        # Print the cell values with tab space
        print(worksheet.cell_value(i, j), end='\t')
    print('')
'''



'''import csv
f=open("Ro.csv","r")
file1 = csv.DictReader(f)
file = csv.reader(x.replace('\0', '') for x in file1) 
# creating empty lists
month = []
totalprofit = []
totalunit = []'''
 
# iterating over each row and append
# values to empty list
'''for col in file:
    month.append(col['S.NO'])'''
'''totalprofit.append(col['User Action'])
    totalunit.append(col['Timestamp'])'''
 
# printing lists
#print('Month:', month)
'''print('Moisturizer:', totalprofit)
print('Total Units:', totalunit)'''






'''import csv
 
with open('AttendanceList_20102021.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    reader = reader.replace('\x00','?')
    for row in reader:
        print(row)'''





'''import csv
from io import StringIO

with open('AttendanceList_20102021.csv',newline='',encoding='utf8') as f:
    data = f.read()
    data = data.replace('\x00','?')
    r = csv.DictReader(StringIO(data))
    for line in r:
        print(line)
'''



'''import pandas as pd

# Read CSV file into DataFrame df
df = pd.read_csv('AttendanceList_20102021.csv', index_col=0)

# Show dataframe
print(df)'''
'''import pandas as pd
df = pd.read_csv('AttendanceList_20102021.csv')
print(df.head())'''

'''import pandas as pd
df = pd.read_csv('AttendanceList_20102021.csv',encoding='utf-8')
print(df)'''


'''l=[10,10,10,20,0,10,10,10,10]
d={}
for i in range(3):
    s=l[i::3]
    d[i+1]=s
print(d)
z=[]
for i in range(3):
    s=0
    for j in range(len(d[i+1])):
        if d[i+1][j]>0:
            s=s+d[i+1][j]*1000
        elif d[i+1][j]==0:
            s=s-2000
    z.append(s)
    
print(z)'''

    

def rl(n,p,s):
    for i in range(p):
        s=ra(n,s)
    return s
    
def ra(n,s):
    first=s[0]
    for i in range(n-1):
        s[i]=s[i+1]
    s[n-1]=first
    return s
n=int(input("Enter number of customers:"))
p=int(input("Enter number of sweet boxes:"))
s=list(range(1,n+1))
print("order of buliding:")
for i in rl(n,p,s):
    print(i, end=" ")























































