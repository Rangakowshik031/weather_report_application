f1=open("s2.txt","r")
print(f1.read())
f1.close()

f1=open("s2.txt","r+")
print(f1.read())
f1.close()

f1=open("s2.txt","rb")
print(f1.read())
f1.close()

f1=open("s2.txt","rb+")
print(f1.read())
f1.close()


f1=open("s7.txt","w")
f1.write("hello")
f1.close()

f1=open("s7.txt","w+")
f1.write("hi")
f1.close()

f1=open("s7.txt","wb")
f1.write(b"CSE -4")
f1.close()

f1=open("s7.txt","wb+")
f1.write(b"CSE -4")
f1.close()

f1=open("s7.txt","a")
f1.write("CSE -4")
f1.close()

f1=open("s7.txt","a+")
f1.write("CSE -4")
f1.close()

f1=open("s7.txt","ab")
f1.write(b"CSE -4")
f1.close()

f1=open("s7.txt","ab+")
f1.write(b"CSE -4")
f1.close()



