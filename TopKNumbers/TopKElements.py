from heapq import *

class Solution :
  def findKLargestNumbers(self, nums, k):
    min_heap = []

    for num in nums:
      heappush(min_heap, num)

      if (len(min_heap) > k):
        heappop(min_heap)
    return min_heap
