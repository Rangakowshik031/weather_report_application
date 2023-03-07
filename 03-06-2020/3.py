class circle():
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius*self.radius



r=circle(10)
print("perimeter of the circle =",r.circumference())
print("area of the circle=",r.area())
