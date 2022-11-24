class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        c_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for c in s:
            if c not in c_map:
                stack.append(c)
            elif not stack or stack[-1] != c_map[c]:
                return False
            else:
                stack.pop()
                
        return not stack