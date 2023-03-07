class sample:
    a=10
    __b="hello"
    def func(self):
        print("hello")
    def __func1(self):
        print("CSE")

class sample_1:
    print(sample.a)
    #print(sample.b)





obj=sample()
print(obj.a)
#print(obj.__b)
#print(obj.b)
obj.func()
a=obj._sample__func1()
#print(obj.func1())
