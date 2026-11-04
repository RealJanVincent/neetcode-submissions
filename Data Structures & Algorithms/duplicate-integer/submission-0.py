class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for n in nums:
            if n in m:
                return True
            m[n] = 1
        return False