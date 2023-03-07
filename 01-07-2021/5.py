f1=open("s6.txt","w")
f1.write("regular\t expressions is\t very important\n concept in \n oop")
f1.close()

f1=open("s6.txt","r")
p=f1.read()
print(p)
tab=0
space=0
new_line=0
for i in p:
    if i=='\t':
        tab+=1
    elif i==' ':
        space=space+1
    elif i=='\n':
        new_line+=1
print("TABS:",tab)
print("SPACES:",space)
print("NEW LINES:",new_line)
        
