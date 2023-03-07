from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def company(self):
        pass
    @abstractmethod
    def model(self):
        pass

class car(vehicle):
    def company(self):
        print("--car--")
        print("TOYOTA")
        return
    def model(self):
        print("innovva crysta")
        return

class truck(vehicle):
    def company(self):
        print("--truck--")
        print("MAHINDRA COMPANY")
        return
    def model(self):
        print("E alfa mini")
        return

class motorcycle(vehicle):
    def company(self):
        print("--motorcycle--")
        print("BMW")
        return
    def model(self):
        print("G 310 R")
        return
a=car()
a.company()
a.model()
b=truck()
b.company()
b.model()
c=motorcycle()
c.company()
c.model()
