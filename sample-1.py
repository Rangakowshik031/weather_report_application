rows=6
for row in range(1, rows+1):
    print("\n")
    for i in range(1,rows-row+1):
        print(end=" ")
    for j in range(1,row+1):
        print("* ",end=" ")

print("\n")

rows=6
i=0
while(i<=rows):
    c=1
    while(c<=rows-i):
        print(" ",end=" ")
        c=c+1
    e=1
    while(e<=i):
        print(e,end=" ")
        e=e+1
    print()
    i=i+1

