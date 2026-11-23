class MinStack:

    def __init__(self):
        self.min_stack = []
        self.mono_stack = []
        
    def push(self, value: int) -> None:
        self.min_stack.append(value)
        
        if ((not self.mono_stack) or (value <= self.mono_stack[-1])):
            self.mono_stack.append(value)

    def pop(self) -> None:
        if (self.mono_stack):
            if (self.min_stack[-1] == self.mono_stack[-1]):
                self.mono_stack.pop()

        self.min_stack.pop()
        
    def top(self) -> int:
        return self.min_stack[-1]
        
    def getMin(self) -> int:
        return self.mono_stack[-1]
