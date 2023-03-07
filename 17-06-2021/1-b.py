class Person:
    def m1(self,name):
        self.name=name
        return

class publications:
    def m2(self,b):
        self.b=b
        return

class Faculty(Person,publications):
    def m3(self):
        print("CSE FACULTY")
        print("NAME:",self.name)
        print("PUBICATIONS:",self.b)

a=Faculty()
a.m1("swamy das")
a.m2("DBMS")
a.m3()
