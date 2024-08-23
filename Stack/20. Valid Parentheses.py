class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        connection = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in connection and stack:
                if stack[-1] != connection[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        if stack:
            return False
        
        return True

            

            
        