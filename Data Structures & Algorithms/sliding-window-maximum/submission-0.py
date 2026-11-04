class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res = []
        while r <= len(nums):
            res.append(max(nums[l:r]))
            l += 1
            r += 1
        return res