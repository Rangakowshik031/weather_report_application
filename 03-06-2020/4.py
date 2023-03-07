class funct:
    def __init__(self):
        print("welcome")
    def func(self):
        print("hi")
    def __del__(self):
        pass
c1 = funct()
c1.func()
del c1
#c1.func()  c1 is not identified
