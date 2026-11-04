class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        
        return i if nums[i] == val else i + 1