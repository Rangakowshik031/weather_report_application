l=[100,98,95,94,90,99]
total=0
for i in l:
    total = total + i
    average= total/6
print(total)
print(average)
if average>75:
    print('distinction')
elif average<75 and average>60:
    print('first division')
elif average<60 and average>50:
    print('second division')
else:
    print("fail")
