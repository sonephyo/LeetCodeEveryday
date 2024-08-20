

def missingNumber(nums):
    i = 0
    while i < len(nums):
        print(nums)
        if nums[i] != i and nums[i] < len(nums):
            nums = swap(nums[i], i, nums )
        else:
            i += 1
        
    for i,v in enumerate(nums):
        if i != v:
            return i
    return len(nums)
            

    
    
    
    
print(missingNumber([9,6,4,2,3,5,7,0,1]))