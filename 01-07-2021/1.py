'''f=open("s1.txt","w")
f.write("artificial intelligence")
f.close()'''


f=open("s1.txt","w")
print("NAME OF THE FILE:",f.name)
print("MODE IN WHICH THE FILE IS OPENED:",f.mode)
print("FILE IS CLOSED OR NOT:",f.closed)
f.close()
print("FILE IS CLOSED OR NOT:",f.closed)
