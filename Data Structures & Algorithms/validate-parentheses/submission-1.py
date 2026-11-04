class Solution:  

    def isValid(self, s: str) -> bool:
        pairs = { '{': '}', '(': ')', '[': ']'}
        lefts = pairs.keys()
        ls = []
        for p in s:
            if p in lefts:
                ls.append(p)
            elif not ls:
                return False
            elif not p == pairs[ls[-1]]:
                return False
            else:
                ls.pop()
        return len(ls) == 0
        