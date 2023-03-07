s=input("enter file name:")
file=open(s,"w")
file.write("internet of things")
file.close()

file=open(s,"r")
p=file.read()
#print(p)
q=input("enter any character:")
cout=0
for i in p:
    if i==q:
        cout=cout+1
print("Number of times ",q,"is repeated is:",cout)
file.close()

