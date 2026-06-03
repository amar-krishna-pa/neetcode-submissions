class MinStack:

    def __init__(self):
        self.stack = []
        self.min_number = float('-inf')
        self.prefix_min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix_min_stack or self.prefix_min_stack[-1] >= val:
            self.prefix_min_stack.append(val)

    def pop(self) -> None:
        deleted_item = self.stack.pop()
        if self.prefix_min_stack[-1] == deleted_item:
            self.prefix_min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min_stack[-1]