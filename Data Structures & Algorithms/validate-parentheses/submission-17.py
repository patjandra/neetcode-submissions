class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack or stack[-1] != closeOpen[i]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False
            