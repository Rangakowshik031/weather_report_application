class Person:
    def m1(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        return
class Employee(Person):
    def disp(self):
        print("employee name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)
        return

a=Employee()
a.m1("ravi",25,100000)
a.disp()
        
