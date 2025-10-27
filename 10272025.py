#project 1 due in two weeks, no practice08

#OOP: Object Oriented Programming
# Combination of data and behavior, in things called objects
# Chunks of code that can all be tested individually then stuck together like legos

Square: 
    data:
        side length
    behavior:
        area()
        perimeter()
        set_length(x)
        scale(f)

3 parts of an object
-instance variables, makes this object this Object
    example: length for square
-constructor, fill in values for all instance variables
-methods/functions, functions that can use the instance variables
    example: area, scale, anything that uses length (in this example)

#__init__ is used for object construction

class Square: #blueprint for an object
    def__init__(self,length): #dunder function, double underscore, init, double underscore, special functions that do special things
        self.length=length
        self.name="Asdf"
    def area(sel):
        return self.length**2 #or self.length*self.length


sq1=Square(6)
print(sq1)
area=sq1.area() #puts this in the self slot above
sq1.length=5 #now area should be 25
area=Square.area(sq1) # another option for the above
print(area)

