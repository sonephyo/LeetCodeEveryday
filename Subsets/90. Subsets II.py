class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        result.append([])

        for num in nums:
            list_to_add = []
            for li in result:
                new_li = li.copy()
                new_li.append(num)
                if not new_li in result:
                    list_to_add.append(new_li)
            result = result + list_to_add
            print(result)
        
        return result
    

        print(result)
        