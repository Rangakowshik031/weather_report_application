for i in range(1,5):
    for j in range(5,i):
        print(" ",end="")
    for k in range(1,i):
        print("* ",end="")
    print("\n")
number_list = []
n = int(input("Enter the list size "))
print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)


for i in range(10,0):
    print(i)


    

