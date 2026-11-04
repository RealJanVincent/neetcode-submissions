class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        elif len(temperatures) == 1:
            return [0]
        else:
            result = self.dailyTemperatures(temperatures[1:])
            days = 0
            for i in range(1, len(temperatures)):
                if temperatures[0] < temperatures[i]:
                    days = i
                    break
            return [days] + result