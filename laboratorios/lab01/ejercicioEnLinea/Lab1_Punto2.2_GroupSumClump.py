
def existe1(nums, target):
    return existe(0,nums,target)

def existe(start,nums,target):
    if target==0:
        return True # T(n) = c1 = 6
    else: 
        if start<len(nums)-1:           
            cont=0
            if nums[start+cont]==nums[start+1+cont]:
                while nums[start+cont]==nums[start+1+cont]:
                    cont=cont+1                   
                    if len(nums)==start+cont+1:
                        break 
                cont=cont+1
                si= existe(start+1+cont,nums,target-nums[start]*cont)
                no= existe(start+1+cont,nums,target)   
                # T(n) = c2*n + T( n - 1 ) + T( n - 1 ) + c3  , donde c2 = 12 y c3=12
            else:
                si= existe(start+1,nums,target-nums[start])
                no= existe(start+1,nums,target)
                # T(n) = c4 + T( n - 1 ) + T( n - 1 ) , donde c4 = 4
            si_no=si or no
            return bool(si_no)
            # T(n) = c2*n + T( n - 1 ) + T( n - 1 ) + c5  , donde c2 = 12 y c5= c3+ 7 =19
            # T(n) = c2(-n + 2^(n + 1) - 2) + c5(2^n - 1) + c1 2^(n - 1) 
            
"Test"
print(existe1([4,4,2,6,3,3],8)) 

