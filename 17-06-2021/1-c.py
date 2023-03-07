class department:
    def m1(self,dept):
        self.dept=dept
        return

class course(department):
    def m2(self,b):
        self.b=b
        return
    def disp1(self):
        print("DEPARTMENT:",self.dept)
        return

class student(course):
    def m3(self,name):
        self.name=name
        return
    def disp2(self):
        print("COURSE:",self.b)
        print("STUDENT NAME:",self.name)
        return

c=student()
c.m1("CSE")
c.m2("AI AND ML")
c.m3("kowshik")
c.disp1()
c.disp2()

        
