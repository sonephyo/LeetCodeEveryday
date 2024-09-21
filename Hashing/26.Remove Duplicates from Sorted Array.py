class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fp = 0
        cur = nums[0]

        for sp in range(1, len(nums)):
            if nums[sp] != cur:
                nums[fp+1] = nums[sp]
                cur = nums[fp+1]
                fp += 1
            

        return fp+1
                

        