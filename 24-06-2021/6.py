import datetime
class a:
    def __init__(self,a):
        self.date=a
    def __gt__(self,other):
        return(self.date > other.date)

x=a(datetime.date(2020,12,7))
y=a(datetime.date(2020,12,19))
print("comparing two dates with '>': ",x>y)
        
        
            
