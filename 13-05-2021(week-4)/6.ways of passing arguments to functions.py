#required aruguments
def func():
    print("cse")

func()

#keyword aruguments
def func_1(a,b):
    print(a)
    print(b)

c=9
d="helo"
func_1(b=d,a=c)

#default arguments
def func_2(a,b=6.5):
    print(a)
    print(b)

func_2(2)
func_2(2,3.7)


#variable length arguments
def func_3(*a):
    for i in a:
        print(i)

func_3(4,5,'cse',2.574)
