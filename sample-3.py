'''def func(l):
    p=[]
    for i in l:
        if i not in p:
            p.apppend(i)
    return p
            

l=[1,2,3,3,3,2,2]
c=func(l)
print(c)'''

'''n=4
count=0
for i in range(n):
    print()
    for j in range((n-1)-i):
        print(end="  ")
    for k in range((2*i)+1):
        if k<=i:
            print(k+1,end=" ")
        else:
            count=count+1
            k=i+1-count
            print(k,end=" ")
    count=0'''
'''
m=int(input("enter number of rows:"))
count=0
for i in range(m):
    print()
    for j in range((m-1)-i):
        print(end="  ")
    for k in range((2*i)+1):
        if k<=i:
            print(k+1,end=" ")
        else:
            count+=1
            k=i+1-count
            print(k,end=' ')
 count=0'''
'''l=['1','2','3']
d=str(l)
print(d)
list1 = ['1', '2', '3']
str1 = ''.join(list1)
print(str1)
print(list1[-1])'''





'''def longestSubarray(arr):
    l=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i-j==1 or j-i==1:
                l.append(j)
    print(l)
    return len(l)

arr=[2,2,1]
s=longestSubarray(arr)
print(s)'''


'''def stringAnagram(dictionary, query):
    l=[]
    for j in range(len(query)):
        c=0
        for i in range(len(dictionary)):
            p=''.join(sorted(dictionary[i]))
            q=''.join(sorted(query[j]))
            print(p,q)
            if p==q:
                c=c+1
                print(c)
        l.append(c)
    return l

dictionary=['heater','cold','clod','reheat','docl']
query=['codl','heater','abcd']
x=stringAnagram(dictionary, query)
print(x)'''

'''def stringAnagram(dictionary, query):
    l=[]
    l1=[]
    l2=[]
    for i in query:
        p=''.join(sorted(i))
        l1.append(p)
    for j in dictionary:
        p=''.join(sorted(j))
        l2.append(p)
        
    for j in range(len(l1)):
        c=0
        for i in range(len(l2)):
            if l2[i]==l1[j]:
                c=c+1
                #print(c)
        l.append(c)
    return l

dictionary=['heater','cold','clod','reheat','docl']
query=['codl','heater','abcd']
x=stringAnagram(dictionary, query)
print(x)'''


'''s='bcda'
d=''.join(sorted(s))
print(d)'''








'''def solve(arr,query):
	dict={}
	for s in arr:
		i=str(sorted(s))
		if i in dict:
			dict[i]+=1
		else:
			dict[i]=1
	print(dict)
	ans=[]
	for s in query:
		i=str(sorted(s))
		if i in dict:
			ans.append(dict[i])
		else:
			ans.append(0)
	return ans

arr=['heater','cold','clod','reheat','docl']
query=['codl','heater','abcd']

s=solve(arr,query)
print(s)'''


'''# Python3 implementation to find the
# longest subarray consisting of
# only two values with difference K

# Function to return the length
# of the longest sub-array
def longestSubarray (arr):
	Max = 1
	s = set()
	for i in range(len(arr) - 1):
		s.add(arr[i])
		for j in range(i + 1, len(arr)):
			if (abs(arr[i] - arr[j]) == 0 or
				abs(arr[i] - arr[j]) == 1):
				if (not arr[j] in s):
					if (len(s) == 2):
						break
					else:
						s.add(arr[j])
						
			else:
				break

		if (len(s) == 2):
			Max = max(Max, j - i)
			s.clear()

		else:
			s.clear()

	return Max


if __name__ == '__main__':
	
	arr = [1,2,3,4,5]

	N = len(arr)
	K = 1

	length = longestSubarray(arr)

	if (length == 1):
		print("-1")
	else:
		print(length)

# This code is contributed by himanshu77'''


'''def sortedSum(a):
    l=[]
    l1=[]
    su=0
    for i in range(len(a)):
       l.append(a[:i+1])
    for i in range(len(l)):
        su=0
        for j in range(len(l[i])):
            d=sorted(l[i])
            su=su+(j+1)*d[j]
            print(su)
        l1.append(su)
    print(sum(l1))
            
a=[9,5,8]
print(sortedSum(a))'''

'''def sortedSum(a):
    l=[]
    l1=[]
    su=0
    for i in range(len(a)):
       l.append(a[:i+1])
    i=0
    n=len(l)-1
    while(i<=n-1):
        for j in range(len(l[i])):
            d=sorted(l[i])
            su=su+(j+1)*d[j]
            print(su)
            l1.append(su)
        i=i+1
    print(sum(l1))
a=[9,5,8]
print(sortedSum(a))'''

'''m=int(input("enter:"))
n=int(input("enter:"))
l=[]
for i in range(1,m+1):
    if m%i==0:
        l.append(i)
l1=sorted(l)
if n<len(l1):
    print(l1[n-1])
else:
    print("1")'''


'''z="hel h"
x=z.split(" ")
print(x)'''

'''n=int(input())
d={}
l1=[]
for i in range(n):
    l=[]
    p=input()
    z=p.split(" ")
    d[i]=z
print(d[0][1])
for i in range(n):
    p=input()
    l1.append(p)
for i in range(n):
    if d[i][0]==l1[i]:
        print(l[i],'=',d[i][1])
    else:
        print("Not found")'''



'''d=int(input("enter decimal number="))
b=0
i=0
c=0
while(d!=0):
    r=d%2
    b=b+r*(10**i)
    d=d//2
    i=i+1
print(" the bninary number is ",b)

s=str(b)
print(s)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
#print(c)
if c==0 and s.count('1')>1:
    print('1')
else:
    print(c)
'''




'''import csv  

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)



import csv

mydict = {}

with open('csv_file.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

print(dict_from_csv)'''




'''r=range(1,5)
x=list(r)
print(x)
j=1
while(j<len(x)):
    x.pop(j)
    j=j+1
print(x)
j=1
while(j<len(x)):
    x.pop(j)
    j=j+1
print(x)
j=1
while(j<len(x)):
    x.pop(j)
    j=j+1
print(x)
j=1
while(j<len(x)):
    x.pop(j)
    j=j+1
print(x)
j=1
while(j<len(x)):
    x.pop(j)
    j=j+1
print(x)
j=1
while(j<len(x)):
    x.pop(j)
    j=j+1
print(x)'''







'''l=[0,-3,5,-4,-2,3,1,0]
for i in range(len(l)):
    lef=[]
    right=[]
    for j in range(i+1,len(l)):
        right.append(l[j])
    for k in range(i-1,-1,-1):
        lef.append(l[k])
    if len(lef) or len(right)==0:
        lef.append(0)
        right.append(0)
    #print(lef,right)
    if sum(lef)==sum(right):
        print(i)
'''

l="123..123"
s=l.split(".")
print(len(min(s)))





















