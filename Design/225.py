"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.top = None


    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.top = x


    def pop(self) -> int:
        for _ in range(len(self.queue1) - 1):
            self.top = self.queue1.popleft()
            self.queue2.append(self.top)
        res = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res


    def top(self) -> int:
        return self.top


    def empty(self) -> bool:
        return not len(self.queue1)



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
obj.push(11)
obj.push(12)
obj.push(13)
param_2 = obj.pop()
print(param_2)
param_2 = obj.pop()
print(param_2)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)
