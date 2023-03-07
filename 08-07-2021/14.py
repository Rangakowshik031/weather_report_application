f=open("r1.txt","w")
f.write("1601-20-748-031  1601-20-748-028  1601-20-748-035")
f.close()


import re
file=open("r1.txt","r")
file1=open("r2.txt","w")
pat="-"
s=file.read()
sub=""
i=re.sub(pat,sub,s)
print(i)



file1.write(i)

file.close()
file1.close()
