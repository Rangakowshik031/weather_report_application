class Car:
    def __init__(self,n,m):
        self.name=n #instance variable
        self.mil=m #instance variable
        print(" Locals ",locals())
    wheels=4 #class variable

c1=Car("BMW",10)#constructor
c2=Car("Audi",10)#constructor
c2.mil=8
print(c1.name,c1.mil,c1.wheels)
c2.wheels=5
print(c2.name,c2.mil,c2.wheels)
print(c1.name,c1.mil,c1.wheels)
Car.wheels=6
#after changing class variable
print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)
print(" Glabal Variables",globals())



#Class variables : Inside a class and out side all method with in calss
# wheels



#instance variables :
# c1--> name and mil
# c2--> name,mil and wheels




#Local Variables :
# -->init --> n,m,self
# -->




#GlobalVaribles :
# c1,c2,Car









'''import sys
class Test:
    pass
print(sys.getrefcount(Test())) #object 1 --> dontot have any odentifier
print(sys.getrefcount(Test())) #object 2 -->
t1=Test() # object 3
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))
print("Globals ", globals())'''





















