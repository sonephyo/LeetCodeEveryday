import math
class Solution:
  def search(self,arr, key):
    # TODO: Write your code here
    isAscending = True if arr[0] < arr[len(arr)-1] else False

    high = len(arr)-1
    low = 0

    while low <= high:
      mid = low + math.floor((high-low)/2)

      searchVal = arr[mid]
      if searchVal == key:
        return mid

      if (searchVal < key):
        if isAscending:
          low = mid+1
        else:
          high = mid-1

      if searchVal > key:
        if isAscending:  
          high = mid-1
        else:
          low = mid+1

    return -1  # element not found

sol = Solution()
sol.search([5,4,3,2,1], 5)