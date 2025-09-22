def f(n): #parameters - how many times you say hello
    print:("hello"*n)

f(4) #prints hello 4 times.


def f(n): 
    print:("hello"*n)

def find_root(a,b,c):
    return (-b+-(b*2-4*a*c)**.5/2*a) #quadratic equation - i think)

f(4) 
root1 = find_root(1,4,4)
print:(root1):

def f(n): 
    print("hello"*n)

def find_root(a,b,c):
    inside = (b*2-4*a*c) #isnide function definition, should not print inside further below
    return (-b+-(inside)**.5/2*a) 

f(4) 
root1 = find_root(1,4,4)
print(root1):
print(inside): #this should not work because inside is outside....???

#to change a bolean, you have to use the word "not", but in math "!=" also means not

def printn(s,n):
    if n<=0:
        return #youre out of function now, dont have to specify anything
    print(s) #nibble
    print(s,n-1) #callback

#intuitive looping

for letter in "squirrel": #other langs call this for/each loop
    print(letter) #prints letters one by one vertially


def check_for_letter(word,letter):
    for letter2 in word:   #have to name this "letter" diff than parameter
        if target_letter==letter:
            return True
        return False

print(check_for_letter("Squirrel","q")) #output true
print(check_for_letter("Squirrel","x")) #output false

#loop standard 5 times

for i in range (5): #number of times you want a loop
    print("squirrel")

print( range(8) ) # tells you it is a range object
print( list(range(8)) ) #prints list

#numbered list loop i think
for i in range (5): 
    print(f"{i} squirrel")


#two places on the list
for i in range (10,21): 
    print(f"{i} squirrel")


#skip by two
for i in range (10,21,2): 
    print(f"{i} squirrel")

#count to 10
for i in range(1,11):
    print(i)

#or count to ten

for i in range(10):  #this may be incorrect
    print(i+1)

#can count backwards
for i in range(10,0,-1)
    print(i)

#or
for i in range(10):  
    print(10-i)

#when to use for loops and when to use why loops
#for loops - know how many times
#why loop is when you dont know.

prompt = input("do you want to run the prog?")

while prompt =="yes":
    print("calculating")
    prompt = input("do you want to run the prog again: ?")  #i missed some of this, hope this is correct

for i in range(100): #not clean
    print(i)
    if i>40:
        break

for i in range(41):  #clean
    print(i)

#break is a tool, use it as needed to get out of a loop, there is some philosophy that never use it

word = "programming"
for char in word:
    if char not in "aeiou": #if not vowel
        continue #skip to next character
    print(char, end="")
print()

#this is a way to draft a function and not get an error
def func():
    pass

func()


#again

if x>0:
    asdf
else:
    pass


#a cooler way

def func():
    ...

func()

#initialize counter
word = "programming"
vowel_count = 0 #right here, called a accumulator, collector, or counter
for letter in word:
    if letter in "aeiou"
        vowel_count += 1 #increment counter
print(f"found {vowel_count} vowels")


num=1234
total=0
while num:
    digit=num%10
    total=total+digit
    num=num//10
print(f"the sum of digits is {total}!")


#algoritms
#print list of nums
nums=[78,34,89,54,32]
for num in nums
 print(nums)
    
#find biggest
nums=[78,34,89,54,32]
biggest=nums[0] #gives first value
for num in nums
    if num>biggest:
        biggest=num
print(biggest)

#or
print(max(nums))

#not sure what this does, need to try it out
word = "programming"
no_vowel_word=""
for char in word:
    if char not in "aeiou"
        no_vowel_word += char
print(no_vowel_word)

def has_a(word):
    for letter in word:
        if letter=="a":
            return True
        return False
word="dog" #should be false
print (has_a(word) )
print( "a" in word) # same thing as line above

for row in range(5):
    for col in range(6)
        print(row*col, end="")
    print()