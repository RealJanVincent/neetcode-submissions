class MinStack:

    def __init__(self):
        self.mins = []
        self.stck = []
        

    def push(self, val: int) -> None:
        self.stck.append(val)
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)
        

    def pop(self) -> None:
        val = self.stck[-1]
        if val == self.mins[-1]:
            self.mins.pop()
        self.stck.pop()
        

    def top(self) -> int:
        return self.stck[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
