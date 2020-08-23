
def existe1(nums, target):
    return existe(0,nums,target)

def existe(start,nums,target):
    if target==0:
        return True # T(n) = c1 = 6
    else: 
        if start<len(nums):
            if nums[start]%5==0:
                if nums[start+1]==1:
                    si= existe(start+2,nums,target-nums[start])
                    no=False
                else:
                    si= existe(start+1,nums,target-nums[start])
                    no=False
                # T(n) = c2 + T( n - 1 ) , donde c2 = 9
            else:
                si= existe(start+1,nums,target-nums[start])
                no= existe(start+1,nums,target)
                # T(n) = c3 + T( n - 1 ) + T( n - 1 ) , donde c3 = 4
            si_no=si or no
            return bool(si_no)
            # T(n) = c4 + T( n - 1 ) + T( n - 1 ) , donde c4 = c3+6=10
            # T(n) = c4 (2^n - 1) + c1 2^(n-1)
            
"Test"
print(existe1([3,5,10,1],16)) 
