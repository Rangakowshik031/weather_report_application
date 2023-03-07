rows=int(input("enter number of rows:"))
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
    #print(i,end=" ")
    print()
    i=i+1
