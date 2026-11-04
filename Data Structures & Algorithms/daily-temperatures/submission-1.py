class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            stk.append((i, temperatures[i]))
            while stk:
                top_i, top_temp = stk[-1]
                if top_temp < temperatures[i + 1]:
                    res[top_i] = i + 1 - top_i
                    stk.pop()
                else:
                    break
        return res