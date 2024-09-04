class Solution:
  def moveElements(self, arr):
    # TODO: Write your code here
    i = 0
    j = 1
    while j < len(arr):
      if arr[i] == arr[j]:
        j+= 1
        continue
      i += 1
      arr[i] = arr[j]
      j+=1

    return i+1

