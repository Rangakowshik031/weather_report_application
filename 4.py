import datetime
class citizen:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def verify(self):
        today=datetime.date.today()
        #print(today)
        age=today.year-self.dob.year
        #print(datetime.date(today.year,self.dob.month,self.dob.day))
        if today < datetime.date(today.year,self.dob.month,self.dob.day):
            age-=1
        print(age)


r=citizen("kowshik",datetime.date(2002,12,9))
r.verify()
