
def existe1(nums, target):
    return existe(0,nums,target)

def existe(start,nums,target):
    if target==0:
        return True # T(n) = c1 = 3
    else: 
        if start<len(nums):
            si= existe(start+1,nums,target-nums[start])
            no= existe(start+1,nums,target)
            si_no=si or no
            return bool(si_no)
        
            # T(n) = c2 + T( n - 1 ) + T( n - 1 ) , donde c2 = 9

            # T(n) = c2 (2^n - 1) + c1 2^(n-1) 
"Test"
print(existe1([2,4,8],9)) 
