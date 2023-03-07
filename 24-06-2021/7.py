f=open("f1.txt","w")
f.write("CSE 4 CBIT AI AND ML ")
f.close()

f=open("f1.txt","a")
f.write("GANDIPET")
f.close()

f=open("f1.txt","r")
print(f.read())
f.close()
