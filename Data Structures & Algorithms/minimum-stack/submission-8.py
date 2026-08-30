class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=[]
    def push(self, val: int) -> None:
        if not self.mini :
            self.mini.append(val)
            self.stack.append(val)
            return
        if self.mini[-1]>val:
            self.mini.append(val)
        else :
            self.mini.append(self.mini[-1])
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
