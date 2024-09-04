class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prefixList = []
        sumOfList = 0
        for index in range(len(nums)):
            sumOfList += nums[index]
            prefixList.append(sumOfList)

        for middleIndex in range(len(nums)):
            if middleIndex == 0:
                if prefixList[len(prefixList)-1] - prefixList[middleIndex] == 0:
                    return middleIndex
                continue
            
            if middleIndex == len(nums)-1:
                if prefixList[middleIndex-1] == 0:
                    return middleIndex 
                continue

            if prefixList[middleIndex-1] == prefixList[len(prefixList)-1] - prefixList[middleIndex]:
                return middleIndex

        return -1 

            


        