class Solution:
    def findMinRec(self, nums, start, end):
        if end - start == 1:
            return nums[start]
        elif end - start == 2:
            return min(nums[start], nums[end - 1])
        else:
            mid = (start + end) // 2
            if end - start == 3:
                return min(nums[start], nums[end - 1], nums[mid])
            else:
                start1 = start
                end1 = mid
                start2 = mid
                end2 = end
                if nums[start1] <= nums[end1 - 1] and nums[start2] <= nums[end2 - 1]:
                    return min(nums[start1], nums[start2])
                elif nums[start1] > nums[end1 - 1]:
                    return self.findMinRec(nums, start1, end1)
                else:
                   return self.findMinRec(nums, start2, end2) 


    def findMin(self, nums: List[int]) -> int:
        # cases:
        # when splited both ascending. Choose minimal
        # else search in one with descending
        return self.findMinRec(nums, 0, len(nums))