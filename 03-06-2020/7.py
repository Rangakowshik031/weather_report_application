class employee:
    name="abcd"
    designation="abcd"
    salaray=1582000
    cout=0
    def func(self):
        self.name=input("enter employee name:")
        self.designation=input("enter designation:")
        self.salary=int(input("enter salary:"))
    def disp(self):
        print("employee name:",self.name,"designation:",self.designation,"salary:",self.salary)
        employee.cout+=1
    def coutb(self):
        print("number of employees=",employee.cout)
        
        
p=employee()
p.func()
p.disp()
q=employee()
q.func()
q.disp()
r=employee()
r.coutb()
