#recursion question on practice_04
def multiply(a,b):
    return (a*b)
print( Multiply(3,4) )
#Should print "12"

3*4=3+3+3+3=4+4+4

#3 parts of recursion
#nibble
#call back
#terminating condition

3*4=3+3*3
3*b=3+3*(b-1)
a*b=a+a*(b-1)

def multiply(a,b):
    if a==0 or b==0:    #code golfing - a*b==0
        return 0
    return a+multiply(a,b-1)

print( multiply(3,4) )

#There is still a problem with neg numbers.

def multiply(a,b):
    if a==0 or b==0:   
        return 0
        if b<0:
            return multiply(-a,-b) #works now with neg numbers
    return a+multiply(a,b-1)

print( multiply(3,4) )

#function overloading

def (f):
    return 3

def f(x):
    return 3*x

def f(x,y):
    return 3*x*y

print( f(2) )
#output is -12, but f is missing one required positional argument. 
#It ran each function, but overwrote it when it moved to the next function

g = f
print( g(4,5))
#We will come back to this in the future. 

def f(x=1,y=1):
    return 3*x*y

print( f() )
print( f(4) )
print( f(4,5) )
#output is 3, 12, and 60

import turtle  #this actually does not work in codespace
# size, x,y location, rotation, is_outlined, color, outline_color, line_thickness, a million parameters
#size, x,y , thickness, color
def draw_square(size=10,x=0,y=0,thickness=4,color=(0,0,0)):
    turtle.up()
    turtle.goto(x,y)
    turtle.width(thickness)
    turtle.down
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)     #4 times

draw_square(100,10,10,7,(1.0,0,0))  #last 3 need to be float, RBG (100% red here)
turtle.mainloop()   # keeps program from going away

print( dir(turtle) ) # prints all the avaialble widgets of turtle. 
draw_square(x=200,y=200) #overwrite default values
draw_square(80,-20,-20,3,(0.0,0.0,1.0)) #positional arguments
draw_square(300,-150,-150, color=(1,0,1))  #purple, positional arguments up until color
#all arguments would have to be key worded after that

draw_square2()   # another function

def draw_square(size: int=10,x: int=0,y: int=0,thickness: int=4,color=(float,float,float)):
#This specifies what type 

"""Triple Quotes tells you what is happening, can specify what size of square 
is, maybe it is in pixels?"""

#can run tools that turn triple quotes in to html, pdf, or whatever

import.turtle

turtle.forward(100) # run and make sure it works
turtle.mainloop() #first problem identified

#so

#makes a square 
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)


turtle.mainloop()

#instead of comment at header

def draw_square(size):
turtle.forward(size) 
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)



draw_square()
draw_square() #drawing two squares


turtle.mainloop()

#now we want to control size

def draw_square(size):
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)

size1=float(input("sqaure 1 size: "))
size2=float(input("sqaure 2 size: "))

draw_square(size1)
draw_square(size2) 


turtle.mainloop()

#make small changes, test often