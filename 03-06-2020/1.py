class Student:
    roll_no=9999
    name=''
    def get_details(self):
        self.roll_no=int(input("enter student roll number="))
        self.name=input("enter student name=")
    def set_details(self):
        print("Roll Number:",self.roll_no,"Student name:",self.name)

p=Student()
p.get_details()
p.set_details()
q=Student()
q.get_details()
q.set_details()      

class Book:
    author=" "
    publisher=''
    def get_details(self):
        self.book=input("enter book name=")
        self.author=input("enter author name=")
        self.publisher=input("enter publisher=")
    def set_details(self):
        print("Book name:",self.book,"Author:",self.author,"Publisher:",self.publisher)


a=Book()
a.get_details()
a.set_details()
b=Book()
b.get_details()
b.set_details()
