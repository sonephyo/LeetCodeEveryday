

from typing import List


def pairWithTargetSum(arr: List[int], targetValue: int) -> List[int]:
    
    fp_index, sp_index = 0, len(arr)-1
    
    while (fp_index < sp_index):
        sum = arr[fp_index] + arr[sp_index]
        if sum == targetValue: 
            return [fp_index, sp_index]
        elif sum < targetValue:
            fp_index += 1
            continue
        else:
            sp_index -= 1
            continue
        

assert pairWithTargetSum([1, 2, 3, 4, 6], 6) == [1,3]
assert pairWithTargetSum([2, 5, 9, 11], 11) == [0,2]
