#filter function
def func(n):
        c=2
        while c<n:
            if n%c==0:
                return 0
                break
            else:
                c=c+1
        if c>=n:
            return 1

s=[]
s=list(filter(func,range(2,10)))
print("fliter function=",s)






#map function
def func(n):
    return n*n
   
l=[1,2,3,4,5]
s=map(func,l)
print("map function=",list(s))





#reduce functions
import functools
def func(a,b):
    return a*b

l=[1,2,3,4,5]
s=functools.reduce(func,l)
print("reduce function=",s)
