class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        e = nums[0]
        c = 0
        for i in range(len(nums)):
            if nums[i] == e:
                c += 1
            else:
                c -= 1
            if c == 0:
                e = nums[i]
                c = 1
        return e