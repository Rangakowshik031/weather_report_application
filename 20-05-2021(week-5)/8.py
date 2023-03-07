global c
def func():
    p=1
    print(p)
    global c
    c=c+1
    print(c)


c=10
func()
print(c)
#print(p) gives error as it declared in function so it treated as local variable
