class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracking = set()
        alreadyRemoved = set()

        for i in s:
            if i in tracking:
                alreadyRemoved.add(i)
                tracking.remove(i)
            elif i in alreadyRemoved:
                pass
            else:
                tracking.add(i)
        
        
        for index in range(len(s)):
            if s[index] in tracking:
                return index


        return -1
        


            