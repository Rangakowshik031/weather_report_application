a=987 #global
b=535
def sample():
    c=9822  #local
    print(locals())
print(globals())
sample()
#print(dir())
import builtins
print(dir())
l=[1,2,3,4,5]
print(sum(l)) #built in namespace
print(len(l)) #built in namespace
