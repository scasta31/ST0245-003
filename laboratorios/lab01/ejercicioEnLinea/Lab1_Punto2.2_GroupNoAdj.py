
def existe1(nums, target):
    return existe(0,nums,target,target)

def existe(start,nums,target,targetAnterior):
    if target==0:
        return True # T(n) = c1 = 6
    else: 
        if start+1<len(nums):
            if target==targetAnterior:
                si= existe(start+2,nums,target-nums[start],target)
                no= False
            else:
                si= existe(start+1,nums,target-nums[start],target)
                no= existe(start+1,nums,target,target)                
                # T(n) = c2 + T( n - 1 ) + T( n - 1 ) , donde c2 = 8
            si_no=si or no
            return bool(si_no)
            # T(n) = c3 + T( n - 1 ) + T( n - 1 ) , donde c3 = c2 + 7= 15
            # T(n) = c3 (2^n - 1) + c1 2^(n - 1) 
"Test"
print(existe1([2,5,10,4],7)) 