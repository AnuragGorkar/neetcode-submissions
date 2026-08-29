class MinStack:

    def __init__(self):
        self.minStack = []  # Main stack
        self.minValStack = []  # Auxiliary stack to track minimums

    def push(self, val: int) -> None:
        self.minStack.append(val)
        # Push the new minimum value onto the minValStack
        if len(self.minValStack) == 0 or val <= self.minValStack[-1]:
            self.minValStack.append(val)

    def pop(self) -> None:
        if len(self.minStack) == 0: return
        top = self.minStack.pop()
        # Pop from minValStack if the popped element is the current minimum
        if len(self.minValStack) > 0 and top == self.minValStack[-1]:
            self.minValStack.pop()

    def top(self) -> int:
        if len(self.minStack) == 0: return None
        return self.minStack[-1]

    def getMin(self) -> int:
        if len(self.minValStack) == 0: return None
        return self.minValStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()