class sample:
    a=10 #public member
    __b=20 #private member
    def func(self): #public method
        print("hello")
    def __func1(self): #private method
        print("cbit")



p=sample()
print(p.a)
#print(p.b)
#print(p.__b)
print(p._sample__b)
p.func()
#print(p.func1())
#print(p.__func1())
p._sample__func1()
