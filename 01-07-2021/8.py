f1=open("questions.txt","w")
f1.write("FULL OF API \n1.APPLICATION PROGRAM INTERFACE \t 2.ANDROID PROGRAM INTERFACE \nMETHOD OVERLOADING IS SUPPORTED IN PYTHON\n1.True \t 2.False")
f1.close()

f1=open("answers.txt","w")
f1.write(" (1) APPLICATION PROGRAM INTERFACE \n (2) False")
f1.close()


f2=open("questions.txt","r")
f3=open("answers.txt","r")
p=f2.read()
q=f3.read()
#print(p)
print("-------------------------")
print("Questions")
print(p)
print("-------------------------")
print("ANSWERS")
print(q)
print("-------------------------")

