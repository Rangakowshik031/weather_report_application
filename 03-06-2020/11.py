class book():
    def __init__(self):
        self.name=""
        self.author=""
        self.price=0
    def new(self):
        self.name=input("enter the name of the book:")
        self.author=input("enter the name of the author:")
        self.price=int(input("enter the price:"))
    def display(self):
        print("------------------------------")
        print("NAME: ",self.name)
        print("AUTHOR: ",self.author)
        print("PRICE: ", self.price)
        print("------------------------------")
l=[]
a=1
while(a):
    x=int(input("enter 1 for adding new book\n 2 for display:"))
    if(x!=1 and x!=2):
        break
    elif(x==1):
        b=book()
        b.new()
        l.append(b)
    elif(x==2):
        for i in l:
            i.display()
