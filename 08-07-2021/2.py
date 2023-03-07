import random
i=-1
s=0
while i<1:
    s=s+1
    print(s)
    try:
        if s==20:
            raise(StopIteration)
    except StopIteration:
        print("program is terminated")
        break
