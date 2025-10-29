# Working Local tab in Blackboard now, shows you different IDEs.

import turtle

turtle.forward(100)
turtle.mainloop()

#This cannot be done in codespace, so we need to set up alternate IDEs as seen in working locally

# install VS code
# Install git
# install python
# add one extension (python) to VS code
# Clone repository for the first time
# Create python environment - kind of project specific. Doesnt really need to happen


1) Attributes/data/instance variable: what makes a point different from another point
    minimum amount of info needed to know a point? X and y
2) Constructor:  Fills in the attributees
3)Methods and functions: Modify the attributes or read the attributes.


class Point:
    def__init__(self,x,y)
        self.x=X
        self.y=y


p=Point(3,4)
print(p.x) # prints 3

#NEXT
import math

class Point:
    def__init__(self,x,y)
        self.x=X
        self.y=y

    def move(self,dx,dy)
        self.x+=dx
        self.y+=dy

    def distance_to_origin(self):
        return math.hypot(self.x,self.y)

    def __str__(self):
        return "I am a point" # or return F"Point(x={self.x}, y={self.y})

p=Point(3,4)

p.move(2,-1) #x = 2 y = -1

print(p.x)
print(p.y)
print(p.distance_to_origin() )
print( str(p) ) # or just print(p), or print(f"point1 info:(p))

#Encapsulation
#invariants .... should always be true

import math

class Point:
    def__init__(self,x,y)
        self.x=X
        self.y=y
        self.dist_org=math.hypot(self.x,self.y) # If someone changed X, everything would break

    def set_x(self, new_x):
        self.x=new_x

    def move(self,dx,dy)
        self.x+=dx
        self.y+=dy
        self.dist_org=math.hypot(self.x,self.y) # Also, this takes hours to compute, called cacheing

    def distance_to_origin(self):
        return math.hypot(self.x,self.y)

    def __str__(self):
        return "I am a point" 

p=Point(3,4)
p.move(2,-1) 

print(p.x)
print(p.y)
print(p.distance_to_origin() )
print( str(p) ) 