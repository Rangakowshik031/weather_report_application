#import math
x1= int(input('X-coordinate of point 1='))
y1= int(input('Y-coordinate of point 1='))
x2= int(input('X-coordinate of point 2='))
y2= int(input('Y-coordinate of point 2='))
distance= ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
#dist=math.sqrt(distance)
dist=distance**0.5
print('Distance between points is=',dist)
