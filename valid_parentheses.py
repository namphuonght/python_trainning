class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        
        for c in s:
            if stack and c in para_dict and para_dict[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            
        return not stack
            