class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        m = self.getMin()
        print(m, 'is the m')
        if x < m:
            self.stack.append((x, x))
        else:
            self.stack.append((x, m))

    def pop(self) -> None:
        x = self.stack.pop()
        return x[0]

    def top(self) -> int:
        x = self.stack[-1]
        return x[0]

    def getMin(self) -> int:
        if len(self.stack) >= 1:
            return self.stack[-1][1]
        return float('inf')

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

m = MinStack()

print(m.push(0))
print(m.push(1))
print(m.push(0))
print(m.getMin())
print(m.pop())
print(m.getMin())