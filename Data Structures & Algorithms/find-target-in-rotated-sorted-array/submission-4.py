class Solution:
    def search_i(self, nums, target, start, end):
        delta = end - start
        if delta < 1:
            return -1
        mid = start + delta // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # 1 2 3 |4| 5 6 t 1 
            # 2 3 4 |5| 6 1 t 1
            # 2 3 4 |5| 6 7 t 1
            if nums[start] <= target:
                return self.search_i(nums, target, start, mid)
            elif nums[end - 1] < nums[mid]:
                return self.search_i(nums, target, mid + 1, end)
            else:
                return self.search_i(nums, target, start, mid)
        else:
            # 1 2 3 |4| 5 6 t 6 
            # 6 1 2 |3| 4 5 t 6
            # 0 1 2 |3| 4 5 t 6
            if nums[end - 1] >= target:
                return self.search_i(nums, target, mid + 1, end)
            elif nums[start] > nums[mid]:
                return self.search_i(nums, target, start, mid)
            else:
                return self.search_i(nums, target, mid + 1, end)
            

    def search(self, nums: List[int], target: int) -> int:
        return self.search_i(nums, target, 0, len(nums))