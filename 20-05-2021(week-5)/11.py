n=int(input("enter the number of rows :"))
count=0
for i in range (n):
      print()
      for j in range ((n-1)-i):
            print(end="  ")
      for k in range ((2*i)+1):
            if(k<=i):
                  print(k+1,end=" ")
            else:
                  count+=1
                  k=i+1-count
                  print(k,end=" ")
      count=0
