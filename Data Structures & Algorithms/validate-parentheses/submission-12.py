class Solution:
    def isValid(self, s: str) -> bool:
        #make a dictionary mapping closing:opening
        #make an empty stack
        #loop through s
        #if its a closing AND its the closing of the most recent opening ==> pop it off the stack
        #elif its an opening parentheses ==> put it on the stack
        #else we have nothing OR an invalid set of parenthese ==> return False
        #if we make it thoug

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