print("File operation")
try:
    f=open("f1.txt","r")
except FileNotFoundError:
    print("file is not found")
else:
    print("done")

import io
try:
    f1=open("f2.txt","r")
    f1.write("hello")
except io.UnsupportedOperation:
    print("This opearation cannot be performed")
else:
    print("done")

'''
import io
print(dir(io))
'''
    
