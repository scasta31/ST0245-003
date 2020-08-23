def splitarray(nums):
    return splitarray1(nums,0,0,0)

def splitarray1(nums,index,sum1,sum2):
    if index>=len(nums):
        return sum1 == sum2
    else:
        return (splitarray1(nums,index+1,sum1+nums[index],sum2) 
                or splitarray1(nums,index+1,sum1,sum2+nums[index]))

"Test"
print(splitarray([2,2]))      
print(splitarray([2,3])) 
print(splitarray([5,2,3]))                