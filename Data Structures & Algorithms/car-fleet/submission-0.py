class Solution:
    def will_catch_up(self, i, head, data, target):
        time_to_finish_head = (target - data[head][0]) / data[head][1]
        time_to_finish_i = (target - data[i][0]) / data[i][1]
        return time_to_finish_i <= time_to_finish_head



    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [(position[i], speed[i]) for i in range(len(speed))]
        data.sort()
        n_fleet = 1
        head = len(data) - 1
        for i in range(len(data) - 2, -1, -1):
            if not self.will_catch_up(i, head,data, target):
                n_fleet += 1
                head = i
        return n_fleet