# File I/O
# 10% quiz, 10% Tutorial 10% Practice, 5% Participation, 35% Project, 10% Midterm, 20% final

# First project starting wednesday 10/22

my_list=[23,56,5423]
my_list.appemd(23)

my_tuple=(56,789,43)
print(my_tuple[1])

my_dict={"alice":342553454,"bob":[23,45,65]}

def f(x):
    y=4
    x+=y
    return x

f(8) #stores 12
print(f(8)) # prints 12

# if try to print(y) it will throw an error, y only exists in that function
# y exists only at that tab level

x=10
print(f(x))
print(x) # this prints 14, then 10

#this tab level is global, global x in above
    #this tab level is function level, function level x in above

#SCOPE is tab level existence.

s="      squirrel    "

print(s.strip()) # removes unneccessary spaces
l.strip # strips only the left side
r.strip # strips only the right side

print(s.replace("    ", "*"))  # Replaces spaces with stars, case sensitive when replacing
# words with other words
print(s.replace("Squirrel", "Marmot") # s = lower case squirrel, no replace

#Opening a file

See related worksheet.
