class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        windowStart = 0
        leastCount = float('INF')
        windowSum = 0

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= target:
                leastCount = min(leastCount, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1

        return leastCount