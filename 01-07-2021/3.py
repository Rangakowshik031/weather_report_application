f=open("s4.txt","w")
f.write("GSTgoodsandservicetax")
f.close()

f=open("s4.txt","r")
l=f.read()
print(l)
vowels=0
consonants=0
t=len(l)
for i in l:
    if (i=='a' or i=='e' or i== 'i'  or i== 'o' or i== 'u' or i== 'A' or i== 'E' or i=='I' or i=='O' or i=='U'):
        vowels+=1
    elif(i>='a' and i<='z') or (i>='A' and i<='Z'):
        consonants+=1
print("number of vowels in the file=",vowels)
print("number of consonants in the file=",consonants)
print("total number of characters in the file=",t)
v=(vowels/t)*100
c=(consonants/t)*100
print("Percentage of vowels:",int(v))
print("Percentage of consonants:",int(c))
#print(vowels,consonants)
        
