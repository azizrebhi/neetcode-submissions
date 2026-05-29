class MinStack:

    def __init__(self):
        self.elements=[]
        self.minstack=[]
    def push(self, val: int) -> None:
        if not self.minstack or val<self.minstack[-1]:
            self.minstack.append(val)
        else : 
            self.minstack.append(self.minstack[-1])
        self.elements.append(val)
    def pop(self) -> None:
        if not self.elements : 
            return "stack empty"
        self.elements.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        if not self.elements : 
            return "stack empty"
        return self.elements[-1]
    def getMin(self) -> int:
        return self.minstack[-1]

        
