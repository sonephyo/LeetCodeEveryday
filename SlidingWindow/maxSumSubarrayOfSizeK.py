from typing import List


def maximumSubarraySum(nums: List[int], k: int) -> int:

    maxSum = 0.0
    windowSum, windowStart = 0.0, 0

    tracking = set()

    for windowEnd in range(len(nums)):
        while nums[windowEnd] in tracking:
            windowSum -= nums[windowStart]
            tracking.remove(nums[windowStart])
            windowStart += 1
        windowSum += nums[windowEnd]
        tracking.add(nums[windowEnd])

        if windowEnd - windowStart + 1 == k:
            maxSum = max(maxSum, windowSum)
            windowSum -= nums[windowStart]
            tracking.remove(nums[windowStart])
            windowStart += 1
            

    return maxSum


print(maximumSubarraySum([1, 2, 3, 4], 3))

print(maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
