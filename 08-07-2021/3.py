import random
s=random.randint(-100,100)
print(s)
class num(Exception):
    def __init__(self,a):
        self.a=a

try :
    if s<0:
        raise num(s)
except num:
    print("given number is below 0")
