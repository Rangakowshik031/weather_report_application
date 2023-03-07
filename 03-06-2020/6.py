import datetime
class citizen:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def verify(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today < datetime.date(today.year,self.dob.month,self.dob.day):
            age-=1
        if age>=18:
            print("you are eligible to vote : ",self.name)
        else:
            print("soory you are not eligible to vote ")


r=citizen("kowshik",datetime.date(2002,12,9))
r.verify()
