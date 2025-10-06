#sample midterms on blackboard

#ask user if they want to run program again below

total=0

while true:
    num=float(input("num (negative number to stop): "))
    if num<0:
        break
    total+=num
    count+=1
if count==0:
    print("no numbers were entered")
else:
print(f"total={total} average={total/count}")

# to put it in a loop

def doAverage():
    total=0

while true:
    num=float(input("num (negative number to stop): "))
    if num<0:
        break
    total+=num
    count+=1
if count==0:
    print("no numbers were entered")
else:
print(f"total={total} average={total/count}")

while True:
    doAverage()
    prompt=input("Do you want to run this again? (y/n)? ")
    if prompt!="y":    #doesnt equal
        break

#still dont have two helper functions

def doesnt_want_to_continue():
    prompt=input("Do you want to run this again? (y/n)? ")
    return prompt=="y"

def doAverage():    #need snake case
       total=0

while true:
    num=float(input("num (negative number to stop): "))
    if num<0:
        break
    total+=num
    count+=1
if count==0:
    print("no numbers were entered")
else:
print(f"total={total} average={total/count}")

while True:
    doAverage()
        if not doesnt_want_to_continue():
        break

# Moving on to actual class

#Sting is something in quotes, single quotes or double quotes
print("abc"=='abc')
s="asdf"
print(len(s))
print(type(s))

#all the same things you do with lists you can do with strings

print("abc"=='abc')
s="squirrel"
print(len(s))
print(type(s))
print(s[0]) #result is s
print(s[-1]) #result is l

# uppercase and lowercase are not interwoven

word = banana
upp_word = word.upper()
lower_word = word.lower_wordtitle_word = word.title
print(upper_world)
print(lower_word)
print(title_word)
