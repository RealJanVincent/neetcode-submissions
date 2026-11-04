class Solution:
    def eval(self, x, y, op):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return x / y

    def evalRPN(self, tokens: List[str]) -> int:
        stc = []
        for t in tokens:
            if t not in "+-*/":
                stc.append(int(t))
            else:
                y = stc.pop()
                x = stc.pop()
                stc.append(int(self.eval(x, y, t)))
        return stc.pop()
        
        