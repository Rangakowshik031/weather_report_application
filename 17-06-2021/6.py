class distance:
    def kms(self,school,office):
        self.school=school
        self.office=office
    def meters(self):
        self.school_1=self.school*1000
        self.office_1=self.office*1000
class school(distance):
    def A(self):
        print("distance from home to school in kms:",self.school)
        print("distance from home to school in meters:",self.school_1)
class office(school):
    def B(self):
        print("distance from home to office in kms:",self.office)
        print("distance from home to office in meters:",self.office_1)
o=office()
o.kms(4,10)
o.meters()
o.A()
o.B()

'''class a:
    def func(self,a):
        self.b=10
        self.a=a
        return
class b(a):
    def func1(self):
        print(self.a)

x=b()
x.func(100)
x.func1()'''
