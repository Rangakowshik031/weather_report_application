class time_in_sec:
    def __init__(self,sec):
        self.sec=sec
        return
    def display(self):
        print("TIME IN SECONDS IS :{}".format(self.sec))
        return

class time_in_hr:
    def __init__(self,hr):
        self.hr=hr
        return
    def display(self):
        print("TIME IN HOURS IS :{}".format(self.hr))
        return

def hours(t):
    x = t.sec/60
    return x/60

def second(t):
    x=t.hr*60
    return x*60

t1=time_in_sec(36000)
t1.display()
print("TIME IN HOURS IS:",hours(t1))

t2=time_in_hr(5)
t2.display()
print("TIME IN SECONDS IS:",second(t2))
