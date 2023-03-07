class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.breadth+self.length)
    def area(self):
        return self.breadth*self.length



r=rectangle(10,20)
print("perimeter of the rectangle =",r.perimeter())
print("area of the rectangle =",r.area())
    
