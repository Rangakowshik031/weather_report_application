'''f=open("s2.txt","wb")
f.write(b"machine learning")
f.close()'''

f=open("s2.txt","rb")
f1=open("s3.txt","wb")
p=f.read(10)
f1.write(p)
f.close()
f1.close()
