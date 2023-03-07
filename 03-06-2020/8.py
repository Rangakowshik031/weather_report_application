class student:
    "taking dummy"
    name=""
    rollno=000
    marks=[]
    def input(self):
        self.name=input("enter student name:")
        self.rollno=int(input("enter student roll number:"))
        self.marks=[]
        for i in range(3):
            self.mark=int(input("enter student marks:"))
            self.marks.append(self.mark)
    def disp(self):
        print("student name:",self.name,"Roll no:",self.rollno,"Marks:",self.marks)
    def total(self):
        total=0
        for i in range(3):
            total=total+self.marks[i]
        return total
    
p=student()
p.input()
p.disp()
print(p.total())
q=student()
q.input()
q.disp()
print(q.total())

