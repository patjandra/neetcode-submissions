class MinStack:

    def __init__(self):
        self.stack = []
        self.sort = []

    def push(self, val: int) -> None:
        if not self.sort:
            self.sort.append(val)
        else:
            if val > self.sort[-1]:
                prev = self.sort.pop()
                self.sort.append(val)
                self.sort.append(prev)
            else:
                self.sort.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.sort.remove(popped)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sort[-1]