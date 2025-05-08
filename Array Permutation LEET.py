nums=[0,2,1,5,3,4]
#Output: [0,1,2,4,5,3]
number=[]
for i in range(len(nums)):
    number.append(nums[nums[i]])
print(number)