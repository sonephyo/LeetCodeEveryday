class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        subsets.append([])

        for n in nums:
            for i in range(len(subsets)):
                set1 = list(subsets[i])
                set1.append(n)
                subsets.append(set1)
        return subsets
        