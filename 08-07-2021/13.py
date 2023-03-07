file=open("s1.txt","w")
file.write("9908517699 160120748031 kowshikranga@gmail.com")
file.close()


import re
pat="[7-9]{1}[0-9]{9}"
file=open("s1.txt","r")
s=file.read()
l1=re.findall(pat,s)
print("mobile number:",l1)

pat1="160120748[0-9]{3}"
l2=re.findall(pat1,s)
print("Roll number:",l2)

pat2=r"[a-z]+[\.]+[\w]{2,3}"
l3=re.findall(pat2,s)
print("host part",l3)

l=[]
l.append(l1[0])
l.append(l2[0])
l.append(l3[0])
print(l)


file1=open("s2.txt","w")
for i in l:
    file1.write(i)
file.close()
file1.close()
