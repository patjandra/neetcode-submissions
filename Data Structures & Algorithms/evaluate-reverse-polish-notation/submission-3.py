class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                add = stack.pop() + stack.pop()
                stack.append(add)
            elif tokens[i] == '-':
                a, b = stack.pop(), stack.pop()
                sub = b - a
                stack.append(sub)
            elif tokens[i] == '*':
                mul = stack.pop() * stack.pop()
                stack.append(mul)
            elif tokens[i] == '/':
                a, b = stack.pop(), stack.pop()
                div = b/a
                stack.append(int(div))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()