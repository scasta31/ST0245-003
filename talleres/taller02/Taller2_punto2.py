"""
Estructura de datos y algoritmos 1
Taller 2 Punto 2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

""" 
def existe1(nums, target):
    return existe(0,nums,target)

def existe(start,nums,target):
    if target==0:
        return True
    else: 
        if start<len(nums):
            si= existe(start+1,nums,target-nums[start])
            no= existe(start+1,nums,target)
            si_no=si or no
            return bool(si_no)
            
"Test"
print(existe1([17,8,8,2],18)) 
