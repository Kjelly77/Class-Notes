Sets 2/5
counter 1/5
defaultdict 1/5
comprehnsions* 5/5
conditional stm* 2/5
iter 1/5
generations 2/5
lambda 4/5
sort uses lambda
zip 4/5
map 2/5


nums=[1,2,3,4,54,34,1,1,1,]
nums=set(nums) #de duplicate
print(nums) # only get uniques but lose your order
can also turn into a list nums=list(set(nums)) and sort iter

##comprehension
[100,99,98,...,1]

nums=[i for i in range(100,0,-1)] can count from 100 down to 1

nums[start:stop:step]

mydict={i:0 for i in range(10)}
print(mydict)

#lambda
function that doesnt have a name
lambda x: x*x  #valid ffunction, didnt give it a name, dont have a way to call it

f=lambda x: x*x

print( f(5) )

should be used with map,filter,sort functions, feed lambda into them and have them do work

nums=[1,2,3,4]
print( map(f,nums) )

#zip - two different lists you can go through at the same time
for i in range(len(names)):
    name=names[i]
python gives us zip, cleaner

zip(names,ages)
print( zip(names,ages) )

# you could
print( list( zip(names,ages) ) )

x,y=[3,4] # zip auto unpacks, 3 in x, 4 in y

for name,age in zip(names,ages):
    print(name,age)