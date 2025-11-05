#class
#Make a class, list all of its attributes

#Java went wild

#Try to limit yourself to 1 level of inheritence, make a base class and go from there

class Rectangle:
    def __init__(self,w,h):
        self._w=w
        self._h=h #underscore shows that someone doesnt need to mess with your internals
    def area(self):
        return self._w*self._h

r=Rectngle(4,6)
print(r.area())

#feed into, store it, recall it
#perfect for recipes

class Ingredient:
    def __init___(self,quant,unit,name)

#making square do what rectangle does

class Rectangle:
    def __init__(self,w,h):
        self._w=w
        self._h=h 
    def area(self):
        return self._w*self._h

class Square(Rectangle):
    pass

r=Rectngle(4,6)
s=Square(5,5)
print(r.area())
print(s.area())

#OR

class Rectangle:
    def __init__(self,w,h):
        self._w=w
        self._h=h 
    def area(self):
        return self._w*self._h

class Square(Rectangle):
    def __init__(self,length,):
        super().__init__(self,length,length)
        #or self._w=length, self._h=length

r=Rectngle(4,6)
s=Square(5)
print(r.area())
print(s.area())

#another example

class Fraction:
    def __init__(self,n,d):
        self._n=n
        self._d=d
        f=2
        while f<=d:
            while self.n%2f==0 and self.d%f==0:
                self.n//=f
                self.d//=f
            #keep going until you get to a value bigger than d
            f+=1

    def __add__(left,right) #or __add__(self,other)
        n1=left.n
        d1=left.d
        n2=right.n
        d2=right.d
        return Fraction(n1*d2+n2*d1,d1*d2)


    def __str__(self):
        return f"{self.n}/{self.d}"

a=Fraction(2,4)
print(a)

a+a

#deep copying

a=[1,2,3]
b=a

b[1]=99
print(b)

#but

a=[1,2,3]
b=a

b[1]=99
print(f"a={a}")
print(f"b={b}")
