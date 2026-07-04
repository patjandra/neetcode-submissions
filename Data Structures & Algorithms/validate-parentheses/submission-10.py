class Solution:
    def isValid(self, s: str) -> bool:
        #make a dictionary mapping closing to opening
        #

        matching = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for i in range(len(s)):
            if stack and s[i] in matching and stack[-1] == matching[s[i]]:
                stack.pop()
            elif s[i] not in matching:
                stack.append(s[i])
            else:
                return False
        return not stack
    
            
            

        