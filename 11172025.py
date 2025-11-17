3 modules, 11, 12, and 13 remain, plus a final project, object oriented recipe book
final - 100 pts for attesting that we do course eval, then some options for the coding portion.  
There will be an inperson final as well

import randon

n=100
nums=[i in range(n)]
random.shuffle(nums)

print(nums)

for i in range(len(nums)-1):
    if nums[i] > nums [i+1]
        temp = nums[i] #start to flip
        nums[i]=nums[i+1]
        nums[i+1]=temp # finish the flip

        #cleeaner way to flip in python
        nums[i],nums[i+1] =nums[i+1],nums[i]