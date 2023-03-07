class distance:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        return
    def cal(self):
        self.x=((self.a-self.c)**2 + (self.b-self.d)**2)**0.5
        return self.x
    def __isub__(self,other):
        self.x-=other.x
        return self.x

z=distance(1,0,4,4) #5
z.cal()
y=distance(0,1,0,2) #1
y.cal()
z-=y
print(z)
        
