class Solution:
    def isValid(self, s: str) -> bool:
        # create mapping of closing to opening
        # iterate string and store any opening brackets in a stack
        # if we find a closing bracket, if that brackets mapping is not the same as the top of the stack, return False

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