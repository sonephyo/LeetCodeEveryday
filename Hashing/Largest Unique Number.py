from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        # ToDo: Write Your Code Here.
        tracking = {}

        for i in A:
            tracking[i] = tracking.get(i, 0) + 1
        
        for i in tracking.keys():
            if tracking[i] == 1:
                maxUnique = max(maxUnique, i)
        return maxUnique
