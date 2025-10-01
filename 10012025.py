#list and dictionaries last class, hopefully get sign up for mid term out today.

Dictionary does not matter what order you have the items in, can look up a bunch of pairs of things
Immediate results from a Dictionary
Dictionary v list, depends on problem, but if Dict can solve your problem, go with it

[] for list
{ around key values for dictionary}

Tuples
t = ('a', 'b', 'c')
Lists that cant change after it is made

if you want one item:
single = (42, )
print(single) # result is 42, 
print(single*5) #result is printing 5 times

word="racecar" #string of characters
print(word[0])  # result is "r"
print(word[:4]) #slice the result (?)everything before(?)
print(word[4:]) #slice the result (?) everything after (?) these may be switched
print(word[::2]) #everything backwards or was it print(word[::-1])

print( tuple(word) )  #turns word into a tuple
print( list(word) )  #turns word into a list

nums=(1,2,3,4)

nums=list(nums)

nums[1]=99 #replacing values in a tuple
print(nums) #result is printing list/tuple with 1 being replaced by 99

#mapping
buildings={} #empty dictionary
buildings[(0,0)] = "city hall"
buildings[(1,0)] = "police station"
buildings[(0,1)] = "pizza place"
print( (0,0) in buildings)
print (buildings[(0,0)])

point=1, 5
print(point) #this is a tuple, understood parenthesis, use square bracks for list

x=point[0]
y=point[1]

but python has a better way 

point=[1, 5]
print(point)
x,y=point
print(x)
print(y)

#swapping values from one variable to another

x,y=y,x # python method


#other languages
temp=x
x=y=temp

def distance_from_origin(x,y):
    return (x*x+y*y)**.5  #**.5 to the half power same thing as square root
point = [3,4]
print(point)
x,y=point
print( distance_from_origin)

#or you can

print( distance_from_origin(*point) ) #not suggessted, previous version super clean

a={1,2,3]
b=a #we dont get more memory...bpoints at what a points at - why? list could be big
b[1]=99
print(b) # not blow anyone mind
print(a) #same result, int float bool with an "=" sign...

x=5
y=x #get another slot in memory, value is copied
y=99
print(y) #result 99
print(x) #result 5

