class Solution:
    def search_rec(self, nums, target, start, end):
        if start == end:
            return -1
        elif end - start == 1:
            return start if nums[start] == target else -1
        else:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.search_rec(nums, target, mid, end)
            else:
                return self.search_rec(nums, target, start, mid)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.search_rec(nums, target, 0, len(nums))
        