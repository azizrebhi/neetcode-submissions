class MinStack:

    def __init__(self):
        self.items=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val, current_min))

    def pop(self) -> None:
        if not self.items:
            raise IndexError("Pop from empty stack")
        
        self.min_stack.pop()
        return self.items.pop()

    def top(self) -> int:
        if not self.items : 
            raise IndexError("empty stack")
        return self.items[-1]

    def getMin(self) -> int:
        if not self.items : 
            raise IndexError("empty stack")
        return self.min_stack[-1]
        
        
        
        
