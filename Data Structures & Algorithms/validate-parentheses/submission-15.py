class Solution:
    def isValid(self, s: str) -> bool:
        closing_opening = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack or closing_opening[i] != stack[-1]:
                    return False
                stack.pop()
        return True if not stack else False