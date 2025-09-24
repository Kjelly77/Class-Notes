for i in range(x):   #tattoo in notes, 

for i in range(6): #we know how many times we want to loop
    print("asdf") #will print this 6 times

#multiplication tables

* | 1 | 2 | 3
--+---+---+---
1 | 1 | 2 | 3
--+---+---+---
2 | 2 | 4 | 6


print("* |")
for i in range(1,4): #start at 1 and go short of 4
    print(f"{ i} |")
#in class example
print(" * |", end="")
for i in range(3):
    print(f"{ i+1} |", end="") # another option of the above
print() #gets you down to next line
print("---+"*4)
#2nd row - basically a copy and paste and edit the "*" to a "1"
print(" 1 |", end="")
for i in range(3):
    print(f"{ i+1} |", end="")
print() 
print("---+"*4)
#3rd row
print(" 2 |", end="")
for i in range(3):
    print(f"{ (i+1)*2} |", end="") #note change in this line
print() 
print("---+"*4)

#variable for more rows - he went fast, i think this is correct.
number_of_columns=6
print(" * |", end="")
for i in range(number_of_columns):
    print(f"{ i+1} |", end="") 
print() 
print("---+"*4)
#2nd row 
print(" 1 |", end="")
for i in range(number_of_columns):
    print(f"{ i+1} |", end="")
print() 
print("---+"*4(number_of_columns+1))
#3rd row
print(" 2 |", end="")
for i in range(number_of_columns):
    print(f"{ (i+1)*2} |", end="") 
print() 
print("---+"*4)

# we could make a function
def print_row(row)
    print()
    print("---+"*4(number_of_columns+1))

    #damn im missing this lecture

#what is a double for loop?

#5d - decimal number 5
#5b - binary number 5
#5f - floating point number 5

def has_vowel(word):
    for letter in word:
        if letter in "aeiou":
            return True
        else: #this line is incorrect
            return False #this line is incorrect
print( has_vowel("Squirrel") ) 

#try again
def has_vowel_fast(word):
    for letter in word:
        if letter in "aeiou":
            return True
    return False 
print( has_vowel_fast("Squirrel") ) 

#or

def has_vowel_slow(word):
    result=False
    for letter in word:
        if letter in "aeiou":
            return True
    return result
print( has_vowel_slow("Squirrel") ) 

#checking if n words each have vowels.....linear scaling
# if I double the number of words....time doubles

#quadratic scaling: double something....time quadruples - we are not here yet, this is a property of algorithms
#sometimes you want to switch from quadratic algorithm to linear algorithm

#bad loops
#debugging loops, lets get some loops wrong

count=0
num=234
while num>0:
    count += 1  # += is = count+1
    print(count)
#infinite loop is the result, will seem like it is paused there when you run program

#start putting debug prints in

count=0
num=234
print("loop started")
while num>0:
    count += 1  
    print(f"loop looped: count={count}")
    num=num//2
print("loop ended")
print(count)

for letter in "squirrel":
    if letter in "aeiou":
        vow_count+=1
print(vow_count)

# OBOB: off by one bug
# two ways to solve, think harder, or test code and adjust as needed

for i in range(10,0,-1): #start stop and step, start at 10, go to on1, go down by on1 every time
    print(i)


for i in range(10,0,-1): 
    print(f"T-{i} seconds until lift off")
print("BLASTOFF!!!")

#slower version
for i in range(10,0,-1): 
    print(f"T-{i} seconds until lift off")
    time.sleep(1)
print("BLASTOFF!!!")

