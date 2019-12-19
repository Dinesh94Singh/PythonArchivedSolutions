"""
716. Max Stack
"""

"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements,
only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""


class MaxStack:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        curMax = self.peekMax()
        if curMax == None or x > curMax:
            curMax = x
        self.q.append((x, curMax))

    def pop(self) -> int:
        return self.q.pop()[0] if self.q else None

    def top(self) -> int:
        return self.q[-1][0] if self.q else None

    def peekMax(self) -> int:
        return self.q[-1][1] if self.q else None

    def popMax(self) -> int:
        curMax = self.q[-1][1]
        b = []
        while self.q[-1][0] != curMax:
            b.append(self.pop())
        self.pop()
        for i in reversed(b): self.push(i)
        return curMax

# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(5)
obj.push(1)
print(obj.popMax())
print(obj.peekMax())